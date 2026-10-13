"""Generated from Smithy shape ``com.amazonaws.guardduty#Service``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.action
    import capo_guardduty.types.boolean
    import capo_guardduty.types.detection
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.ebs_volume_scan_details
    import capo_guardduty.types.evidence
    import capo_guardduty.types.integer
    import capo_guardduty.types.malware_scan_details
    import capo_guardduty.types.runtime_details
    import capo_guardduty.types.service_additional_info
    import capo_guardduty.types.string


class Service(TypedDict, closed=True):
    action: NotRequired["capo_guardduty.types.action.Action"]
    """<p>Information about the activity that is described in a finding.</p>"""
    evidence: NotRequired["capo_guardduty.types.evidence.Evidence"]
    """<p>An evidence object associated with the service.</p>"""
    archived: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates whether this finding is archived.</p>"""
    count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The total count of the occurrences of this finding type.</p>"""
    detector_id: NotRequired["capo_guardduty.types.detector_id.DetectorId"]
    """<p>The detector ID for the GuardDuty service.</p>"""
    event_first_seen: NotRequired["capo_guardduty.types.string.String"]
    """<p>The first-seen timestamp of the activity that prompted GuardDuty to generate this finding.</p>"""
    event_last_seen: NotRequired["capo_guardduty.types.string.String"]
    """<p>The last-seen timestamp of the activity that prompted GuardDuty to generate this finding.</p>"""
    resource_role: NotRequired["capo_guardduty.types.string.String"]
    """<p>The resource role information for this finding.</p>"""
    service_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the Amazon Web Services service (GuardDuty) that generated a finding.</p>"""
    user_feedback: NotRequired["capo_guardduty.types.string.String"]
    """<p>Feedback that was submitted about the finding.</p>"""
    additional_info: NotRequired[
        "capo_guardduty.types.service_additional_info.ServiceAdditionalInfo"
    ]
    """<p>Contains additional information about the generated finding.</p>"""
    feature_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the feature that generated a finding.</p>"""
    ebs_volume_scan_details: NotRequired[
        "capo_guardduty.types.ebs_volume_scan_details.EbsVolumeScanDetails"
    ]
    """<p>Returns details from the malware scan that created a finding.</p>"""
    runtime_details: NotRequired["capo_guardduty.types.runtime_details.RuntimeDetails"]
    """<p>Information about the process and any required context values for a specific finding</p>"""
    detection: NotRequired["capo_guardduty.types.detection.Detection"]
    """<p>Contains information about the detected unusual behavior.</p>"""
    malware_scan_details: NotRequired[
        "capo_guardduty.types.malware_scan_details.MalwareScanDetails"
    ]
    """<p>Returns details from the malware scan that generated a GuardDuty finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Service) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_guardduty.types.action

        out["action"] = capo_guardduty.types.action.serialize_json(value["action"])
    if "evidence" in value:
        import capo_guardduty.types.evidence

        out["evidence"] = capo_guardduty.types.evidence.serialize_json(
            value["evidence"]
        )
    if "archived" in value:
        out["archived"] = value["archived"]
    if "count" in value:
        out["count"] = value["count"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "event_first_seen" in value:
        out["eventFirstSeen"] = value["event_first_seen"]
    if "event_last_seen" in value:
        out["eventLastSeen"] = value["event_last_seen"]
    if "resource_role" in value:
        out["resourceRole"] = value["resource_role"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "user_feedback" in value:
        out["userFeedback"] = value["user_feedback"]
    if "additional_info" in value:
        import capo_guardduty.types.service_additional_info

        out["additionalInfo"] = (
            capo_guardduty.types.service_additional_info.serialize_json(
                value["additional_info"]
            )
        )
    if "feature_name" in value:
        out["featureName"] = value["feature_name"]
    if "ebs_volume_scan_details" in value:
        import capo_guardduty.types.ebs_volume_scan_details

        out["ebsVolumeScanDetails"] = (
            capo_guardduty.types.ebs_volume_scan_details.serialize_json(
                value["ebs_volume_scan_details"]
            )
        )
    if "runtime_details" in value:
        import capo_guardduty.types.runtime_details

        out["runtimeDetails"] = capo_guardduty.types.runtime_details.serialize_json(
            value["runtime_details"]
        )
    if "detection" in value:
        import capo_guardduty.types.detection

        out["detection"] = capo_guardduty.types.detection.serialize_json(
            value["detection"]
        )
    if "malware_scan_details" in value:
        import capo_guardduty.types.malware_scan_details

        out["malwareScanDetails"] = (
            capo_guardduty.types.malware_scan_details.serialize_json(
                value["malware_scan_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_guardduty.types.action

        out["action"] = capo_guardduty.types.action.deserialize_json(data["action"])
    if data.get("evidence") is not None:
        import capo_guardduty.types.evidence

        out["evidence"] = capo_guardduty.types.evidence.deserialize_json(
            data["evidence"]
        )
    if data.get("archived") is not None:
        out["archived"] = data["archived"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    if data.get("eventFirstSeen") is not None:
        out["event_first_seen"] = data["eventFirstSeen"]
    if data.get("eventLastSeen") is not None:
        out["event_last_seen"] = data["eventLastSeen"]
    if data.get("resourceRole") is not None:
        out["resource_role"] = data["resourceRole"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("userFeedback") is not None:
        out["user_feedback"] = data["userFeedback"]
    if data.get("additionalInfo") is not None:
        import capo_guardduty.types.service_additional_info

        out["additional_info"] = (
            capo_guardduty.types.service_additional_info.deserialize_json(
                data["additionalInfo"]
            )
        )
    if data.get("featureName") is not None:
        out["feature_name"] = data["featureName"]
    if data.get("ebsVolumeScanDetails") is not None:
        import capo_guardduty.types.ebs_volume_scan_details

        out["ebs_volume_scan_details"] = (
            capo_guardduty.types.ebs_volume_scan_details.deserialize_json(
                data["ebsVolumeScanDetails"]
            )
        )
    if data.get("runtimeDetails") is not None:
        import capo_guardduty.types.runtime_details

        out["runtime_details"] = capo_guardduty.types.runtime_details.deserialize_json(
            data["runtimeDetails"]
        )
    if data.get("detection") is not None:
        import capo_guardduty.types.detection

        out["detection"] = capo_guardduty.types.detection.deserialize_json(
            data["detection"]
        )
    if data.get("malwareScanDetails") is not None:
        import capo_guardduty.types.malware_scan_details

        out["malware_scan_details"] = (
            capo_guardduty.types.malware_scan_details.deserialize_json(
                data["malwareScanDetails"]
            )
        )
    return out


def redact_sensitive(value: Service) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action" in value:
        import capo_guardduty.types.action

        out["action"] = capo_guardduty.types.action.redact_sensitive(value["action"])
    if "detection" in value:
        import capo_guardduty.types.detection

        out["detection"] = capo_guardduty.types.detection.redact_sensitive(
            value["detection"]
        )
    return out
