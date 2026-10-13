"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateRegistryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.registry_identifier
    import capo_bedrock_agentcore_control.types.registry_name
    import capo_bedrock_agentcore_control.types.updated_approval_configuration
    import capo_bedrock_agentcore_control.types.updated_authorizer_configuration
    import capo_bedrock_agentcore_control.types.updated_description


class UpdateRegistryRequest(TypedDict, closed=True):
    registry_id: (
        "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry to update. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>"""
    name: NotRequired["capo_bedrock_agentcore_control.types.registry_name.RegistryName"]
    """<p>The updated name of the registry.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
    ]
    """<p>The updated description of the registry. To clear the description, include the <code>UpdatedDescription</code> wrapper with <code>optionalValue</code> not specified.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"
    ]
    """<p>The updated authorizer configuration for the registry. Changing the authorizer configuration can break existing consumers of the registry who are using the authorization type prior to the update.</p>"""
    approval_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_approval_configuration.UpdatedApprovalConfiguration"
    ]
    """<p>The updated approval configuration for registry records. The updated configuration only affects new records that move to <code>PENDING_APPROVAL</code> status after the change. Existing records already in <code>PENDING_APPROVAL</code> status are not affected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.serialize_json(
                value["description"]
            )
        )
    if "authorizer_configuration" in value:
        import capo_bedrock_agentcore_control.types.updated_authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.updated_authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "approval_configuration" in value:
        import capo_bedrock_agentcore_control.types.updated_approval_configuration

        out["approvalConfiguration"] = (
            capo_bedrock_agentcore_control.types.updated_approval_configuration.serialize_json(
                value["approval_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRegistryRequest:
    out: UpdateRegistryRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.deserialize_json(
                data["description"]
            )
        )
    if data.get("authorizerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.updated_authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.updated_authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("approvalConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.updated_approval_configuration

        out["approval_configuration"] = (
            capo_bedrock_agentcore_control.types.updated_approval_configuration.deserialize_json(
                data["approvalConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateRegistryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.redact_sensitive(
                value["description"]
            )
        )
    return out
