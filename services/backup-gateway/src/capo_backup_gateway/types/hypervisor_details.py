"""Generated from Smithy shape ``com.amazonaws.backupgateway#HypervisorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.host
    import capo_backup_gateway.types.hypervisor_state
    import capo_backup_gateway.types.kms_key_arn
    import capo_backup_gateway.types.log_group_arn
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.server_arn
    import capo_backup_gateway.types.string
    import capo_backup_gateway.types.sync_metadata_status
    import capo_backup_gateway.types.time


class HypervisorDetails(TypedDict, closed=True):
    host: NotRequired["capo_backup_gateway.types.host.Host"]
    """<p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>"""
    hypervisor_arn: NotRequired["capo_backup_gateway.types.server_arn.ServerArn"]
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""
    kms_key_arn: NotRequired["capo_backup_gateway.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS used to encrypt the hypervisor.</p>"""
    name: NotRequired["capo_backup_gateway.types.name.Name"]
    """<p>This is the name of the specified hypervisor.</p>"""
    log_group_arn: NotRequired["capo_backup_gateway.types.log_group_arn.LogGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the group of gateways within the requested log.</p>"""
    state: NotRequired["capo_backup_gateway.types.hypervisor_state.HypervisorState"]
    """<p>This is the current state of the specified hypervisor.</p> <p>The possible states are <code>PENDING</code>, <code>ONLINE</code>, <code>OFFLINE</code>, or <code>ERROR</code>.</p>"""
    last_successful_metadata_sync_time: NotRequired[
        "capo_backup_gateway.types.time.Time"
    ]
    """<p>This is the time when the most recent successful sync of metadata occurred.</p>"""
    latest_metadata_sync_status_message: NotRequired[
        "capo_backup_gateway.types.string.string"
    ]
    """<p>This is the most recent status for the indicated metadata sync.</p>"""
    latest_metadata_sync_status: NotRequired[
        "capo_backup_gateway.types.sync_metadata_status.SyncMetadataStatus"
    ]
    """<p>This is the most recent status for the indicated metadata sync.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HypervisorDetails) -> dict:
    out: dict = {}
    if "host" in value:
        out["Host"] = value["host"]
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    if "state" in value:
        out["State"] = value["state"]
    if "last_successful_metadata_sync_time" in value:
        import capo_backup_gateway.types.time

        out["LastSuccessfulMetadataSyncTime"] = (
            capo_backup_gateway.types.time.serialize_aws_json_1_0(
                value["last_successful_metadata_sync_time"]
            )
        )
    if "latest_metadata_sync_status_message" in value:
        out["LatestMetadataSyncStatusMessage"] = value[
            "latest_metadata_sync_status_message"
        ]
    if "latest_metadata_sync_status" in value:
        out["LatestMetadataSyncStatus"] = value["latest_metadata_sync_status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HypervisorDetails:
    out: HypervisorDetails = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("LogGroupArn") is not None:
        out["log_group_arn"] = data["LogGroupArn"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("LastSuccessfulMetadataSyncTime") is not None:
        import capo_backup_gateway.types.time

        out["last_successful_metadata_sync_time"] = (
            capo_backup_gateway.types.time.deserialize_aws_json_1_0(
                data["LastSuccessfulMetadataSyncTime"]
            )
        )
    if data.get("LatestMetadataSyncStatusMessage") is not None:
        out["latest_metadata_sync_status_message"] = data[
            "LatestMetadataSyncStatusMessage"
        ]
    if data.get("LatestMetadataSyncStatus") is not None:
        out["latest_metadata_sync_status"] = data["LatestMetadataSyncStatus"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HypervisorDetails) -> dict:
    out: dict = {}
    if "host" in value:
        out["Host"] = value["host"]
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    if "state" in value:
        out["State"] = value["state"]
    if "last_successful_metadata_sync_time" in value:
        import capo_backup_gateway.types.time

        out["LastSuccessfulMetadataSyncTime"] = (
            capo_backup_gateway.types.time.serialize_cbor(
                value["last_successful_metadata_sync_time"]
            )
        )
    if "latest_metadata_sync_status_message" in value:
        out["LatestMetadataSyncStatusMessage"] = value[
            "latest_metadata_sync_status_message"
        ]
    if "latest_metadata_sync_status" in value:
        out["LatestMetadataSyncStatus"] = value["latest_metadata_sync_status"]
    return out


def deserialize_cbor(data: dict) -> HypervisorDetails:
    out: HypervisorDetails = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("LogGroupArn") is not None:
        out["log_group_arn"] = data["LogGroupArn"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("LastSuccessfulMetadataSyncTime") is not None:
        import capo_backup_gateway.types.time

        out["last_successful_metadata_sync_time"] = (
            capo_backup_gateway.types.time.deserialize_cbor(
                data["LastSuccessfulMetadataSyncTime"]
            )
        )
    if data.get("LatestMetadataSyncStatusMessage") is not None:
        out["latest_metadata_sync_status_message"] = data[
            "LatestMetadataSyncStatusMessage"
        ]
    if data.get("LatestMetadataSyncStatus") is not None:
        out["latest_metadata_sync_status"] = data["LatestMetadataSyncStatus"]
    return out
