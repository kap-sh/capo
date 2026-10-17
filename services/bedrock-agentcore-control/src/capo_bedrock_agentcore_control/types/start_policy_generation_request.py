"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StartPolicyGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.content
    import capo_bedrock_agentcore_control.types.policy_generation_name
    import capo_bedrock_agentcore_control.types.resource
    import capo_bedrock_agentcore_control.types.resource_id


class StartPolicyGenerationRequest(TypedDict, closed=True):
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine that provides the context for policy generation. This engine's schema and tool context are used to ensure generated policies are valid and applicable.</p>"""
    resource: "capo_bedrock_agentcore_control.types.resource.Resource"
    """<p>The resource information that provides context for policy generation. This helps the AI understand the target resources and generate appropriate access control rules.</p>"""
    content: "capo_bedrock_agentcore_control.types.content.Content"
    """<p>The natural language description of the desired policy behavior. This content is processed by AI to generate corresponding Dogwood policy statements that match the described intent.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_generation_name.PolicyGenerationName"
    """<p>A customer-assigned name for the policy generation request. This helps track and identify generation operations, especially when running multiple generations simultaneously.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without starting a duplicate generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPolicyGenerationRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.resource

    out["resource"] = capo_bedrock_agentcore_control.types.resource.serialize_json(
        value["resource"]
    )
    import capo_bedrock_agentcore_control.types.content

    out["content"] = capo_bedrock_agentcore_control.types.content.serialize_json(
        value["content"]
    )
    out["name"] = value["name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartPolicyGenerationRequest:
    out: StartPolicyGenerationRequest = {}  # type: ignore[typeddict-item]
    if data.get("resource") is not None:
        import capo_bedrock_agentcore_control.types.resource

        out["resource"] = (
            capo_bedrock_agentcore_control.types.resource.deserialize_json(
                data["resource"]
            )
        )
    else:
        raise DeserializationError("StartPolicyGenerationRequest.resource required")
    if data.get("content") is not None:
        import capo_bedrock_agentcore_control.types.content

        out["content"] = capo_bedrock_agentcore_control.types.content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("StartPolicyGenerationRequest.content required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartPolicyGenerationRequest.name required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
