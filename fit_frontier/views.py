from django.shortcuts import render


def error_404(request, exception):
    """
    Handles 404 HTTP response status - Page Not Found
    """
    return render(request, '404.html', status=404)
