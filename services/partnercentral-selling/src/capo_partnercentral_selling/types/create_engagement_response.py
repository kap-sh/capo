"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateEngagementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_arn
    import capo_partnercentral_selling.types.engagement_identifier


class CreateEngagementResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>Unique identifier assigned to the newly created engagement.</p>"""
    arn: NotRequired["capo_partnercentral_selling.types.engagement_arn.EngagementArn"]
    """<p>The Amazon Resource Name (ARN) that identifies the engagement.</p>"""
    modified_at: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp indicating when the engagement was last modified, in ISO 8601 format (UTC). For newly created engagements, this value matches the creation timestamp. Example: "2023-05-01T20:37:46Z".</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEngagementResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "modified_at" in value:
        import capo_partnercentral_selling.types.date_time

        out["ModifiedAt"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEngagementResponse:
    out: CreateEngagementResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ModifiedAt") is not None:
        import capo_partnercentral_selling.types.date_time

        out["modified_at"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    return out
