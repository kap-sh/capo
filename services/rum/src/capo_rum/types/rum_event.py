"""Generated from Smithy shape ``com.amazonaws.rum#RumEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rum.types.json_value


class RumEvent(TypedDict, closed=True):
    id: "str"
    """<p>A unique ID for this event.</p>"""
    timestamp: "datetime.datetime"
    """<p>The exact time that this event occurred.</p>"""
    type: "str"
    """<p>The JSON schema that denotes the type of event this is, such as a page load or a new session.</p>"""
    metadata: NotRequired["capo_rum.types.json_value.JsonValue"]
    """<p>Metadata about this event, which contains a JSON serialization of the identity of the user for this session. The user information comes from information such as the HTTP user-agent request header and document interface.</p>"""
    details: "capo_rum.types.json_value.JsonValue"
    """<p>A string containing details about the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RumEvent) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_rum.types._prelude.timestamp

    out["timestamp"] = capo_rum.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    out["type"] = value["type"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    out["details"] = value["details"]
    return out


def deserialize_json(data: dict) -> RumEvent:
    out: RumEvent = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("timestamp") is not None:
        import capo_rum.types._prelude.timestamp

        out["timestamp"] = capo_rum.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    if data.get("details") is not None:
        out["details"] = data["details"]
    else:
        out["details"] = ""
    return out
