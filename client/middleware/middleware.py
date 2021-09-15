from datetime import date
from re import I
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
from client.django_tenants_edited.middleware.default import DefaultTenantMiddleware
from django_tenants.utils import get_public_schema_name
from client.django_tenants_edited.middleware.main import TenantMainMiddleware
from rest_framework.exceptions import ValidationError


class RequestIDTenantMiddleware(DefaultTenantMiddleware):
    def get_tenant(self, model, hostname, request):
        try:

            public_schema = model.objects.get(schema_name=get_public_schema_name())

        except ObjectDoesNotExist:

            public_schema = model.objects.create(
                domain_url=hostname,
                schema_name=get_public_schema_name(),
                tenant_name=get_public_schema_name().capitalize(),
                paid_until=date.today() + relativedelta(months=+1),
                on_trial=True,
            )

        public_schema.save()
        x_request_id = request.META.get("HTTP_X_REQUEST_ID", public_schema.tenant_uuid)
        tenant_model = model.objects.get(tenant_uuid=x_request_id)

        return tenant_model if not None else public_schema
