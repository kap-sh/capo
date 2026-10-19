"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateTrafficPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.traffic_policy_id


class CreateTrafficPolicyResponse(TypedDict, closed=True):
    traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of the traffic policy resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTrafficPolicyResponse) -> dict:
    out: dict = {}
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTrafficPolicyResponse:
    out: CreateTrafficPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrafficPolicyId") is not None:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        out["traffic_policy_id"] = ""
    return out
