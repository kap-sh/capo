"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#NotificationDestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.destination_uri


class NotificationDestinationConfig(TypedDict, closed=True):
    uri: "capo_kinesis_video.types.destination_uri.DestinationUri"
    """<p>The Uniform Resource Identifier (URI) that identifies where the images will be delivered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationDestinationConfig) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> NotificationDestinationConfig:
    out: NotificationDestinationConfig = {}  # type: ignore[typeddict-item]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    else:
        out["uri"] = ""
    return out
