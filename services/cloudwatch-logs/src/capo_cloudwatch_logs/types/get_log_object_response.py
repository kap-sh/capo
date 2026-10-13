"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogObjectResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.get_log_object_response_stream


class GetLogObjectResponse(TypedDict, closed=True):
    field_stream: NotRequired[
        "capo_cloudwatch_logs.types.get_log_object_response_stream.GetLogObjectResponseStream"
    ]
    """<p>A stream of structured log data returned by the GetLogObject operation. This stream contains log events with their associated metadata and extracted fields.</p>"""


def redact_sensitive(value: GetLogObjectResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_stream" in value:
        out["field_stream"] = "*** Streaming Data Redacted ***"
    return out
