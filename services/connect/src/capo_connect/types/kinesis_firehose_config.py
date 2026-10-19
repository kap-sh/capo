"""Generated from Smithy shape ``com.amazonaws.connect#KinesisFirehoseConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn


class KinesisFirehoseConfig(TypedDict, closed=True):
    firehose_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the delivery stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisFirehoseConfig) -> dict:
    out: dict = {}
    out["FirehoseArn"] = value["firehose_arn"]
    return out


def deserialize_json(data: dict) -> KinesisFirehoseConfig:
    out: KinesisFirehoseConfig = {}  # type: ignore[typeddict-item]
    if data.get("FirehoseArn") is not None:
        out["firehose_arn"] = data["FirehoseArn"]
    else:
        out["firehose_arn"] = ""
    return out
