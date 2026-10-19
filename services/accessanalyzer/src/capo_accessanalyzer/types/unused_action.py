"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.timestamp


class UnusedAction(TypedDict, closed=True):
    action: "str"
    """<p>The action for which the unused access finding was generated.</p>"""
    last_accessed: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the action was last accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedAction) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    if "last_accessed" in value:
        import capo_accessanalyzer.types.timestamp

        out["lastAccessed"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["last_accessed"]
        )
    return out


def deserialize_json(data: dict) -> UnusedAction:
    out: UnusedAction = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    if data.get("lastAccessed") is not None:
        import capo_accessanalyzer.types.timestamp

        out["last_accessed"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["lastAccessed"]
        )
    return out
