"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedAutoDetectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.auto_detection_configuration


class UpdatedAutoDetectionConfiguration(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.auto_detection_configuration.AutoDetectionConfiguration"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAutoDetectionConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_agent_registry_control.types.auto_detection_configuration

        out["optionalValue"] = (
            capo_agent_registry_control.types.auto_detection_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAutoDetectionConfiguration:
    out: UpdatedAutoDetectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_agent_registry_control.types.auto_detection_configuration

        out["optional_value"] = (
            capo_agent_registry_control.types.auto_detection_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
