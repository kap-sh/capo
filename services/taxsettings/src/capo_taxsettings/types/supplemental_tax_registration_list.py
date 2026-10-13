"""Generated from Smithy shape ``com.amazonaws.taxsettings#SupplementalTaxRegistrationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.supplemental_tax_registration

SupplementalTaxRegistrationList: TypeAlias = list[
    "capo_taxsettings.types.supplemental_tax_registration.SupplementalTaxRegistration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalTaxRegistrationList) -> list:
    import capo_taxsettings.types.supplemental_tax_registration

    out: list = []
    for item in value:
        out.append(
            capo_taxsettings.types.supplemental_tax_registration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SupplementalTaxRegistrationList:
    import capo_taxsettings.types.supplemental_tax_registration

    out: SupplementalTaxRegistrationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_taxsettings.types.supplemental_tax_registration.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SupplementalTaxRegistrationList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
