"""Generated from Smithy shape ``com.amazonaws.kinesis#S3DestinationUpdateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.data_freshness_in_seconds


class S3DestinationUpdateInput(TypedDict, closed=True):
    data_freshness_in_seconds: (
        "capo_kinesis.types.data_freshness_in_seconds.DataFreshnessInSeconds"
    )
    """<p>The maximum age, in seconds, of undelivered data before the channel delivers it to the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DestinationUpdateInput) -> dict:
    out: dict = {}
    out["DataFreshnessInSeconds"] = value["data_freshness_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DestinationUpdateInput:
    out: S3DestinationUpdateInput = {}  # type: ignore[typeddict-item]
    if data.get("DataFreshnessInSeconds") is not None:
        out["data_freshness_in_seconds"] = data["DataFreshnessInSeconds"]
    else:
        out["data_freshness_in_seconds"] = 0
    return out
