"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedDescriptorData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.descriptor_data


class UpdatedDescriptorData(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.descriptor_data.DescriptorData"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDescriptorData) -> dict:
    out: dict = {}
    if "optional_value" in value:
        out["optionalValue"] = value["optional_value"]
    return out


def deserialize_json(data: dict) -> UpdatedDescriptorData:
    out: UpdatedDescriptorData = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        out["optional_value"] = data["optionalValue"]
    return out


def redact_sensitive(value: UpdatedDescriptorData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "optional_value" in value:
        out["optional_value"] = "*** Sensitive Data Redacted ***"
    return out
