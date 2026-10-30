"""Generated from Smithy shape ``com.amazonaws.continuum#UpdateEnvironmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.update_code_configuration


class UpdateEnvironmentConfiguration(TypedDict, closed=True):
    code_configuration: NotRequired[
        "capo_continuum.types.update_code_configuration.UpdateCodeConfiguration"
    ]
    """Changes to a code-scanning environment."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentConfiguration) -> dict:
    out: dict = {}
    if "code_configuration" in value:
        import capo_continuum.types.update_code_configuration

        out["codeConfiguration"] = (
            capo_continuum.types.update_code_configuration.serialize_json(
                value["code_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentConfiguration:
    out: UpdateEnvironmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("codeConfiguration") is not None:
        import capo_continuum.types.update_code_configuration

        out["code_configuration"] = (
            capo_continuum.types.update_code_configuration.deserialize_json(
                data["codeConfiguration"]
            )
        )
    return out
