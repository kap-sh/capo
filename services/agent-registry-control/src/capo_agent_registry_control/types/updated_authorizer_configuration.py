"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedAuthorizerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.authorizer_configuration


class UpdatedAuthorizerConfiguration(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The new authorizer configuration to set. Omit to leave the existing configuration unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAuthorizerConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_agent_registry_control.types.authorizer_configuration

        out["optionalValue"] = (
            capo_agent_registry_control.types.authorizer_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAuthorizerConfiguration:
    out: UpdatedAuthorizerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_agent_registry_control.types.authorizer_configuration

        out["optional_value"] = (
            capo_agent_registry_control.types.authorizer_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
