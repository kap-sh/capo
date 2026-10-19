"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetScheduledQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.scheduled_query_identifier


class GetScheduledQueryRequest(TypedDict, closed=True):
    identifier: (
        "capo_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier"
    )
    """<p>The ARN or name of the scheduled query to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScheduledQueryRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScheduledQueryRequest:
    out: GetScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
