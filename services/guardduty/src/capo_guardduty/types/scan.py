"""Generated from Smithy shape ``com.amazonaws.guardduty#Scan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.non_empty_string
    import capo_guardduty.types.positive_long
    import capo_guardduty.types.resource_details
    import capo_guardduty.types.scan_result_details
    import capo_guardduty.types.scan_status
    import capo_guardduty.types.scan_type
    import capo_guardduty.types.timestamp
    import capo_guardduty.types.trigger_details
    import capo_guardduty.types.volume_details


class Scan(TypedDict, closed=True):
    detector_id: NotRequired["capo_guardduty.types.detector_id.DetectorId"]
    """<p>The unique ID of the detector that is associated with the request.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    admin_detector_id: NotRequired["capo_guardduty.types.detector_id.DetectorId"]
    """<p>The unique detector ID of the administrator account that the request is associated with. If the account is an administrator, the <code>AdminDetectorId</code> will be the same as the one used for <code>DetectorId</code>.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    scan_id: NotRequired["capo_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The unique scan ID associated with a scan entry.</p>"""
    scan_status: NotRequired["capo_guardduty.types.scan_status.ScanStatus"]
    """<p>An enum value representing possible scan statuses.</p>"""
    failure_reason: NotRequired["capo_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>Represents the reason for <code>FAILED</code> scan status.</p>"""
    scan_start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp of when the scan was triggered.</p>"""
    scan_end_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp of when the scan was finished.</p>"""
    trigger_details: NotRequired["capo_guardduty.types.trigger_details.TriggerDetails"]
    """<p>Specifies the reason why the scan was initiated.</p>"""
    resource_details: NotRequired[
        "capo_guardduty.types.resource_details.ResourceDetails"
    ]
    """<p>Represents the resources that were scanned in the scan entry.</p>"""
    scan_result_details: NotRequired[
        "capo_guardduty.types.scan_result_details.ScanResultDetails"
    ]
    """<p>Represents the result of the scan.</p>"""
    account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The ID for the account that belongs to the scan.</p>"""
    total_bytes: NotRequired["capo_guardduty.types.positive_long.PositiveLong"]
    """<p>Represents total bytes that were scanned.</p>"""
    file_count: NotRequired["capo_guardduty.types.positive_long.PositiveLong"]
    """<p>Represents the number of files that were scanned.</p>"""
    attached_volumes: NotRequired["capo_guardduty.types.volume_details.VolumeDetails"]
    """<p>List of volumes that were attached to the original instance to be scanned.</p>"""
    scan_type: NotRequired["capo_guardduty.types.scan_type.ScanType"]
    """<p>Specifies the scan type that invoked the malware scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Scan) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "admin_detector_id" in value:
        out["adminDetectorId"] = value["admin_detector_id"]
    if "scan_id" in value:
        out["scanId"] = value["scan_id"]
    if "scan_status" in value:
        import capo_guardduty.types.scan_status

        out["scanStatus"] = capo_guardduty.types.scan_status.serialize_json(
            value["scan_status"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "scan_start_time" in value:
        import capo_guardduty.types.timestamp

        out["scanStartTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["scan_start_time"]
        )
    if "scan_end_time" in value:
        import capo_guardduty.types.timestamp

        out["scanEndTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["scan_end_time"]
        )
    if "trigger_details" in value:
        import capo_guardduty.types.trigger_details

        out["triggerDetails"] = capo_guardduty.types.trigger_details.serialize_json(
            value["trigger_details"]
        )
    if "resource_details" in value:
        import capo_guardduty.types.resource_details

        out["resourceDetails"] = capo_guardduty.types.resource_details.serialize_json(
            value["resource_details"]
        )
    if "scan_result_details" in value:
        import capo_guardduty.types.scan_result_details

        out["scanResultDetails"] = (
            capo_guardduty.types.scan_result_details.serialize_json(
                value["scan_result_details"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "total_bytes" in value:
        out["totalBytes"] = value["total_bytes"]
    if "file_count" in value:
        out["fileCount"] = value["file_count"]
    if "attached_volumes" in value:
        import capo_guardduty.types.volume_details

        out["attachedVolumes"] = capo_guardduty.types.volume_details.serialize_json(
            value["attached_volumes"]
        )
    if "scan_type" in value:
        import capo_guardduty.types.scan_type

        out["scanType"] = capo_guardduty.types.scan_type.serialize_json(
            value["scan_type"]
        )
    return out


def deserialize_json(data: dict) -> Scan:
    out: Scan = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    if data.get("adminDetectorId") is not None:
        out["admin_detector_id"] = data["adminDetectorId"]
    if data.get("scanId") is not None:
        out["scan_id"] = data["scanId"]
    if data.get("scanStatus") is not None:
        import capo_guardduty.types.scan_status

        out["scan_status"] = capo_guardduty.types.scan_status.deserialize_json(
            data["scanStatus"]
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("scanStartTime") is not None:
        import capo_guardduty.types.timestamp

        out["scan_start_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["scanStartTime"]
        )
    if data.get("scanEndTime") is not None:
        import capo_guardduty.types.timestamp

        out["scan_end_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["scanEndTime"]
        )
    if data.get("triggerDetails") is not None:
        import capo_guardduty.types.trigger_details

        out["trigger_details"] = capo_guardduty.types.trigger_details.deserialize_json(
            data["triggerDetails"]
        )
    if data.get("resourceDetails") is not None:
        import capo_guardduty.types.resource_details

        out["resource_details"] = (
            capo_guardduty.types.resource_details.deserialize_json(
                data["resourceDetails"]
            )
        )
    if data.get("scanResultDetails") is not None:
        import capo_guardduty.types.scan_result_details

        out["scan_result_details"] = (
            capo_guardduty.types.scan_result_details.deserialize_json(
                data["scanResultDetails"]
            )
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("totalBytes") is not None:
        out["total_bytes"] = data["totalBytes"]
    if data.get("fileCount") is not None:
        out["file_count"] = data["fileCount"]
    if data.get("attachedVolumes") is not None:
        import capo_guardduty.types.volume_details

        out["attached_volumes"] = capo_guardduty.types.volume_details.deserialize_json(
            data["attachedVolumes"]
        )
    if data.get("scanType") is not None:
        import capo_guardduty.types.scan_type

        out["scan_type"] = capo_guardduty.types.scan_type.deserialize_json(
            data["scanType"]
        )
    return out
