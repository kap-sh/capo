"""Generated from Smithy shape ``com.amazonaws.ivschat#FirehoseDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.delivery_stream_name


class FirehoseDestinationConfiguration(TypedDict, closed=True):
    delivery_stream_name: "capo_ivschat.types.delivery_stream_name.DeliveryStreamName"
    """<p>Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseDestinationConfiguration) -> dict:
    out: dict = {}
    out["deliveryStreamName"] = value["delivery_stream_name"]
    return out


def deserialize_json(data: dict) -> FirehoseDestinationConfiguration:
    out: FirehoseDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("deliveryStreamName") is not None:
        out["delivery_stream_name"] = data["deliveryStreamName"]
    else:
        out["delivery_stream_name"] = ""
    return out
