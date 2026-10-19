"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceSyncBlockerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.resource_name
    import capo_proton.types.sync_blocker


class UpdateServiceSyncBlockerOutput(TypedDict, closed=True):
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service that you want to update the service sync blocker for.</p>"""
    service_instance_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service instance that you want to update the service sync blocker for.</p>"""
    service_sync_blocker: "capo_proton.types.sync_blocker.SyncBlocker"
    """<p>The detailed data on the service sync blocker that was updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceSyncBlockerOutput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    import capo_proton.types.sync_blocker

    out["serviceSyncBlocker"] = capo_proton.types.sync_blocker.serialize_aws_json_1_0(
        value["service_sync_blocker"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceSyncBlockerOutput:
    out: UpdateServiceSyncBlockerOutput = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("serviceSyncBlocker") is not None:
        import capo_proton.types.sync_blocker

        out["service_sync_blocker"] = (
            capo_proton.types.sync_blocker.deserialize_aws_json_1_0(
                data["serviceSyncBlocker"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceSyncBlockerOutput.service_sync_blocker required"
        )
    return out
