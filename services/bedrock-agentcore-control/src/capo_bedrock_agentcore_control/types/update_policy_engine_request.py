"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePolicyEngineRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.resource_id
    import capo_bedrock_agentcore_control.types.updated_description


class UpdatePolicyEngineRequest(TypedDict, closed=True):
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy engine to be updated.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
    ]
    """<p>The new description for the policy engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyEngineRequest) -> dict:
    out: dict = {}
    if "description" in value:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.serialize_json(
                value["description"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePolicyEngineRequest:
    out: UpdatePolicyEngineRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.deserialize_json(
                data["description"]
            )
        )
    return out


def redact_sensitive(value: UpdatePolicyEngineRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.redact_sensitive(
                value["description"]
            )
        )
    return out
