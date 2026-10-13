"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#UpdateBenefitApplicationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_application_description
    import capo_partnercentral_benefits.types.benefit_application_identifier
    import capo_partnercentral_benefits.types.benefit_application_name
    import capo_partnercentral_benefits.types.catalog_name
    import capo_partnercentral_benefits.types.contacts
    import capo_partnercentral_benefits.types.file_input_details


class UpdateBenefitApplicationInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    client_token: "str"
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the update request.</p>"""
    name: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_name.BenefitApplicationName"
    ]
    """<p>The updated human-readable name for the benefit application.</p>"""
    description: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_description.BenefitApplicationDescription"
    ]
    """<p>The updated detailed description of the benefit application.</p>"""
    identifier: "capo_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to update.</p>"""
    revision: "str"
    """<p>The current revision number of the benefit application to ensure optimistic concurrency control.</p>"""
    benefit_application_details: NotRequired["object"]
    """<p>Updated detailed information and requirements specific to the benefit being requested.</p>"""
    partner_contacts: NotRequired[
        "capo_partnercentral_benefits.types.contacts.Contacts"
    ]
    """<p>Updated contact information for partner representatives responsible for this benefit application.</p>"""
    file_details: NotRequired[
        "capo_partnercentral_benefits.types.file_input_details.FileInputDetails"
    ]
    """<p>Updated supporting documents and files attached to the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Identifier"] = value["identifier"]
    out["Revision"] = value["revision"]
    if "benefit_application_details" in value:
        out["BenefitApplicationDetails"] = value["benefit_application_details"]
    if "partner_contacts" in value:
        import capo_partnercentral_benefits.types.contacts

        out["PartnerContacts"] = (
            capo_partnercentral_benefits.types.contacts.serialize_aws_json_1_0(
                value["partner_contacts"]
            )
        )
    if "file_details" in value:
        import capo_partnercentral_benefits.types.file_input_details

        out["FileDetails"] = (
            capo_partnercentral_benefits.types.file_input_details.serialize_aws_json_1_0(
                value["file_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBenefitApplicationInput:
    out: UpdateBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("UpdateBenefitApplicationInput.catalog required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "UpdateBenefitApplicationInput.client_token required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("UpdateBenefitApplicationInput.identifier required")
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    else:
        raise DeserializationError("UpdateBenefitApplicationInput.revision required")
    if data.get("BenefitApplicationDetails") is not None:
        out["benefit_application_details"] = data["BenefitApplicationDetails"]
    if data.get("PartnerContacts") is not None:
        import capo_partnercentral_benefits.types.contacts

        out["partner_contacts"] = (
            capo_partnercentral_benefits.types.contacts.deserialize_aws_json_1_0(
                data["PartnerContacts"]
            )
        )
    if data.get("FileDetails") is not None:
        import capo_partnercentral_benefits.types.file_input_details

        out["file_details"] = (
            capo_partnercentral_benefits.types.file_input_details.deserialize_aws_json_1_0(
                data["FileDetails"]
            )
        )
    return out


def redact_sensitive(value: UpdateBenefitApplicationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "partner_contacts" in value:
        import capo_partnercentral_benefits.types.contacts

        out["partner_contacts"] = (
            capo_partnercentral_benefits.types.contacts.redact_sensitive(
                value["partner_contacts"]
            )
        )
    return out
