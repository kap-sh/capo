"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ResourcePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.policy
    import capo_ssm_incidents.types.policy_id


class ResourcePolicy(TypedDict, closed=True):
    policy_document: "capo_ssm_incidents.types.policy.Policy"
    """<p>The JSON blob that describes the policy.</p>"""
    policy_id: "capo_ssm_incidents.types.policy_id.PolicyId"
    """<p>The ID of the resource policy.</p>"""
    ram_resource_share_region: "str"
    """<p>The Amazon Web Services Region that policy allows resources to be used in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePolicy) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    out["policyId"] = value["policy_id"]
    out["ramResourceShareRegion"] = value["ram_resource_share_region"]
    return out


def deserialize_json(data: dict) -> ResourcePolicy:
    out: ResourcePolicy = {}  # type: ignore[typeddict-item]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        out["policy_document"] = ""
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        out["policy_id"] = ""
    if data.get("ramResourceShareRegion") is not None:
        out["ram_resource_share_region"] = data["ramResourceShareRegion"]
    else:
        out["ram_resource_share_region"] = ""
    return out
