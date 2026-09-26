"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedCustomDescriptorFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_descriptor_data


class UpdatedCustomDescriptorFields(TypedDict, closed=True):
    data: NotRequired[
        "capo_agent_registry_control.types.updated_descriptor_data.UpdatedDescriptorData"
    ]
    """<p>The patch for the descriptor's data field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedCustomDescriptorFields) -> dict:
    out: dict = {}
    if "data" in value:
        import capo_agent_registry_control.types.updated_descriptor_data

        out["data"] = (
            capo_agent_registry_control.types.updated_descriptor_data.serialize_json(
                value["data"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedCustomDescriptorFields:
    out: UpdatedCustomDescriptorFields = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        import capo_agent_registry_control.types.updated_descriptor_data

        out["data"] = (
            capo_agent_registry_control.types.updated_descriptor_data.deserialize_json(
                data["data"]
            )
        )
    return out
