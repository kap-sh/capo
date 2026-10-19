"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.qualified_policy_arn


class PolicyReference(TypedDict, closed=True):
    policy_arn: "capo_mpa.types.qualified_policy_arn.QualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyReference) -> dict:
    out: dict = {}
    out["PolicyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> PolicyReference:
    out: PolicyReference = {}  # type: ignore[typeddict-item]
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    else:
        out["policy_arn"] = ""
    return out
