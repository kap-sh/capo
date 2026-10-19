"""Generated from Smithy shape ``com.amazonaws.proton#ServiceSyncBlockerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.latest_sync_blockers


class ServiceSyncBlockerSummary(TypedDict, closed=True):
    service_name: "str"
    """<p>The name of the service that you want to get the sync blocker summary for. If given a service instance name and a service name, it will return the blockers only applying to the instance that is blocked.</p> <p>If given only a service name, it will return the blockers that apply to all of the instances. In order to get the blockers for a single instance, you will need to make two distinct calls, one to get the sync blocker summary for the service and the other to get the sync blocker for the service instance.</p>"""
    service_instance_name: NotRequired["str"]
    """<p>The name of the service instance that you want sync your service configuration with.</p>"""
    latest_blockers: NotRequired[
        "capo_proton.types.latest_sync_blockers.LatestSyncBlockers"
    ]
    """<p>The latest active blockers for the synced service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceSyncBlockerSummary) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "latest_blockers" in value:
        import capo_proton.types.latest_sync_blockers

        out["latestBlockers"] = (
            capo_proton.types.latest_sync_blockers.serialize_aws_json_1_0(
                value["latest_blockers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceSyncBlockerSummary:
    out: ServiceSyncBlockerSummary = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("latestBlockers") is not None:
        import capo_proton.types.latest_sync_blockers

        out["latest_blockers"] = (
            capo_proton.types.latest_sync_blockers.deserialize_aws_json_1_0(
                data["latestBlockers"]
            )
        )
    return out
