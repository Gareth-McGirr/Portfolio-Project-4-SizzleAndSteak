from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from menu.forms import CreateMenuForm
from .models import Menu


class MenuListView(ListView):
    """ View menu list """
    model = Menu
    template_name = 'menu/menus.html'

    def get_queryset(self):
        return Menu.objects.filter(active=True)


class ManageMenusListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """ Manage menu view"""
    model = Menu
    template_name = 'menu/managemenus.html'

    def get_queryset(self):
        return Menu.objects.all()

    def test_func(self):
        """ Check user is superuser or throw 403"""
        if self.request.user.is_staff:
            return True
        else:
            return False


class CreateMenuView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Create menu view to create a menu if user is staff """
    model = Menu
    form_class = CreateMenuForm
    template_name = 'menu/create_menu.html'
    success_url = '/menu/menus'

    def test_func(self):
        """ Test user is staff else throw 403 """
        if self.request.user.is_staff:
            return True
        else:
            return False

    def form_valid(self, form):
        """ Assign create_by to creator """
        form.instance.created_by = self.request.user

        messages.success(
            self.request,
            'Successfully created menu'
        )

        return super(CreateMenuView, self).form_valid(form)


class EditMenuView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to provide a Form to the user
    to edit a menu
    """
    form_class = CreateMenuForm
    template_name = 'menu/edit_menu.html'
    success_url = "/menu/managemenus"
    model = Menu

    def form_valid(self, form):
        """ Show toast on success """
        messages.success(
            self.request,
            'Successfully updated menu'
        )
        return super(EditMenuView, self).form_valid(form)

    def test_func(self):
        """ Check user is staff else throw 403 """
        return self.request.user.is_staff


class DeleteMenuView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete a menu """
    model = Menu
    success_url = "/menu/managemenus/"

    def test_func(self):
        """ Test user is staff else throw 403 """
        return self.request.user.is_staff
