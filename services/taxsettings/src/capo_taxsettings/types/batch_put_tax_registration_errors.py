"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchPutTaxRegistrationErrors``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.batch_put_tax_registration_error

BatchPutTaxRegistrationErrors: TypeAlias = list[
    "capo_taxsettings.types.batch_put_tax_registration_error.BatchPutTaxRegistrationError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutTaxRegistrationErrors) -> list:
    import capo_taxsettings.types.batch_put_tax_registration_error

    out: list = []
    for item in value:
        out.append(
            capo_taxsettings.types.batch_put_tax_registration_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchPutTaxRegistrationErrors:
    import capo_taxsettings.types.batch_put_tax_registration_error

    out: BatchPutTaxRegistrationErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_taxsettings.types.batch_put_tax_registration_error.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: BatchPutTaxRegistrationErrors) -> list[Any]:
    import capo_taxsettings.types.batch_put_tax_registration_error

    return [
        capo_taxsettings.types.batch_put_tax_registration_error.redact_sensitive(item)
        for item in value
    ]
