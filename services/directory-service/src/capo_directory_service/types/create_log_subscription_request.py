"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateLogSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.log_group_name


class CreateLogSubscriptionRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the directory to which you want to subscribe and receive real-time logs to your specified CloudWatch log group.</p>"""
    log_group_name: "capo_directory_service.types.log_group_name.LogGroupName"
    """<p>The name of the CloudWatch log group where the real-time domain controller logs are forwarded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLogSubscriptionRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["LogGroupName"] = value["log_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLogSubscriptionRequest:
    out: CreateLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("LogGroupName") is not None:
        out["log_group_name"] = data["LogGroupName"]
    else:
        out["log_group_name"] = ""
    return out
