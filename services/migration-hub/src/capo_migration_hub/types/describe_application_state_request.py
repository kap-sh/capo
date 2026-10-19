"""Generated from Smithy shape ``com.amazonaws.migrationhub#DescribeApplicationStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.application_id


class DescribeApplicationStateRequest(TypedDict, closed=True):
    application_id: "capo_migration_hub.types.application_id.ApplicationId"
    """<p>The configurationId in Application Discovery Service that uniquely identifies the grouped application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationStateRequest) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationStateRequest:
    out: DescribeApplicationStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    else:
        out["application_id"] = ""
    return out
