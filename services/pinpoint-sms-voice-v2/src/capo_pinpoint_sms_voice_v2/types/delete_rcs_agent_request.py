"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteRcsAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn


class DeleteRcsAgentRequest(TypedDict, closed=True):
    rcs_agent_id: "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn"
    """<p>The unique identifier of the RCS agent to delete. You can use either the RcsAgentId or RcsAgentArn.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRcsAgentRequest) -> dict:
    out: dict = {}
    out["RcsAgentId"] = value["rcs_agent_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRcsAgentRequest:
    out: DeleteRcsAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("RcsAgentId") is not None:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        out["rcs_agent_id"] = ""
    return out
