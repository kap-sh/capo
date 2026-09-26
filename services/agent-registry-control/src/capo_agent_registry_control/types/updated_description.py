"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.description


class UpdatedDescription(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.description.Description"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDescription) -> dict:
    out: dict = {}
    if "optional_value" in value:
        out["optionalValue"] = value["optional_value"]
    return out


def deserialize_json(data: dict) -> UpdatedDescription:
    out: UpdatedDescription = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        out["optional_value"] = data["optionalValue"]
    return out
