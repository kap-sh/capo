"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedAgUiDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_ag_ui_descriptor_fields


class UpdatedAgUiDescriptor(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.updated_ag_ui_descriptor_fields.UpdatedAgUiDescriptorFields"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAgUiDescriptor) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_agent_registry_control.types.updated_ag_ui_descriptor_fields

        out["optionalValue"] = (
            capo_agent_registry_control.types.updated_ag_ui_descriptor_fields.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAgUiDescriptor:
    out: UpdatedAgUiDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_agent_registry_control.types.updated_ag_ui_descriptor_fields

        out["optional_value"] = (
            capo_agent_registry_control.types.updated_ag_ui_descriptor_fields.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
