# pages/views.py

from django.shortcuts import render
from django.views.generic import TemplateView  # new


# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greetings": "THAnk you FOR visitING",
    }

    return render(request, "home.html", context)


class AboutPageView(TemplateView):  # new
    template_name = "about.html"  # new

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)  # new
        context["contact_address"] = "1600 Pennsylvania Ave, Washington DC, DC 20500"
        context["phone_number"] = "202 208 1631"
        return context


class ProductsPageView(TemplateView):  # new
    template_name = "products.html"  # new

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["products_list"] = (
            "Venomous Vortex",
            "Shadowstrike Blade",
            "Inferno Catalyst",
            "Raptor’s Fury",
        )

        return context
