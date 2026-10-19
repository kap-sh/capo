"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.additional_info_response
    import capo_taxsettings.types.address
    import capo_taxsettings.types.certified_email_id
    import capo_taxsettings.types.legal_name
    import capo_taxsettings.types.registration_id
    import capo_taxsettings.types.sector
    import capo_taxsettings.types.tax_document_metadatas
    import capo_taxsettings.types.tax_registration_status
    import capo_taxsettings.types.tax_registration_type


class TaxRegistration(TypedDict, closed=True):
    registration_id: "capo_taxsettings.types.registration_id.RegistrationId"
    """<p> Your tax registration unique identifier. </p>"""
    registration_type: (
        "capo_taxsettings.types.tax_registration_type.TaxRegistrationType"
    )
    """<p>Type of your tax registration. </p>"""
    legal_name: "capo_taxsettings.types.legal_name.LegalName"
    """<p> The legal name associated with your TRN registration. </p>"""
    status: "capo_taxsettings.types.tax_registration_status.TaxRegistrationStatus"
    """<p> The status of your TRN. This can be either <code>Verified</code>, <code>Pending</code>, <code>Deleted</code>, or <code>Rejected</code>. </p>"""
    sector: NotRequired["capo_taxsettings.types.sector.Sector"]
    """<p>The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government. Note that certain values may not applicable for the request country. Please refer to country specific information in API document. </p>"""
    tax_document_metadatas: NotRequired[
        "capo_taxsettings.types.tax_document_metadatas.TaxDocumentMetadatas"
    ]
    """<p>The metadata for your tax document.</p>"""
    certified_email_id: NotRequired[
        "capo_taxsettings.types.certified_email_id.CertifiedEmailId"
    ]
    """<p>The email address to receive VAT invoices.</p>"""
    additional_tax_information: NotRequired[
        "capo_taxsettings.types.additional_info_response.AdditionalInfoResponse"
    ]
    """<p> Additional tax information associated with your TRN. </p>"""
    legal_address: "capo_taxsettings.types.address.Address"
    """<p> The legal address associated with your TRN registration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistration) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    import capo_taxsettings.types.tax_registration_type

    out["registrationType"] = (
        capo_taxsettings.types.tax_registration_type.serialize_json(
            value["registration_type"]
        )
    )
    out["legalName"] = value["legal_name"]
    import capo_taxsettings.types.tax_registration_status

    out["status"] = capo_taxsettings.types.tax_registration_status.serialize_json(
        value["status"]
    )
    if "sector" in value:
        import capo_taxsettings.types.sector

        out["sector"] = capo_taxsettings.types.sector.serialize_json(value["sector"])
    if "tax_document_metadatas" in value:
        import capo_taxsettings.types.tax_document_metadatas

        out["taxDocumentMetadatas"] = (
            capo_taxsettings.types.tax_document_metadatas.serialize_json(
                value["tax_document_metadatas"]
            )
        )
    if "certified_email_id" in value:
        out["certifiedEmailId"] = value["certified_email_id"]
    if "additional_tax_information" in value:
        import capo_taxsettings.types.additional_info_response

        out["additionalTaxInformation"] = (
            capo_taxsettings.types.additional_info_response.serialize_json(
                value["additional_tax_information"]
            )
        )
    import capo_taxsettings.types.address

    out["legalAddress"] = capo_taxsettings.types.address.serialize_json(
        value["legal_address"]
    )
    return out


def deserialize_json(data: dict) -> TaxRegistration:
    out: TaxRegistration = {}  # type: ignore[typeddict-item]
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
    else:
        out["legal_name"] = ""
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
    if data.get("sector") is not None:
        import capo_taxsettings.types.sector

        out["sector"] = capo_taxsettings.types.sector.deserialize_json(data["sector"])
    if data.get("taxDocumentMetadatas") is not None:
        import capo_taxsettings.types.tax_document_metadatas

        out["tax_document_metadatas"] = (
            capo_taxsettings.types.tax_document_metadatas.deserialize_json(
                data["taxDocumentMetadatas"]
            )
        )
    if data.get("certifiedEmailId") is not None:
        out["certified_email_id"] = data["certifiedEmailId"]
    if data.get("additionalTaxInformation") is not None:
        import capo_taxsettings.types.additional_info_response

        out["additional_tax_information"] = (
            capo_taxsettings.types.additional_info_response.deserialize_json(
                data["additionalTaxInformation"]
            )
        )
    if data.get("legalAddress") is not None:
        import capo_taxsettings.types.address

        out["legal_address"] = capo_taxsettings.types.address.deserialize_json(
            data["legalAddress"]
        )
    else:
        raise DeserializationError("TaxRegistration.legal_address required")
    return out
