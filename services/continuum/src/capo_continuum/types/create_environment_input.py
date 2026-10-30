"""Generated from Smithy shape ``com.amazonaws.continuum#CreateEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.create_environment_configuration
    import capo_continuum.types.environment_name


class CreateEnvironmentInput(TypedDict, closed=True):
    name: "capo_continuum.types.environment_name.EnvironmentName"
    """The customer-visible name of the environment."""
    configuration: NotRequired[
        "capo_continuum.types.create_environment_configuration.CreateEnvironmentConfiguration"
    ]
    """Type-specific configuration. Omission creates a code environment with the default operating policy and no sources."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "configuration" in value:
        import capo_continuum.types.create_environment_configuration

        out["configuration"] = (
            capo_continuum.types.create_environment_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateEnvironmentInput:
    out: CreateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("configuration") is not None:
        import capo_continuum.types.create_environment_configuration

        out["configuration"] = (
            capo_continuum.types.create_environment_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
