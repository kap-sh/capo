"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_check_run_status
    import capo_iot.types.check_compliant
    import capo_iot.types.error_code
    import capo_iot.types.error_message
    import capo_iot.types.non_compliant_resources_count
    import capo_iot.types.suppressed_non_compliant_resources_count
    import capo_iot.types.total_resources_count


class AuditCheckDetails(TypedDict, closed=True):
    check_run_status: NotRequired[
        "capo_iot.types.audit_check_run_status.AuditCheckRunStatus"
    ]
    """<p>The completion status of this check. One of "IN_PROGRESS", "WAITING_FOR_DATA_COLLECTION", "CANCELED", "COMPLETED_COMPLIANT", "COMPLETED_NON_COMPLIANT", or "FAILED".</p>"""
    check_compliant: NotRequired["capo_iot.types.check_compliant.CheckCompliant"]
    """<p>True if the check is complete and found all resources compliant.</p>"""
    total_resources_count: NotRequired[
        "capo_iot.types.total_resources_count.TotalResourcesCount"
    ]
    """<p>The number of resources on which the check was performed.</p>"""
    non_compliant_resources_count: NotRequired[
        "capo_iot.types.non_compliant_resources_count.NonCompliantResourcesCount"
    ]
    """<p>The number of resources that were found noncompliant during the check.</p>"""
    suppressed_non_compliant_resources_count: NotRequired[
        "capo_iot.types.suppressed_non_compliant_resources_count.SuppressedNonCompliantResourcesCount"
    ]
    """<p> Describes how many of the non-compliant resources created during the evaluation of an audit check were marked as suppressed. </p>"""
    error_code: NotRequired["capo_iot.types.error_code.ErrorCode"]
    """<p>The code of any error encountered when this check is performed during this audit. One of "INSUFFICIENT_PERMISSIONS" or "AUDIT_CHECK_DISABLED".</p>"""
    message: NotRequired["capo_iot.types.error_message.ErrorMessage"]
    """<p>The message associated with any error encountered when this check is performed during this audit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditCheckDetails) -> dict:
    out: dict = {}
    if "check_run_status" in value:
        import capo_iot.types.audit_check_run_status

        out["checkRunStatus"] = capo_iot.types.audit_check_run_status.serialize_json(
            value["check_run_status"]
        )
    if "check_compliant" in value:
        out["checkCompliant"] = value["check_compliant"]
    if "total_resources_count" in value:
        out["totalResourcesCount"] = value["total_resources_count"]
    if "non_compliant_resources_count" in value:
        out["nonCompliantResourcesCount"] = value["non_compliant_resources_count"]
    if "suppressed_non_compliant_resources_count" in value:
        out["suppressedNonCompliantResourcesCount"] = value[
            "suppressed_non_compliant_resources_count"
        ]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AuditCheckDetails:
    out: AuditCheckDetails = {}  # type: ignore[typeddict-item]
    if data.get("checkRunStatus") is not None:
        import capo_iot.types.audit_check_run_status

        out["check_run_status"] = (
            capo_iot.types.audit_check_run_status.deserialize_json(
                data["checkRunStatus"]
            )
        )
    if data.get("checkCompliant") is not None:
        out["check_compliant"] = data["checkCompliant"]
    if data.get("totalResourcesCount") is not None:
        out["total_resources_count"] = data["totalResourcesCount"]
    if data.get("nonCompliantResourcesCount") is not None:
        out["non_compliant_resources_count"] = data["nonCompliantResourcesCount"]
    if data.get("suppressedNonCompliantResourcesCount") is not None:
        out["suppressed_non_compliant_resources_count"] = data[
            "suppressedNonCompliantResourcesCount"
        ]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
