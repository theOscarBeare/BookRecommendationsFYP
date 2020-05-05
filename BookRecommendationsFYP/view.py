import logging
import os

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, '../frontend/templates/HTMLFrontend/index.html')


class FrontendAppView(View):
    """
    Serves the compiled HTMLFrontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'src', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )




