"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotDefaultValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_default_value_string


class SlotDefaultValue(TypedDict, closed=True):
    default_value: (
        "capo_lex_models_v2.types.slot_default_value_string.SlotDefaultValueString"
    )
    """<p>The default value to use when a user doesn't provide a value for a slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotDefaultValue) -> dict:
    out: dict = {}
    out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> SlotDefaultValue:
    out: SlotDefaultValue = {}  # type: ignore[typeddict-item]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    else:
        out["default_value"] = ""
    return out
