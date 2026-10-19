"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateEngagementInvitationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_invitation_arn
    import capo_partnercentral_selling.types.engagement_invitation_identifier


class CreateEngagementInvitationResponse(TypedDict, closed=True):
    id: "capo_partnercentral_selling.types.engagement_invitation_identifier.EngagementInvitationIdentifier"
    """<p> Unique identifier assigned to the newly created engagement invitation. </p>"""
    arn: "capo_partnercentral_selling.types.engagement_invitation_arn.EngagementInvitationArn"
    """<p> The Amazon Resource Name (ARN) that uniquely identifies the engagement invitation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEngagementInvitationResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEngagementInvitationResponse:
    out: CreateEngagementInvitationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
