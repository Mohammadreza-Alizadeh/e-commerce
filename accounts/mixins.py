from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.conf import settings


class LimitLoginUser:

    redirect_to_view = 'ecommerce:HomeView' 

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect(self.redirect_to_view)

             