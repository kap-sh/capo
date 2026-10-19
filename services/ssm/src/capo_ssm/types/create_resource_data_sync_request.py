"""Generated from Smithy shape ``com.amazonaws.ssm#CreateResourceDataSyncRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.resource_data_sync_name
    import capo_ssm.types.resource_data_sync_s3_destination
    import capo_ssm.types.resource_data_sync_source
    import capo_ssm.types.resource_data_sync_type


class CreateResourceDataSyncRequest(TypedDict, closed=True):
    sync_name: "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    """<p>A name for the configuration.</p>"""
    s3_destination: NotRequired[
        "capo_ssm.types.resource_data_sync_s3_destination.ResourceDataSyncS3Destination"
    ]
    """<p>Amazon S3 configuration details for the sync. This parameter is required if the <code>SyncType</code> value is SyncToDestination.</p>"""
    sync_type: NotRequired[
        "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    ]
    """<p>Specify <code>SyncToDestination</code> to create a resource data sync that synchronizes data to an S3 bucket for Inventory. If you specify <code>SyncToDestination</code>, you must provide a value for <code>S3Destination</code>. Specify <code>SyncFromSource</code> to synchronize data from a single account and multiple Regions, or multiple Amazon Web Services accounts and Amazon Web Services Regions, as listed in Organizations for Explorer. If you specify <code>SyncFromSource</code>, you must provide a value for <code>SyncSource</code>. The default value is <code>SyncToDestination</code>.</p>"""
    sync_source: NotRequired[
        "capo_ssm.types.resource_data_sync_source.ResourceDataSyncSource"
    ]
    """<p>Specify information about the data sources to synchronize. This parameter is required if the <code>SyncType</code> value is SyncFromSource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResourceDataSyncRequest) -> dict:
    out: dict = {}
    out["SyncName"] = value["sync_name"]
    if "s3_destination" in value:
        import capo_ssm.types.resource_data_sync_s3_destination

        out["S3Destination"] = (
            capo_ssm.types.resource_data_sync_s3_destination.serialize_aws_json_1_1(
                value["s3_destination"]
            )
        )
    if "sync_type" in value:
        out["SyncType"] = value["sync_type"]
    if "sync_source" in value:
        import capo_ssm.types.resource_data_sync_source

        out["SyncSource"] = (
            capo_ssm.types.resource_data_sync_source.serialize_aws_json_1_1(
                value["sync_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResourceDataSyncRequest:
    out: CreateResourceDataSyncRequest = {}  # type: ignore[typeddict-item]
    if data.get("SyncName") is not None:
        out["sync_name"] = data["SyncName"]
    else:
        out["sync_name"] = ""
    if data.get("S3Destination") is not None:
        import capo_ssm.types.resource_data_sync_s3_destination

        out["s3_destination"] = (
            capo_ssm.types.resource_data_sync_s3_destination.deserialize_aws_json_1_1(
                data["S3Destination"]
            )
        )
    if data.get("SyncType") is not None:
        out["sync_type"] = data["SyncType"]
    if data.get("SyncSource") is not None:
        import capo_ssm.types.resource_data_sync_source

        out["sync_source"] = (
            capo_ssm.types.resource_data_sync_source.deserialize_aws_json_1_1(
                data["SyncSource"]
            )
        )
    return out
