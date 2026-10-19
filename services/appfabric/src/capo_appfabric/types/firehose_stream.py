"""Generated from Smithy shape ``com.amazonaws.appfabric#FirehoseStream``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.string64


class FirehoseStream(TypedDict, closed=True):
    stream_name: "capo_appfabric.types.string64.String64"
    """<p>The name of the Amazon Kinesis Data Firehose delivery stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseStream) -> dict:
    out: dict = {}
    out["streamName"] = value["stream_name"]
    return out


def deserialize_json(data: dict) -> FirehoseStream:
    out: FirehoseStream = {}  # type: ignore[typeddict-item]
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    else:
        out["stream_name"] = ""
    return out
