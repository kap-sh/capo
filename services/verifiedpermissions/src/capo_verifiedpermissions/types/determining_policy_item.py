"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeterminingPolicyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_id


class DeterminingPolicyItem(TypedDict, closed=True):
    policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId"
    """<p>The Id of a policy that determined to an authorization decision.</p> <p>Example: <code>"policyId":"SPEXAMPLEabcdefg111111"</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeterminingPolicyItem) -> dict:
    out: dict = {}
    out["policyId"] = value["policy_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeterminingPolicyItem:
    out: DeterminingPolicyItem = {}  # type: ignore[typeddict-item]
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("DeterminingPolicyItem.policy_id required")
    return out
