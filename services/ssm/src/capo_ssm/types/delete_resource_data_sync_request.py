"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteResourceDataSyncRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.resource_data_sync_name
    import capo_ssm.types.resource_data_sync_type


class DeleteResourceDataSyncRequest(TypedDict, closed=True):
    sync_name: "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    """<p>The name of the configuration to delete.</p>"""
    sync_type: NotRequired[
        "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    ]
    """<p>Specify the type of resource data sync to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourceDataSyncRequest) -> dict:
    out: dict = {}
    out["SyncName"] = value["sync_name"]
    if "sync_type" in value:
        out["SyncType"] = value["sync_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourceDataSyncRequest:
    out: DeleteResourceDataSyncRequest = {}  # type: ignore[typeddict-item]
    if data.get("SyncName") is not None:
        out["sync_name"] = data["SyncName"]
    else:
        out["sync_name"] = ""
    if data.get("SyncType") is not None:
        out["sync_type"] = data["SyncType"]
    return out
