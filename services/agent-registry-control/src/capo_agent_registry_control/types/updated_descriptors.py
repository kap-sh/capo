"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedDescriptors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_descriptors_fields


class UpdatedDescriptors(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.updated_descriptors_fields.UpdatedDescriptorsFields"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDescriptors) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_agent_registry_control.types.updated_descriptors_fields

        out["optionalValue"] = (
            capo_agent_registry_control.types.updated_descriptors_fields.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedDescriptors:
    out: UpdatedDescriptors = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_agent_registry_control.types.updated_descriptors_fields

        out["optional_value"] = (
            capo_agent_registry_control.types.updated_descriptors_fields.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
