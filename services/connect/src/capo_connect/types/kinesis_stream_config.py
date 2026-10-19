"""Generated from Smithy shape ``com.amazonaws.connect#KinesisStreamConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn


class KinesisStreamConfig(TypedDict, closed=True):
    stream_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the data stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisStreamConfig) -> dict:
    out: dict = {}
    out["StreamArn"] = value["stream_arn"]
    return out


def deserialize_json(data: dict) -> KinesisStreamConfig:
    out: KinesisStreamConfig = {}  # type: ignore[typeddict-item]
    if data.get("StreamArn") is not None:
        out["stream_arn"] = data["StreamArn"]
    else:
        out["stream_arn"] = ""
    return out
