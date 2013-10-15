# -*- coding:utf-8 -*-
from django.contrib import admin
from realty.models import *

realty_models = [
    State,
    Metro,
    District,
    Developer,
    DeveloperProject,
    RealtyType,
    Realty,
    PropertyName,
    Property,
    Photo
]

for model in realty_models:
    admin.site.register(model)
