"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateEngagementContextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_arn
    import capo_partnercentral_selling.types.engagement_context_identifier
    import capo_partnercentral_selling.types.engagement_identifier


class CreateEngagementContextResponse(TypedDict, closed=True):
    engagement_id: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The unique identifier of the engagement to which the context was added. This ID confirms the successful association of the context with the specified engagement.</p>"""
    engagement_arn: NotRequired[
        "capo_partnercentral_selling.types.engagement_arn.EngagementArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the engagement to which the context was added. This globally unique identifier can be used for cross-service references and IAM policies.</p>"""
    engagement_last_modified_at: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>The timestamp indicating when the engagement was last modified as a result of adding the context, in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z".</p>"""
    context_id: NotRequired[
        "capo_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier"
    ]
    """<p>The unique identifier assigned to the newly created engagement context. This ID can be used to reference the specific context within the engagement for future operations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEngagementContextResponse) -> dict:
    out: dict = {}
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "engagement_arn" in value:
        out["EngagementArn"] = value["engagement_arn"]
    if "engagement_last_modified_at" in value:
        import capo_partnercentral_selling.types.date_time

        out["EngagementLastModifiedAt"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["engagement_last_modified_at"]
            )
        )
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEngagementContextResponse:
    out: CreateEngagementContextResponse = {}  # type: ignore[typeddict-item]
    if data.get("EngagementId") is not None:
        out["engagement_id"] = data["EngagementId"]
    if data.get("EngagementArn") is not None:
        out["engagement_arn"] = data["EngagementArn"]
    if data.get("EngagementLastModifiedAt") is not None:
        import capo_partnercentral_selling.types.date_time

        out["engagement_last_modified_at"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["EngagementLastModifiedAt"]
            )
        )
    if data.get("ContextId") is not None:
        out["context_id"] = data["ContextId"]
    return out
