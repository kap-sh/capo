"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_id
    import capo_directory_service.types.assessment_report_type
    import capo_directory_service.types.assessment_start_time
    import capo_directory_service.types.assessment_status
    import capo_directory_service.types.customer_dns_ips
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.directory_name
    import capo_directory_service.types.last_update_date_time


class AssessmentSummary(TypedDict, closed=True):
    assessment_id: NotRequired[
        "capo_directory_service.types.assessment_id.AssessmentId"
    ]
    """<p>The unique identifier of the directory assessment.</p>"""
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory associated with this assessment.</p>"""
    dns_name: NotRequired["capo_directory_service.types.directory_name.DirectoryName"]
    """<p>The fully qualified domain name (FQDN) of the Active Directory domain being assessed.</p>"""
    start_time: NotRequired[
        "capo_directory_service.types.assessment_start_time.AssessmentStartTime"
    ]
    """<p>The date and time when the assessment was initiated.</p>"""
    last_update_date_time: NotRequired[
        "capo_directory_service.types.last_update_date_time.LastUpdateDateTime"
    ]
    """<p>The date and time when the assessment status was last updated.</p>"""
    status: NotRequired[
        "capo_directory_service.types.assessment_status.AssessmentStatus"
    ]
    """<p>The current status of the assessment. Valid values include <code>SUCCESS</code>, <code>FAILED</code>, <code>PENDING</code>, and <code>IN_PROGRESS</code>.</p>"""
    customer_dns_ips: NotRequired[
        "capo_directory_service.types.customer_dns_ips.CustomerDnsIps"
    ]
    """<p>The IP addresses of the DNS servers or domain controllers in your self-managed AD environment.</p>"""
    report_type: NotRequired[
        "capo_directory_service.types.assessment_report_type.AssessmentReportType"
    ]
    """<p>The type of assessment report generated. Valid values include <code>CUSTOMER</code> and <code>SYSTEM</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentSummary) -> dict:
    out: dict = {}
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "start_time" in value:
        import capo_directory_service.types.assessment_start_time

        out["StartTime"] = (
            capo_directory_service.types.assessment_start_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "last_update_date_time" in value:
        import capo_directory_service.types.last_update_date_time

        out["LastUpdateDateTime"] = (
            capo_directory_service.types.last_update_date_time.serialize_aws_json_1_1(
                value["last_update_date_time"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "customer_dns_ips" in value:
        import capo_directory_service.types.customer_dns_ips

        out["CustomerDnsIps"] = (
            capo_directory_service.types.customer_dns_ips.serialize_aws_json_1_1(
                value["customer_dns_ips"]
            )
        )
    if "report_type" in value:
        out["ReportType"] = value["report_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentSummary:
    out: AssessmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("StartTime") is not None:
        import capo_directory_service.types.assessment_start_time

        out["start_time"] = (
            capo_directory_service.types.assessment_start_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if data.get("LastUpdateDateTime") is not None:
        import capo_directory_service.types.last_update_date_time

        out["last_update_date_time"] = (
            capo_directory_service.types.last_update_date_time.deserialize_aws_json_1_1(
                data["LastUpdateDateTime"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("CustomerDnsIps") is not None:
        import capo_directory_service.types.customer_dns_ips

        out["customer_dns_ips"] = (
            capo_directory_service.types.customer_dns_ips.deserialize_aws_json_1_1(
                data["CustomerDnsIps"]
            )
        )
    if data.get("ReportType") is not None:
        out["report_type"] = data["ReportType"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssessmentSummary) -> dict:
    out: dict = {}
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "start_time" in value:
        import capo_directory_service.types.assessment_start_time

        out["StartTime"] = (
            capo_directory_service.types.assessment_start_time.serialize_cbor(
                value["start_time"]
            )
        )
    if "last_update_date_time" in value:
        import capo_directory_service.types.last_update_date_time

        out["LastUpdateDateTime"] = (
            capo_directory_service.types.last_update_date_time.serialize_cbor(
                value["last_update_date_time"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "customer_dns_ips" in value:
        import capo_directory_service.types.customer_dns_ips

        out["CustomerDnsIps"] = (
            capo_directory_service.types.customer_dns_ips.serialize_cbor(
                value["customer_dns_ips"]
            )
        )
    if "report_type" in value:
        out["ReportType"] = value["report_type"]
    return out


def deserialize_cbor(data: dict) -> AssessmentSummary:
    out: AssessmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("StartTime") is not None:
        import capo_directory_service.types.assessment_start_time

        out["start_time"] = (
            capo_directory_service.types.assessment_start_time.deserialize_cbor(
                data["StartTime"]
            )
        )
    if data.get("LastUpdateDateTime") is not None:
        import capo_directory_service.types.last_update_date_time

        out["last_update_date_time"] = (
            capo_directory_service.types.last_update_date_time.deserialize_cbor(
                data["LastUpdateDateTime"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("CustomerDnsIps") is not None:
        import capo_directory_service.types.customer_dns_ips

        out["customer_dns_ips"] = (
            capo_directory_service.types.customer_dns_ips.deserialize_cbor(
                data["CustomerDnsIps"]
            )
        )
    if data.get("ReportType") is not None:
        out["report_type"] = data["ReportType"]
    return out
