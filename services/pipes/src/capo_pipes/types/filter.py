"""Generated from Smithy shape ``com.amazonaws.pipes#Filter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.event_pattern


class Filter(TypedDict, closed=True):
    pattern: NotRequired["capo_pipes.types.event_pattern.EventPattern"]
    """<p>The event pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    return out


def redact_sensitive(value: Filter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pattern" in value:
        out["pattern"] = "*** Sensitive Data Redacted ***"
    return out
