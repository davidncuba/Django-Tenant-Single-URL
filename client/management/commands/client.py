import datetime
from django.core.management.base import BaseCommand, CommandError
from client.models import Client
from django.utils.text import capfirst
from django.core import exceptions


class Command(BaseCommand):
    help = "Create a client"

    def add_arguments(self, parser):
        """
        Args:
            parser:
        Returns:
        """
        for field_name in Client.REQUIRED_FIELDS:
            parser.add_argument(
                "--%s" % field_name,
                action="append",
                help="Specifies the %s for the superuser." % field_name,
            )

    def handle(self, *args, **options):
        user_data = {}
        for field_name in Client.REQUIRED_FIELDS:
            field = Client._meta.get_field(field_name)
            user_data[field_name] = options[field_name]
            while user_data[field_name] is None:
                message = self._get_input_message(field)
                input_value = self.get_input_data(field, message)
                user_data[field_name] = input_value

        tenant = Client.objects.create(**user_data)
        tenant.save()
        if options["verbosity"] >= 1:
            self.stdout.write("Client created successfully.")

    def get_input_data(self, field, message, default=None):
        """
        Override this method if you want to customize data inputs or
        validation exceptions.
        """
        raw_value = input(message)
        if default and raw_value == "":
            raw_value = default
        try:
            val = field.clean(raw_value, None)
        except exceptions.ValidationError as e:
            self.stderr.write("Error: %s" % "; ".join(e.messages))
            val = None

        return val

    @staticmethod
    def _get_input_message(field, default=None):
        return "%s%s%s: " % (
            capfirst(field.verbose_name),
            " (leave blank to use '%s')" % default if default else "",
            " (%s.%s)"
            % (
                field.remote_field.model._meta.object_name,
                field.m2m_target_field_name()
                if field.many_to_many
                else field.remote_field.field_name,
            )
            if field.remote_field
            else "",
        )
