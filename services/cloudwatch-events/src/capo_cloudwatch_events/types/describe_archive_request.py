"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeArchiveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.archive_name


class DescribeArchiveRequest(TypedDict, closed=True):
    archive_name: "capo_cloudwatch_events.types.archive_name.ArchiveName"
    """<p>The name of the archive to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeArchiveRequest) -> dict:
    out: dict = {}
    out["ArchiveName"] = value["archive_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeArchiveRequest:
    out: DescribeArchiveRequest = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveName") is not None:
        out["archive_name"] = data["ArchiveName"]
    else:
        out["archive_name"] = ""
    return out
