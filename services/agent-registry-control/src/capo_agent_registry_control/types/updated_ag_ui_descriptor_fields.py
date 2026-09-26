"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedAgUiDescriptorFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_descriptor_source


class UpdatedAgUiDescriptorFields(TypedDict, closed=True):
    source: NotRequired[
        "capo_agent_registry_control.types.updated_descriptor_source.UpdatedDescriptorSource"
    ]
    """<p>The patch for the descriptor's source field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAgUiDescriptorFields) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_agent_registry_control.types.updated_descriptor_source

        out["source"] = (
            capo_agent_registry_control.types.updated_descriptor_source.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAgUiDescriptorFields:
    out: UpdatedAgUiDescriptorFields = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_agent_registry_control.types.updated_descriptor_source

        out["source"] = (
            capo_agent_registry_control.types.updated_descriptor_source.deserialize_json(
                data["source"]
            )
        )
    return out
