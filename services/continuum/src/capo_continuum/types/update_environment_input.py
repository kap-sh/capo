"""Generated from Smithy shape ``com.amazonaws.continuum#UpdateEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.environment_name
    import capo_continuum.types.update_environment_configuration


class UpdateEnvironmentInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier of the environment to update."""
    name: NotRequired["capo_continuum.types.environment_name.EnvironmentName"]
    """The new customer-visible name."""
    configuration: NotRequired[
        "capo_continuum.types.update_environment_configuration.UpdateEnvironmentConfiguration"
    ]
    """Type-specific configuration changes. Omission preserves the configuration."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "configuration" in value:
        import capo_continuum.types.update_environment_configuration

        out["configuration"] = (
            capo_continuum.types.update_environment_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentInput:
    out: UpdateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("configuration") is not None:
        import capo_continuum.types.update_environment_configuration

        out["configuration"] = (
            capo_continuum.types.update_environment_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
