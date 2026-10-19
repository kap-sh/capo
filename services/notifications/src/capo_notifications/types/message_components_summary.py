"""Generated from Smithy shape ``com.amazonaws.notifications#MessageComponentsSummary``."""

from typing_extensions import TypedDict


class MessageComponentsSummary(TypedDict, closed=True):
    headline: "str"
    """<p>A sentence long summary. For example, titles or an email subject line.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageComponentsSummary) -> dict:
    out: dict = {}
    out["headline"] = value["headline"]
    return out


def deserialize_json(data: dict) -> MessageComponentsSummary:
    out: MessageComponentsSummary = {}  # type: ignore[typeddict-item]
    if data.get("headline") is not None:
        out["headline"] = data["headline"]
    else:
        out["headline"] = ""
    return out
