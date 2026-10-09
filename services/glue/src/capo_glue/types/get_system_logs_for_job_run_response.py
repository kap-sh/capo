"""Generated from Smithy shape ``com.amazonaws.glue#GetSystemLogsForJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.url


class GetSystemLogsForJobRunResponse(TypedDict, closed=True):
    system_logs_url: NotRequired["capo_glue.types.url.Url"]
    """<p>The URL to download the system logs for the job run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemLogsForJobRunResponse) -> dict:
    out: dict = {}
    if "system_logs_url" in value:
        out["SystemLogsUrl"] = value["system_logs_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemLogsForJobRunResponse:
    out: GetSystemLogsForJobRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("SystemLogsUrl") is not None:
        out["system_logs_url"] = data["SystemLogsUrl"]
    return out
