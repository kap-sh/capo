"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateCapacityProviderInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_name
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.compute_configuration
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.permissions_configuration
    import capo_bedrock_agentcore_control.types.tags_map


class CreateCapacityProviderInput(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.capacity_provider_name.CapacityProviderName"
    """<p>The name of the capacity provider. The name must be unique within your account.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>An optional description of the capacity provider. If you don't specify a description, the service creates the capacity provider without one.</p>"""
    permissions_configuration: "capo_bedrock_agentcore_control.types.permissions_configuration.PermissionsConfiguration"
    """<p>The permissions configuration for the capacity provider. This specifies the IAM role that AgentCore uses to manage the Amazon EC2 instances on your behalf.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to associate with the capacity provider. If you don't specify tags, the capacity provider is created with no tags.</p>"""
    compute_configuration: "capo_bedrock_agentcore_control.types.compute_configuration.ComputeConfiguration"
    """<p>The compute configuration for the capacity provider. This defines the Amazon EC2 compute resources used to launch instances: the operating system, allowed instance types, networking, and storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCapacityProviderInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.permissions_configuration

    out["permissionsConfiguration"] = (
        capo_bedrock_agentcore_control.types.permissions_configuration.serialize_json(
            value["permissions_configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    import capo_bedrock_agentcore_control.types.compute_configuration

    out["computeConfiguration"] = (
        capo_bedrock_agentcore_control.types.compute_configuration.serialize_json(
            value["compute_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateCapacityProviderInput:
    out: CreateCapacityProviderInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCapacityProviderInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("permissionsConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.permissions_configuration

        out["permissions_configuration"] = (
            capo_bedrock_agentcore_control.types.permissions_configuration.deserialize_json(
                data["permissionsConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCapacityProviderInput.permissions_configuration required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    if data.get("computeConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.compute_configuration

        out["compute_configuration"] = (
            capo_bedrock_agentcore_control.types.compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCapacityProviderInput.compute_configuration required"
        )
    return out
