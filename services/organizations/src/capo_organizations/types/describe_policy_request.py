"""Generated from Smithy shape ``com.amazonaws.organizations#DescribePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.policy_id


class DescribePolicyRequest(TypedDict, closed=True):
    policy_id: "capo_organizations.types.policy_id.PolicyId"
    """<p>ID for the policy that you want details about. You can get the ID from the <a>ListPolicies</a> or <a>ListPoliciesForTarget</a> operations.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a policy ID string requires "p-" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePolicyRequest:
    out: DescribePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("DescribePolicyRequest.policy_id required")
    return out
