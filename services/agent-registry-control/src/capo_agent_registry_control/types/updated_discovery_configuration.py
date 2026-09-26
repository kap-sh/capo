"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedDiscoveryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_authorizer_configuration


class UpdatedDiscoveryConfiguration(TypedDict, closed=True):
    authorizer_configuration: NotRequired[
        "capo_agent_registry_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"
    ]
    """<p>Authorization configuration for the registry, with PATCH semantics</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDiscoveryConfiguration) -> dict:
    out: dict = {}
    if "authorizer_configuration" in value:
        import capo_agent_registry_control.types.updated_authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_agent_registry_control.types.updated_authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedDiscoveryConfiguration:
    out: UpdatedDiscoveryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("authorizerConfiguration") is not None:
        import capo_agent_registry_control.types.updated_authorizer_configuration

        out["authorizer_configuration"] = (
            capo_agent_registry_control.types.updated_authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    return out
