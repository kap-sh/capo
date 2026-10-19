"""Generated from Smithy shape ``com.amazonaws.taxsettings#RomaniaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.tax_registration_number_type


class RomaniaAdditionalInfo(TypedDict, closed=True):
    tax_registration_number_type: (
        "capo_taxsettings.types.tax_registration_number_type.TaxRegistrationNumberType"
    )
    """<p> The tax registration number type. The value can be <code>TaxRegistrationNumber</code> or <code>LocalRegistrationNumber</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RomaniaAdditionalInfo) -> dict:
    out: dict = {}
    import capo_taxsettings.types.tax_registration_number_type

    out["taxRegistrationNumberType"] = (
        capo_taxsettings.types.tax_registration_number_type.serialize_json(
            value["tax_registration_number_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RomaniaAdditionalInfo:
    out: RomaniaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("taxRegistrationNumberType") is not None:
        import capo_taxsettings.types.tax_registration_number_type

        out["tax_registration_number_type"] = (
            capo_taxsettings.types.tax_registration_number_type.deserialize_json(
                data["taxRegistrationNumberType"]
            )
        )
    else:
        import typing

        out["tax_registration_number_type"] = typing.cast(
            "capo_taxsettings.types.tax_registration_number_type.TaxRegistrationNumberType",
            "",
        )
    return out
