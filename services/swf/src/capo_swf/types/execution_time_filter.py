"""Generated from Smithy shape ``com.amazonaws.swf#ExecutionTimeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.timestamp


class ExecutionTimeFilter(TypedDict, closed=True):
    oldest_date: "capo_swf.types.timestamp.Timestamp"
    """<p>Specifies the oldest start or close date and time to return.</p>"""
    latest_date: NotRequired["capo_swf.types.timestamp.Timestamp"]
    """<p>Specifies the latest start or close date and time to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionTimeFilter) -> dict:
    out: dict = {}
    import capo_swf.types.timestamp

    out["oldestDate"] = capo_swf.types.timestamp.serialize_aws_json_1_0(
        value["oldest_date"]
    )
    if "latest_date" in value:
        import capo_swf.types.timestamp

        out["latestDate"] = capo_swf.types.timestamp.serialize_aws_json_1_0(
            value["latest_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionTimeFilter:
    out: ExecutionTimeFilter = {}  # type: ignore[typeddict-item]
    if data.get("oldestDate") is not None:
        import capo_swf.types.timestamp

        out["oldest_date"] = capo_swf.types.timestamp.deserialize_aws_json_1_0(
            data["oldestDate"]
        )
    else:
        import datetime

        out["oldest_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("latestDate") is not None:
        import capo_swf.types.timestamp

        out["latest_date"] = capo_swf.types.timestamp.deserialize_aws_json_1_0(
            data["latestDate"]
        )
    return out
