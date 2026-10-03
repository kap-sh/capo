"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetEngagementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_arn
    import capo_partnercentral_selling.types.engagement_contexts
    import capo_partnercentral_selling.types.engagement_description
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.engagement_title


class GetEngagementResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The unique resource identifier of the engagement retrieved.</p>"""
    arn: NotRequired["capo_partnercentral_selling.types.engagement_arn.EngagementArn"]
    """<p>The Amazon Resource Name (ARN) of the engagement retrieved.</p>"""
    title: NotRequired[
        "capo_partnercentral_selling.types.engagement_title.EngagementTitle"
    ]
    """<p>The title of the engagement. It provides a brief, descriptive name for the engagement that is meaningful and easily recognizable.</p>"""
    description: NotRequired[
        "capo_partnercentral_selling.types.engagement_description.EngagementDescription"
    ]
    """<p>A more detailed description of the engagement. This provides additional context or information about the engagement's purpose or scope.</p>"""
    created_at: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The date and time when the Engagement was created, presented in ISO 8601 format (UTC). For example: "2023-05-01T20:37:46Z". This timestamp helps track the lifecycle of the Engagement.</p>"""
    created_by: NotRequired["capo_partnercentral_selling.types.aws_account.AwsAccount"]
    """<p>The AWS account ID of the user who originally created the engagement. This field helps in tracking the origin of the engagement.</p>"""
    member_count: NotRequired["int"]
    """<p>Specifies the current count of members participating in the Engagement. This count includes all active members regardless of their roles or permissions within the Engagement.</p>"""
    modified_at: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp indicating when the engagement was last modified, in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z". This helps track the most recent changes to the engagement.</p>"""
    modified_by: NotRequired["capo_partnercentral_selling.types.aws_account.AwsAccount"]
    """<p>The AWS account ID of the user who last modified the engagement. This field helps track who made the most recent changes to the engagement.</p>"""
    contexts: NotRequired[
        "capo_partnercentral_selling.types.engagement_contexts.EngagementContexts"
    ]
    """<p>A list of context objects associated with the engagement. Each context provides additional information related to the Engagement, such as customer projects or documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEngagementResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_partnercentral_selling.types.date_time

        out["CreatedAt"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "member_count" in value:
        out["MemberCount"] = value["member_count"]
    if "modified_at" in value:
        import capo_partnercentral_selling.types.date_time

        out["ModifiedAt"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    if "modified_by" in value:
        out["ModifiedBy"] = value["modified_by"]
    if "contexts" in value:
        import capo_partnercentral_selling.types.engagement_contexts

        out["Contexts"] = (
            capo_partnercentral_selling.types.engagement_contexts.serialize_aws_json_1_0(
                value["contexts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEngagementResponse:
    out: GetEngagementResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_selling.types.date_time

        out["created_at"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("MemberCount") is not None:
        out["member_count"] = data["MemberCount"]
    if data.get("ModifiedAt") is not None:
        import capo_partnercentral_selling.types.date_time

        out["modified_at"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    if data.get("ModifiedBy") is not None:
        out["modified_by"] = data["ModifiedBy"]
    if data.get("Contexts") is not None:
        import capo_partnercentral_selling.types.engagement_contexts

        out["contexts"] = (
            capo_partnercentral_selling.types.engagement_contexts.deserialize_aws_json_1_0(
                data["Contexts"]
            )
        )
    return out
