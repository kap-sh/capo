"""Generated from Smithy shape ``com.amazonaws.appintegrations#EventFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.source


class EventFilter(TypedDict, closed=True):
    source: "capo_appintegrations.types.source.Source"
    """<p>The source of the events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventFilter) -> dict:
    out: dict = {}
    out["Source"] = value["source"]
    return out


def deserialize_json(data: dict) -> EventFilter:
    out: EventFilter = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        out["source"] = ""
    return out
