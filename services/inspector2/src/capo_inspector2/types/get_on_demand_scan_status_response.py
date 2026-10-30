"""Generated from Smithy shape ``com.amazonaws.inspector2#GetOnDemandScanStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.on_demand_resource_type
    import capo_inspector2.types.on_demand_scan_status
    import capo_inspector2.types.on_demand_scan_status_reason
    import capo_inspector2.types.resource_id
    import capo_inspector2.types.scan_id


class GetOnDemandScanStatusResponse(TypedDict, closed=True):
    scan_id: "capo_inspector2.types.scan_id.ScanId"
    """<p>The unique identifier of the on-demand scan.</p>"""
    resource_id: "capo_inspector2.types.resource_id.ResourceId"
    """<p>The ID of the resource that was scanned.</p>"""
    resource_type: "capo_inspector2.types.on_demand_resource_type.OnDemandResourceType"
    """<p>The type of the resource that was scanned.</p>"""
    scan_status: "capo_inspector2.types.on_demand_scan_status.OnDemandScanStatus"
    """<p>The current status of the on-demand scan.</p>"""
    scan_status_reason: NotRequired[
        "capo_inspector2.types.on_demand_scan_status_reason.OnDemandScanStatusReason"
    ]
    """<p>The reason associated with the current on-demand scan status.</p>"""
    started_at: "datetime.datetime"
    """<p>The date and time, in ISO 8601 format, when the on-demand scan started.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The date and time, in ISO 8601 format, when the on-demand scan completed. This field is absent if the scan has not completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOnDemandScanStatusResponse) -> dict:
    out: dict = {}
    out["scanId"] = value["scan_id"]
    out["resourceId"] = value["resource_id"]
    import capo_inspector2.types.on_demand_resource_type

    out["resourceType"] = capo_inspector2.types.on_demand_resource_type.serialize_json(
        value["resource_type"]
    )
    import capo_inspector2.types.on_demand_scan_status

    out["scanStatus"] = capo_inspector2.types.on_demand_scan_status.serialize_json(
        value["scan_status"]
    )
    if "scan_status_reason" in value:
        import capo_inspector2.types.on_demand_scan_status_reason

        out["scanStatusReason"] = (
            capo_inspector2.types.on_demand_scan_status_reason.serialize_json(
                value["scan_status_reason"]
            )
        )
    import capo_inspector2._protocol.serialize

    out["startedAt"] = capo_inspector2._protocol.serialize.fmt_date_time(
        value["started_at"]
    )
    if "completed_at" in value:
        import capo_inspector2._protocol.serialize

        out["completedAt"] = capo_inspector2._protocol.serialize.fmt_date_time(
            value["completed_at"]
        )
    return out


def deserialize_json(data: dict) -> GetOnDemandScanStatusResponse:
    out: GetOnDemandScanStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("scanId") is not None:
        out["scan_id"] = data["scanId"]
    else:
        out["scan_id"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("resourceType") is not None:
        import capo_inspector2.types.on_demand_resource_type

        out["resource_type"] = (
            capo_inspector2.types.on_demand_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_inspector2.types.on_demand_resource_type.OnDemandResourceType", ""
        )
    if data.get("scanStatus") is not None:
        import capo_inspector2.types.on_demand_scan_status

        out["scan_status"] = (
            capo_inspector2.types.on_demand_scan_status.deserialize_json(
                data["scanStatus"]
            )
        )
    else:
        import typing

        out["scan_status"] = typing.cast(
            "capo_inspector2.types.on_demand_scan_status.OnDemandScanStatus", ""
        )
    if data.get("scanStatusReason") is not None:
        import capo_inspector2.types.on_demand_scan_status_reason

        out["scan_status_reason"] = (
            capo_inspector2.types.on_demand_scan_status_reason.deserialize_json(
                data["scanStatusReason"]
            )
        )
    if data.get("startedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["startedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("completedAt") is not None:
        import datetime

        out["completed_at"] = datetime.datetime.fromisoformat(
            data["completedAt"].replace("Z", "+00:00")
        )
    return out
