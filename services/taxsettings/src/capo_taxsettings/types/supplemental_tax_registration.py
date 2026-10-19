"""Generated from Smithy shape ``com.amazonaws.taxsettings#SupplementalTaxRegistration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.address
    import capo_taxsettings.types.generic_string
    import capo_taxsettings.types.legal_name
    import capo_taxsettings.types.registration_id
    import capo_taxsettings.types.supplemental_tax_registration_type
    import capo_taxsettings.types.tax_registration_status


class SupplementalTaxRegistration(TypedDict, closed=True):
    registration_id: "capo_taxsettings.types.registration_id.RegistrationId"
    """<p> The supplemental TRN unique identifier. </p>"""
    registration_type: "capo_taxsettings.types.supplemental_tax_registration_type.SupplementalTaxRegistrationType"
    """<p> Type of supplemental TRN. Currently, this can only be VAT. </p>"""
    legal_name: "capo_taxsettings.types.legal_name.LegalName"
    """<p> The legal name associated with your TRN registration. </p>"""
    address: "capo_taxsettings.types.address.Address"
    authority_id: "capo_taxsettings.types.generic_string.GenericString"
    """<p> Unique authority ID for the supplemental TRN. </p>"""
    status: "capo_taxsettings.types.tax_registration_status.TaxRegistrationStatus"
    """<p> The status of your TRN. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalTaxRegistration) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    import capo_taxsettings.types.supplemental_tax_registration_type

    out["registrationType"] = (
        capo_taxsettings.types.supplemental_tax_registration_type.serialize_json(
            value["registration_type"]
        )
    )
    out["legalName"] = value["legal_name"]
    import capo_taxsettings.types.address

    out["address"] = capo_taxsettings.types.address.serialize_json(value["address"])
    out["authorityId"] = value["authority_id"]
    import capo_taxsettings.types.tax_registration_status

    out["status"] = capo_taxsettings.types.tax_registration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> SupplementalTaxRegistration:
    out: SupplementalTaxRegistration = {}  # type: ignore[typeddict-item]
    if data.get("registrationId") is not None:
        out["registration_id"] = data["registrationId"]
    else:
        out["registration_id"] = ""
    if data.get("registrationType") is not None:
        import capo_taxsettings.types.supplemental_tax_registration_type

        out["registration_type"] = (
            capo_taxsettings.types.supplemental_tax_registration_type.deserialize_json(
                data["registrationType"]
            )
        )
    else:
        import typing

        out["registration_type"] = typing.cast(
            "capo_taxsettings.types.supplemental_tax_registration_type.SupplementalTaxRegistrationType",
            "",
        )
    if data.get("legalName") is not None:
        out["legal_name"] = data["legalName"]
    else:
        out["legal_name"] = ""
    if data.get("address") is not None:
        import capo_taxsettings.types.address

        out["address"] = capo_taxsettings.types.address.deserialize_json(
            data["address"]
        )
    else:
        raise DeserializationError("SupplementalTaxRegistration.address required")
    if data.get("authorityId") is not None:
        out["authority_id"] = data["authorityId"]
    else:
        out["authority_id"] = ""
    if data.get("status") is not None:
        import capo_taxsettings.types.tax_registration_status

        out["status"] = capo_taxsettings.types.tax_registration_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_taxsettings.types.tax_registration_status.TaxRegistrationStatus", ""
        )
    return out
