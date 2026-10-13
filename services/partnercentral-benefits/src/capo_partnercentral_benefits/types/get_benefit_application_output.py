"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#GetBenefitApplicationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.arn
    import capo_partnercentral_benefits.types.arns
    import capo_partnercentral_benefits.types.benefit_application_description
    import capo_partnercentral_benefits.types.benefit_application_id
    import capo_partnercentral_benefits.types.benefit_application_name
    import capo_partnercentral_benefits.types.benefit_application_stage
    import capo_partnercentral_benefits.types.benefit_application_status
    import capo_partnercentral_benefits.types.benefit_id
    import capo_partnercentral_benefits.types.catalog_name
    import capo_partnercentral_benefits.types.contacts
    import capo_partnercentral_benefits.types.file_details
    import capo_partnercentral_benefits.types.fulfillment_types
    import capo_partnercentral_benefits.types.programs
    import capo_partnercentral_benefits.types.status_reason_code
    import capo_partnercentral_benefits.types.status_reason_codes
    import capo_partnercentral_benefits.types.timestamp


class GetBenefitApplicationOutput(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_id.BenefitApplicationId"
    ]
    """<p>The unique identifier of the benefit application.</p>"""
    arn: NotRequired["capo_partnercentral_benefits.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the benefit application.</p>"""
    catalog: NotRequired["capo_partnercentral_benefits.types.catalog_name.CatalogName"]
    """<p>The catalog identifier that the benefit application belongs to.</p>"""
    benefit_id: NotRequired["capo_partnercentral_benefits.types.benefit_id.BenefitId"]
    """<p>The identifier of the benefit being requested in this application.</p>"""
    name: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_name.BenefitApplicationName"
    ]
    """<p>The human-readable name of the benefit application.</p>"""
    description: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_description.BenefitApplicationDescription"
    ]
    """<p>A detailed description of the benefit application.</p>"""
    fulfillment_types: NotRequired[
        "capo_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
    ]
    """<p>The fulfillment types requested for this benefit application.</p>"""
    benefit_application_details: NotRequired["object"]
    """<p>Detailed information and requirements specific to the benefit being requested.</p>"""
    programs: NotRequired["capo_partnercentral_benefits.types.programs.Programs"]
    """<p>The AWS partner programs associated with this benefit application.</p>"""
    status: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_status.BenefitApplicationStatus"
    ]
    """<p>The current processing status of the benefit application.</p>"""
    stage: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_stage.BenefitApplicationStage"
    ]
    """<p>The current stage in the benefit application processing workflow.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information explaining the current status of the benefit application.</p>"""
    status_reason_code: NotRequired[
        "capo_partnercentral_benefits.types.status_reason_code.StatusReasonCode"
    ]
    """<p>A standardized code representing the reason for the current status.</p>"""
    status_reason_codes: NotRequired[
        "capo_partnercentral_benefits.types.status_reason_codes.StatusReasonCodes"
    ]
    """<p>The list of standardized codes representing the reason for the current status.</p>"""
    created_at: NotRequired["capo_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit application was created.</p>"""
    updated_at: NotRequired["capo_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit application was last updated.</p>"""
    revision: NotRequired["str"]
    """<p>The current revision number of the benefit application.</p>"""
    associated_resources: NotRequired["capo_partnercentral_benefits.types.arns.Arns"]
    """<p>AWS resources that are associated with this benefit application.</p>"""
    partner_contacts: NotRequired[
        "capo_partnercentral_benefits.types.contacts.Contacts"
    ]
    """<p>Contact information for partner representatives responsible for this benefit application.</p>"""
    file_details: NotRequired[
        "capo_partnercentral_benefits.types.file_details.FileDetails"
    ]
    """<p>Supporting documents and files attached to the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBenefitApplicationOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "benefit_id" in value:
        out["BenefitId"] = value["benefit_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "fulfillment_types" in value:
        import capo_partnercentral_benefits.types.fulfillment_types

        out["FulfillmentTypes"] = (
            capo_partnercentral_benefits.types.fulfillment_types.serialize_aws_json_1_0(
                value["fulfillment_types"]
            )
        )
    if "benefit_application_details" in value:
        out["BenefitApplicationDetails"] = value["benefit_application_details"]
    if "programs" in value:
        import capo_partnercentral_benefits.types.programs

        out["Programs"] = (
            capo_partnercentral_benefits.types.programs.serialize_aws_json_1_0(
                value["programs"]
            )
        )
    if "status" in value:
        import capo_partnercentral_benefits.types.benefit_application_status

        out["Status"] = (
            capo_partnercentral_benefits.types.benefit_application_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "stage" in value:
        out["Stage"] = value["stage"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "status_reason_code" in value:
        out["StatusReasonCode"] = value["status_reason_code"]
    if "status_reason_codes" in value:
        import capo_partnercentral_benefits.types.status_reason_codes

        out["StatusReasonCodes"] = (
            capo_partnercentral_benefits.types.status_reason_codes.serialize_aws_json_1_0(
                value["status_reason_codes"]
            )
        )
    if "created_at" in value:
        import capo_partnercentral_benefits.types.timestamp

        out["CreatedAt"] = (
            capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_partnercentral_benefits.types.timestamp

        out["UpdatedAt"] = (
            capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "revision" in value:
        out["Revision"] = value["revision"]
    if "associated_resources" in value:
        import capo_partnercentral_benefits.types.arns

        out["AssociatedResources"] = (
            capo_partnercentral_benefits.types.arns.serialize_aws_json_1_0(
                value["associated_resources"]
            )
        )
    if "partner_contacts" in value:
        import capo_partnercentral_benefits.types.contacts

        out["PartnerContacts"] = (
            capo_partnercentral_benefits.types.contacts.serialize_aws_json_1_0(
                value["partner_contacts"]
            )
        )
    if "file_details" in value:
        import capo_partnercentral_benefits.types.file_details

        out["FileDetails"] = (
            capo_partnercentral_benefits.types.file_details.serialize_aws_json_1_0(
                value["file_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBenefitApplicationOutput:
    out: GetBenefitApplicationOutput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    if data.get("BenefitId") is not None:
        out["benefit_id"] = data["BenefitId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FulfillmentTypes") is not None:
        import capo_partnercentral_benefits.types.fulfillment_types

        out["fulfillment_types"] = (
            capo_partnercentral_benefits.types.fulfillment_types.deserialize_aws_json_1_0(
                data["FulfillmentTypes"]
            )
        )
    if data.get("BenefitApplicationDetails") is not None:
        out["benefit_application_details"] = data["BenefitApplicationDetails"]
    if data.get("Programs") is not None:
        import capo_partnercentral_benefits.types.programs

        out["programs"] = (
            capo_partnercentral_benefits.types.programs.deserialize_aws_json_1_0(
                data["Programs"]
            )
        )
    if data.get("Status") is not None:
        import capo_partnercentral_benefits.types.benefit_application_status

        out["status"] = (
            capo_partnercentral_benefits.types.benefit_application_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("Stage") is not None:
        out["stage"] = data["Stage"]
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("StatusReasonCode") is not None:
        out["status_reason_code"] = data["StatusReasonCode"]
    if data.get("StatusReasonCodes") is not None:
        import capo_partnercentral_benefits.types.status_reason_codes

        out["status_reason_codes"] = (
            capo_partnercentral_benefits.types.status_reason_codes.deserialize_aws_json_1_0(
                data["StatusReasonCodes"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_benefits.types.timestamp

        out["created_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_benefits.types.timestamp

        out["updated_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    if data.get("AssociatedResources") is not None:
        import capo_partnercentral_benefits.types.arns

        out["associated_resources"] = (
            capo_partnercentral_benefits.types.arns.deserialize_aws_json_1_0(
                data["AssociatedResources"]
            )
        )
    if data.get("PartnerContacts") is not None:
        import capo_partnercentral_benefits.types.contacts

        out["partner_contacts"] = (
            capo_partnercentral_benefits.types.contacts.deserialize_aws_json_1_0(
                data["PartnerContacts"]
            )
        )
    if data.get("FileDetails") is not None:
        import capo_partnercentral_benefits.types.file_details

        out["file_details"] = (
            capo_partnercentral_benefits.types.file_details.deserialize_aws_json_1_0(
                data["FileDetails"]
            )
        )
    return out


def redact_sensitive(value: GetBenefitApplicationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "partner_contacts" in value:
        import capo_partnercentral_benefits.types.contacts

        out["partner_contacts"] = (
            capo_partnercentral_benefits.types.contacts.redact_sensitive(
                value["partner_contacts"]
            )
        )
    return out
