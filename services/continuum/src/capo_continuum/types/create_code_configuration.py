"""Generated from Smithy shape ``com.amazonaws.continuum#CreateCodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_configuration
    import capo_continuum.types.environment_source_configuration


class CreateCodeConfiguration(TypedDict, closed=True):
    source_configuration: NotRequired[
        "capo_continuum.types.environment_source_configuration.EnvironmentSourceConfiguration"
    ]
    """Source configuration for the environment."""
    environment_configuration: NotRequired[
        "capo_continuum.types.environment_configuration.EnvironmentConfiguration"
    ]
    """Environment-level operating policy."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeConfiguration) -> dict:
    out: dict = {}
    if "source_configuration" in value:
        import capo_continuum.types.environment_source_configuration

        out["sourceConfiguration"] = (
            capo_continuum.types.environment_source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "environment_configuration" in value:
        import capo_continuum.types.environment_configuration

        out["environmentConfiguration"] = (
            capo_continuum.types.environment_configuration.serialize_json(
                value["environment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCodeConfiguration:
    out: CreateCodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceConfiguration") is not None:
        import capo_continuum.types.environment_source_configuration

        out["source_configuration"] = (
            capo_continuum.types.environment_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if data.get("environmentConfiguration") is not None:
        import capo_continuum.types.environment_configuration

        out["environment_configuration"] = (
            capo_continuum.types.environment_configuration.deserialize_json(
                data["environmentConfiguration"]
            )
        )
    return out
