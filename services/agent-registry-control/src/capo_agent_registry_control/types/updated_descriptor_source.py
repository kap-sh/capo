"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedDescriptorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.descriptor_source


class UpdatedDescriptorSource(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.descriptor_source.DescriptorSource"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDescriptorSource) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_agent_registry_control.types.descriptor_source

        out["optionalValue"] = (
            capo_agent_registry_control.types.descriptor_source.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedDescriptorSource:
    out: UpdatedDescriptorSource = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_agent_registry_control.types.descriptor_source

        out["optional_value"] = (
            capo_agent_registry_control.types.descriptor_source.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
