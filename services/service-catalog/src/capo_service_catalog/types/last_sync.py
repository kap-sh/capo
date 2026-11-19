"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LastSync``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id
    import capo_service_catalog.types.last_successful_sync_time
    import capo_service_catalog.types.last_sync_status
    import capo_service_catalog.types.last_sync_status_message
    import capo_service_catalog.types.last_sync_time


class LastSync(TypedDict, closed=True):
    last_sync_time: NotRequired[
        "capo_service_catalog.types.last_sync_time.LastSyncTime"
    ]
    """<p>The time of the last attempted sync from the repository to the Service Catalog product. </p>"""
    last_sync_status: NotRequired[
        "capo_service_catalog.types.last_sync_status.LastSyncStatus"
    ]
    """<p>The current status of the sync. Responses include <code>SUCCEEDED</code> or <code>FAILED</code>. </p>"""
    last_sync_status_message: NotRequired[
        "capo_service_catalog.types.last_sync_status_message.LastSyncStatusMessage"
    ]
    """<p>The sync's status message. </p>"""
    last_successful_sync_time: NotRequired[
        "capo_service_catalog.types.last_successful_sync_time.LastSuccessfulSyncTime"
    ]
    """<p>The time of the latest successful sync from the source repo artifact to the Service Catalog product.</p>"""
    last_successful_sync_provisioning_artifact_id: NotRequired[
        "capo_service_catalog.types.id.Id"
    ]
    """<p>The ProvisioningArtifactID of the ProvisioningArtifact created from the latest successful sync. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastSync) -> dict:
    out: dict = {}
    if "last_sync_time" in value:
        import capo_service_catalog.types.last_sync_time

        out["LastSyncTime"] = (
            capo_service_catalog.types.last_sync_time.serialize_aws_json_1_1(
                value["last_sync_time"]
            )
        )
    if "last_sync_status" in value:
        import capo_service_catalog.types.last_sync_status

        out["LastSyncStatus"] = (
            capo_service_catalog.types.last_sync_status.serialize_aws_json_1_1(
                value["last_sync_status"]
            )
        )
    if "last_sync_status_message" in value:
        out["LastSyncStatusMessage"] = value["last_sync_status_message"]
    if "last_successful_sync_time" in value:
        import capo_service_catalog.types.last_successful_sync_time

        out["LastSuccessfulSyncTime"] = (
            capo_service_catalog.types.last_successful_sync_time.serialize_aws_json_1_1(
                value["last_successful_sync_time"]
            )
        )
    if "last_successful_sync_provisioning_artifact_id" in value:
        out["LastSuccessfulSyncProvisioningArtifactId"] = value[
            "last_successful_sync_provisioning_artifact_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> LastSync:
    out: LastSync = {}  # type: ignore[typeddict-item]
    if data.get("LastSyncTime") is not None:
        import capo_service_catalog.types.last_sync_time

        out["last_sync_time"] = (
            capo_service_catalog.types.last_sync_time.deserialize_aws_json_1_1(
                data["LastSyncTime"]
            )
        )
    if data.get("LastSyncStatus") is not None:
        import capo_service_catalog.types.last_sync_status

        out["last_sync_status"] = (
            capo_service_catalog.types.last_sync_status.deserialize_aws_json_1_1(
                data["LastSyncStatus"]
            )
        )
    if data.get("LastSyncStatusMessage") is not None:
        out["last_sync_status_message"] = data["LastSyncStatusMessage"]
    if data.get("LastSuccessfulSyncTime") is not None:
        import capo_service_catalog.types.last_successful_sync_time

        out["last_successful_sync_time"] = (
            capo_service_catalog.types.last_successful_sync_time.deserialize_aws_json_1_1(
                data["LastSuccessfulSyncTime"]
            )
        )
    if data.get("LastSuccessfulSyncProvisioningArtifactId") is not None:
        out["last_successful_sync_provisioning_artifact_id"] = data[
            "LastSuccessfulSyncProvisioningArtifactId"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LastSync) -> dict:
    out: dict = {}
    if "last_sync_time" in value:
        import capo_service_catalog.types.last_sync_time

        out["LastSyncTime"] = capo_service_catalog.types.last_sync_time.serialize_cbor(
            value["last_sync_time"]
        )
    if "last_sync_status" in value:
        import capo_service_catalog.types.last_sync_status

        out["LastSyncStatus"] = (
            capo_service_catalog.types.last_sync_status.serialize_cbor(
                value["last_sync_status"]
            )
        )
    if "last_sync_status_message" in value:
        out["LastSyncStatusMessage"] = value["last_sync_status_message"]
    if "last_successful_sync_time" in value:
        import capo_service_catalog.types.last_successful_sync_time

        out["LastSuccessfulSyncTime"] = (
            capo_service_catalog.types.last_successful_sync_time.serialize_cbor(
                value["last_successful_sync_time"]
            )
        )
    if "last_successful_sync_provisioning_artifact_id" in value:
        out["LastSuccessfulSyncProvisioningArtifactId"] = value[
            "last_successful_sync_provisioning_artifact_id"
        ]
    return out


def deserialize_cbor(data: dict) -> LastSync:
    out: LastSync = {}  # type: ignore[typeddict-item]
    if data.get("LastSyncTime") is not None:
        import capo_service_catalog.types.last_sync_time

        out["last_sync_time"] = (
            capo_service_catalog.types.last_sync_time.deserialize_cbor(
                data["LastSyncTime"]
            )
        )
    if data.get("LastSyncStatus") is not None:
        import capo_service_catalog.types.last_sync_status

        out["last_sync_status"] = (
            capo_service_catalog.types.last_sync_status.deserialize_cbor(
                data["LastSyncStatus"]
            )
        )
    if data.get("LastSyncStatusMessage") is not None:
        out["last_sync_status_message"] = data["LastSyncStatusMessage"]
    if data.get("LastSuccessfulSyncTime") is not None:
        import capo_service_catalog.types.last_successful_sync_time

        out["last_successful_sync_time"] = (
            capo_service_catalog.types.last_successful_sync_time.deserialize_cbor(
                data["LastSuccessfulSyncTime"]
            )
        )
    if data.get("LastSuccessfulSyncProvisioningArtifactId") is not None:
        out["last_successful_sync_provisioning_artifact_id"] = data[
            "LastSuccessfulSyncProvisioningArtifactId"
        ]
    return out
