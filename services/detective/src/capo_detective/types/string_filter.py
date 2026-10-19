"""Generated from Smithy shape ``com.amazonaws.detective#StringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.value


class StringFilter(TypedDict, closed=True):
    value: "capo_detective.types.value.Value"
    """<p>The string filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringFilter) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> StringFilter:
    out: StringFilter = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
