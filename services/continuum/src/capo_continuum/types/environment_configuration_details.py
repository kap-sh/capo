"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.code_configuration_details


class EnvironmentConfigurationDetails(TypedDict, closed=True):
    code_configuration: NotRequired[
        "capo_continuum.types.code_configuration_details.CodeConfigurationDetails"
    ]
    """Configuration and scan state for a code-scanning environment."""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationDetails) -> dict:
    out: dict = {}
    if "code_configuration" in value:
        import capo_continuum.types.code_configuration_details

        out["codeConfiguration"] = (
            capo_continuum.types.code_configuration_details.serialize_json(
                value["code_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentConfigurationDetails:
    out: EnvironmentConfigurationDetails = {}  # type: ignore[typeddict-item]
    if data.get("codeConfiguration") is not None:
        import capo_continuum.types.code_configuration_details

        out["code_configuration"] = (
            capo_continuum.types.code_configuration_details.deserialize_json(
                data["codeConfiguration"]
            )
        )
    return out
