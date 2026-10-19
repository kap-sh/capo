"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.additional_info_request
    import capo_taxsettings.types.address
    import capo_taxsettings.types.certified_email_id
    import capo_taxsettings.types.legal_name
    import capo_taxsettings.types.registration_id
    import capo_taxsettings.types.sector
    import capo_taxsettings.types.tax_registration_type
    import capo_taxsettings.types.verification_details


class TaxRegistrationEntry(TypedDict, closed=True):
    registration_id: "capo_taxsettings.types.registration_id.RegistrationId"
    """<p>Your tax registration unique identifier. </p>"""
    registration_type: (
        "capo_taxsettings.types.tax_registration_type.TaxRegistrationType"
    )
    """<p> Your tax registration type. This can be either <code>VAT</code> or <code>GST</code>. </p>"""
    legal_name: NotRequired["capo_taxsettings.types.legal_name.LegalName"]
    """<p>The legal name associated with your TRN. </p> <note> <p>If you're setting a TRN in Brazil, you don't need to specify the legal name. For TRNs in other countries, you must specify the legal name.</p> </note>"""
    legal_address: NotRequired["capo_taxsettings.types.address.Address"]
    """<p>The legal address associated with your TRN.</p> <note> <p>If you're setting a TRN in Brazil for the CNPJ tax type, you don't need to specify the legal address. </p> <p>For TRNs in other countries and for CPF tax types Brazil, you must specify the legal address.</p> </note>"""
    sector: NotRequired["capo_taxsettings.types.sector.Sector"]
    """<p>The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government.Note that certain values may not applicable for the request country. Please refer to country specific information in API document. </p>"""
    additional_tax_information: NotRequired[
        "capo_taxsettings.types.additional_info_request.AdditionalInfoRequest"
    ]
    """<p> Additional tax information associated with your TRN. You only need to specify this parameter if Amazon Web Services collects any additional information for your country within <a>AdditionalInfoRequest</a>.</p>"""
    verification_details: NotRequired[
        "capo_taxsettings.types.verification_details.VerificationDetails"
    ]
    """<p>Additional details needed to verify your TRN information in Brazil. You only need to specify this parameter when you set a TRN in Brazil that is the CPF tax type.</p> <note> <p>Don't specify this parameter to set a TRN in Brazil of the CNPJ tax type or to set a TRN for another country. </p> </note>"""
    certified_email_id: NotRequired[
        "capo_taxsettings.types.certified_email_id.CertifiedEmailId"
    ]
    """<p>The email address to receive VAT invoices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationEntry) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    import capo_taxsettings.types.tax_registration_type

    out["registrationType"] = (
        capo_taxsettings.types.tax_registration_type.serialize_json(
            value["registration_type"]
        )
    )
    if "legal_name" in value:
        out["legalName"] = value["legal_name"]
    if "legal_address" in value:
        import capo_taxsettings.types.address

        out["legalAddress"] = capo_taxsettings.types.address.serialize_json(
            value["legal_address"]
        )
    if "sector" in value:
        import capo_taxsettings.types.sector

        out["sector"] = capo_taxsettings.types.sector.serialize_json(value["sector"])
    if "additional_tax_information" in value:
        import capo_taxsettings.types.additional_info_request

        out["additionalTaxInformation"] = (
            capo_taxsettings.types.additional_info_request.serialize_json(
                value["additional_tax_information"]
            )
        )
    if "verification_details" in value:
        import capo_taxsettings.types.verification_details

        out["verificationDetails"] = (
            capo_taxsettings.types.verification_details.serialize_json(
                value["verification_details"]
            )
        )
    if "certified_email_id" in value:
        out["certifiedEmailId"] = value["certified_email_id"]
    return out


def deserialize_json(data: dict) -> TaxRegistrationEntry:
    out: TaxRegistrationEntry = {}  # type: ignore[typeddict-item]
    if data.get("registrationId") is not None:
        out["registration_id"] = data["registrationId"]
    else:
        out["registration_id"] = ""
    if data.get("registrationType") is not None:
        import capo_taxsettings.types.tax_registration_type

        out["registration_type"] = (
            capo_taxsettings.types.tax_registration_type.deserialize_json(
                data["registrationType"]
            )
        )
    else:
        import typing

        out["registration_type"] = typing.cast(
            "capo_taxsettings.types.tax_registration_type.TaxRegistrationType", ""
        )
    if data.get("legalName") is not None:
        out["legal_name"] = data["legalName"]
    if data.get("legalAddress") is not None:
        import capo_taxsettings.types.address

        out["legal_address"] = capo_taxsettings.types.address.deserialize_json(
            data["legalAddress"]
        )
    if data.get("sector") is not None:
        import capo_taxsettings.types.sector

        out["sector"] = capo_taxsettings.types.sector.deserialize_json(data["sector"])
    if data.get("additionalTaxInformation") is not None:
        import capo_taxsettings.types.additional_info_request

        out["additional_tax_information"] = (
            capo_taxsettings.types.additional_info_request.deserialize_json(
                data["additionalTaxInformation"]
            )
        )
    if data.get("verificationDetails") is not None:
        import capo_taxsettings.types.verification_details

        out["verification_details"] = (
            capo_taxsettings.types.verification_details.deserialize_json(
                data["verificationDetails"]
            )
        )
    if data.get("certifiedEmailId") is not None:
        out["certified_email_id"] = data["certifiedEmailId"]
    return out
