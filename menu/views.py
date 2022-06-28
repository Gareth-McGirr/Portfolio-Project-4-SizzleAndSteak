from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from menu.forms import CreateMenuForm
from .models import Menu, MenuItem


class MenuListView(generic.ListView):

    model = Menu
    template_name = 'menu/menus.html'
    def get_queryset(self):
        return Menu.objects.filter(active=True)


class ManageMenusListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):

    model = Menu
    template_name = 'menu/managemenus.html'
    def get_queryset(self):
        return Menu.objects.all()

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False


class CreateMenuView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Menu
    form_class = CreateMenuForm
    template_name = 'menu/create_menu.html'
    success_url = '/menu/menus'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False
    def form_valid(self, form):
        form.instance.created_by = self.request.user

        return super(CreateMenuView, self).form_valid(form)


class EditMenuView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    A view to provide a Form to the user
    to edit a menu
    """
    form_class = CreateMenuForm
    template_name = 'menu/edit_menu.html'
    success_url = "/menu/managemenus"
    model = Menu

    def test_func(self):
        return self.request.user.is_staff


class DeleteMenuView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ A view to delete a menu """
    model = Menu
    success_url = "/menu/managemenus/"

    def test_func(self):
        return self.request.user.is_staff
