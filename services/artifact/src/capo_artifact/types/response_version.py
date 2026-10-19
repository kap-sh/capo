"""Generated from Smithy shape ``com.amazonaws.artifact#ResponseVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.long_string_attribute
    import capo_artifact.types.timestamp_attribute


class ResponseVersion(TypedDict, closed=True):
    response_text: "capo_artifact.types.long_string_attribute.LongStringAttribute"
    """<p>The response text for this version.</p>"""
    timestamp: "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    """<p>ISO 8601 timestamp of when this edit was made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseVersion) -> dict:
    out: dict = {}
    out["responseText"] = value["response_text"]
    import capo_artifact.types.timestamp_attribute

    out["timestamp"] = capo_artifact.types.timestamp_attribute.serialize_json(
        value["timestamp"]
    )
    return out


def deserialize_json(data: dict) -> ResponseVersion:
    out: ResponseVersion = {}  # type: ignore[typeddict-item]
    if data.get("responseText") is not None:
        out["response_text"] = data["responseText"]
    else:
        out["response_text"] = ""
    if data.get("timestamp") is not None:
        import capo_artifact.types.timestamp_attribute

        out["timestamp"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
