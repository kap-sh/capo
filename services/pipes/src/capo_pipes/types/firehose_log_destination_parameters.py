"""Generated from Smithy shape ``com.amazonaws.pipes#FirehoseLogDestinationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.firehose_arn


class FirehoseLogDestinationParameters(TypedDict, closed=True):
    delivery_stream_arn: "capo_pipes.types.firehose_arn.FirehoseArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseLogDestinationParameters) -> dict:
    out: dict = {}
    out["DeliveryStreamArn"] = value["delivery_stream_arn"]
    return out


def deserialize_json(data: dict) -> FirehoseLogDestinationParameters:
    out: FirehoseLogDestinationParameters = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamArn") is not None:
        out["delivery_stream_arn"] = data["DeliveryStreamArn"]
    else:
        out["delivery_stream_arn"] = ""
    return out
