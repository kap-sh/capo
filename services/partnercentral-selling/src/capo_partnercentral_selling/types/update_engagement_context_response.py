"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UpdateEngagementContextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_arn
    import capo_partnercentral_selling.types.engagement_context_identifier
    import capo_partnercentral_selling.types.engagement_identifier


class UpdateEngagementContextResponse(TypedDict, closed=True):
    engagement_id: (
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    )
    """<p>The unique identifier of the engagement that was updated.</p>"""
    engagement_arn: "capo_partnercentral_selling.types.engagement_arn.EngagementArn"
    """<p>The Amazon Resource Name (ARN) of the updated engagement.</p>"""
    engagement_last_modified_at: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p>The timestamp when the engagement context was last modified.</p>"""
    context_id: "capo_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier"
    """<p>The unique identifier of the engagement context that was updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEngagementContextResponse) -> dict:
    out: dict = {}
    out["EngagementId"] = value["engagement_id"]
    out["EngagementArn"] = value["engagement_arn"]
    import capo_partnercentral_selling.types.date_time

    out["EngagementLastModifiedAt"] = (
        capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["engagement_last_modified_at"]
        )
    )
    out["ContextId"] = value["context_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEngagementContextResponse:
    out: UpdateEngagementContextResponse = {}  # type: ignore[typeddict-item]
    if data.get("EngagementId") is not None:
        out["engagement_id"] = data["EngagementId"]
    else:
        out["engagement_id"] = ""
    if data.get("EngagementArn") is not None:
        out["engagement_arn"] = data["EngagementArn"]
    else:
        out["engagement_arn"] = ""
    if data.get("EngagementLastModifiedAt") is not None:
        import capo_partnercentral_selling.types.date_time

        out["engagement_last_modified_at"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["EngagementLastModifiedAt"]
            )
        )
    else:
        import datetime

        out["engagement_last_modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ContextId") is not None:
        out["context_id"] = data["ContextId"]
    else:
        out["context_id"] = ""
    return out
