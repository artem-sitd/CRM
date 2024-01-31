from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse_lazy


def groups_required(*group_names):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if any(request.user.groups.filter(name=group).exists() for group in group_names):
                return view_func(request, *args, **kwargs)
            else:
                return redirect(reverse_lazy('users:stat'))  # Редирект, если группа не найдена

        return _wrapped_view

    return decorator
