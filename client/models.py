from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
import uuid
import os
from django_tenants.postgresql_backend.base import _check_schema_name

# Create your models here.


class Client(TenantMixin):
    REQUIRED_FIELDS = ("tenant_name", "paid_until", "schema_name", "on_trial")
    tenant_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    tenant_uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    domain_url = models.URLField(blank=True, null=True, default=os.getenv("DOMAIN"))

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    pass
