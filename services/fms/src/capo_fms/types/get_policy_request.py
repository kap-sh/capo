"""Generated from Smithy shape ``com.amazonaws.fms#GetPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fms.types.policy_id


class GetPolicyRequest(TypedDict, closed=True):
    policy_id: "capo_fms.types.policy_id.PolicyId"
    """<p>The ID of the Firewall Manager policy that you want the details for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPolicyRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPolicyRequest:
    out: GetPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        out["policy_id"] = ""
    return out
