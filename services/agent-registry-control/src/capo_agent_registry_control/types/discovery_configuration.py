"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#DiscoveryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.authorizer_configuration
    import capo_agent_registry_control.types.registry_authorizer_type


class DiscoveryConfiguration(TypedDict, closed=True):
    authorizer_configuration: NotRequired[
        "capo_agent_registry_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the registry. Required when authorizerType is CUSTOM_JWT.</p>"""
    authorizer_type: NotRequired[
        "capo_agent_registry_control.types.registry_authorizer_type.RegistryAuthorizerType"
    ]
    """<p>The type of authorizer that controls how consumers access the registry's search and MCP invoke operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryConfiguration) -> dict:
    out: dict = {}
    if "authorizer_configuration" in value:
        import capo_agent_registry_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_agent_registry_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "authorizer_type" in value:
        import capo_agent_registry_control.types.registry_authorizer_type

        out["authorizerType"] = (
            capo_agent_registry_control.types.registry_authorizer_type.serialize_json(
                value["authorizer_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DiscoveryConfiguration:
    out: DiscoveryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("authorizerConfiguration") is not None:
        import capo_agent_registry_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_agent_registry_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("authorizerType") is not None:
        import capo_agent_registry_control.types.registry_authorizer_type

        out["authorizer_type"] = (
            capo_agent_registry_control.types.registry_authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    return out
