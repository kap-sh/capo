"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.resource_policy_body


class PutResourcePolicyResponse(TypedDict, closed=True):
    policy: (
        "capo_bedrock_agentcore_control.types.resource_policy_body.ResourcePolicyBody"
    )
    """<p>The resource policy that was created or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
