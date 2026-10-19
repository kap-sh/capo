"""Generated from Smithy shape ``com.amazonaws.ssmincidents#PutResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.policy


class PutResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response plan to add the resource policy to.</p>"""
    policy: "capo_ssm_incidents.types.policy.Policy"
    """<p>Details of the resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyInput:
    out: PutResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
