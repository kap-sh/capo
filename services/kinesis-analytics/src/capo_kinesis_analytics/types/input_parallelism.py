"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputParallelism``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.input_parallelism_count


class InputParallelism(TypedDict, closed=True):
    count: NotRequired[
        "capo_kinesis_analytics.types.input_parallelism_count.InputParallelismCount"
    ]
    """<p>Number of in-application streams to create. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html">Limits</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputParallelism) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputParallelism:
    out: InputParallelism = {}  # type: ignore[typeddict-item]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    return out
