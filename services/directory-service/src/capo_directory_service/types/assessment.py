"""Generated from Smithy shape ``com.amazonaws.directoryservice#Assessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_id
    import capo_directory_service.types.assessment_instance_ids
    import capo_directory_service.types.assessment_report_type
    import capo_directory_service.types.assessment_start_time
    import capo_directory_service.types.assessment_status
    import capo_directory_service.types.assessment_status_code
    import capo_directory_service.types.assessment_status_reason
    import capo_directory_service.types.assessment_version
    import capo_directory_service.types.customer_dns_ips
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.directory_name
    import capo_directory_service.types.last_update_date_time
    import capo_directory_service.types.security_group_ids
    import capo_directory_service.types.subnet_ids
    import capo_directory_service.types.vpc_id


class Assessment(TypedDict, closed=True):
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
    status_code: NotRequired[
        "capo_directory_service.types.assessment_status_code.AssessmentStatusCode"
    ]
    """<p>A detailed status code providing additional information about the assessment state.</p>"""
    status_reason: NotRequired[
        "capo_directory_service.types.assessment_status_reason.AssessmentStatusReason"
    ]
    """<p>A human-readable description of the current assessment status, including any error details or progress information.</p>"""
    customer_dns_ips: NotRequired[
        "capo_directory_service.types.customer_dns_ips.CustomerDnsIps"
    ]
    """<p>The IP addresses of the DNS servers or domain controllers in your self-managed AD environment.</p>"""
    vpc_id: NotRequired["capo_directory_service.types.vpc_id.VpcId"]
    """<p>Contains Amazon VPC information for the <code>StartADAssessment</code> operation. </p>"""
    subnet_ids: NotRequired["capo_directory_service.types.subnet_ids.SubnetIds"]
    """<p>A list of subnet identifiers in the Amazon VPC in which the hybrid directory is created.</p>"""
    security_group_ids: NotRequired[
        "capo_directory_service.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The security groups identifiers attached to the network interfaces.</p>"""
    self_managed_instance_ids: NotRequired[
        "capo_directory_service.types.assessment_instance_ids.AssessmentInstanceIds"
    ]
    """<p>The identifiers of the self-managed AD instances used to perform the assessment.</p>"""
    report_type: NotRequired[
        "capo_directory_service.types.assessment_report_type.AssessmentReportType"
    ]
    """<p>The type of assessment report generated. Valid values are <code>CUSTOMER</code> and <code>SYSTEM</code>.</p>"""
    version: NotRequired[
        "capo_directory_service.types.assessment_version.AssessmentVersion"
    ]
    """<p>The version of the assessment framework used to evaluate your self-managed AD environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Assessment) -> dict:
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
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "customer_dns_ips" in value:
        import capo_directory_service.types.customer_dns_ips

        out["CustomerDnsIps"] = (
            capo_directory_service.types.customer_dns_ips.serialize_aws_json_1_1(
                value["customer_dns_ips"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_directory_service.types.subnet_ids

        out["SubnetIds"] = (
            capo_directory_service.types.subnet_ids.serialize_aws_json_1_1(
                value["subnet_ids"]
            )
        )
    if "security_group_ids" in value:
        import capo_directory_service.types.security_group_ids

        out["SecurityGroupIds"] = (
            capo_directory_service.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "self_managed_instance_ids" in value:
        import capo_directory_service.types.assessment_instance_ids

        out["SelfManagedInstanceIds"] = (
            capo_directory_service.types.assessment_instance_ids.serialize_aws_json_1_1(
                value["self_managed_instance_ids"]
            )
        )
    if "report_type" in value:
        out["ReportType"] = value["report_type"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Assessment:
    out: Assessment = {}  # type: ignore[typeddict-item]
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
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("CustomerDnsIps") is not None:
        import capo_directory_service.types.customer_dns_ips

        out["customer_dns_ips"] = (
            capo_directory_service.types.customer_dns_ips.deserialize_aws_json_1_1(
                data["CustomerDnsIps"]
            )
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_directory_service.types.subnet_ids

        out["subnet_ids"] = (
            capo_directory_service.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_directory_service.types.security_group_ids

        out["security_group_ids"] = (
            capo_directory_service.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if data.get("SelfManagedInstanceIds") is not None:
        import capo_directory_service.types.assessment_instance_ids

        out["self_managed_instance_ids"] = (
            capo_directory_service.types.assessment_instance_ids.deserialize_aws_json_1_1(
                data["SelfManagedInstanceIds"]
            )
        )
    if data.get("ReportType") is not None:
        out["report_type"] = data["ReportType"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Assessment) -> dict:
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
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "customer_dns_ips" in value:
        import capo_directory_service.types.customer_dns_ips

        out["CustomerDnsIps"] = (
            capo_directory_service.types.customer_dns_ips.serialize_cbor(
                value["customer_dns_ips"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_directory_service.types.subnet_ids

        out["SubnetIds"] = capo_directory_service.types.subnet_ids.serialize_cbor(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_directory_service.types.security_group_ids

        out["SecurityGroupIds"] = (
            capo_directory_service.types.security_group_ids.serialize_cbor(
                value["security_group_ids"]
            )
        )
    if "self_managed_instance_ids" in value:
        import capo_directory_service.types.assessment_instance_ids

        out["SelfManagedInstanceIds"] = (
            capo_directory_service.types.assessment_instance_ids.serialize_cbor(
                value["self_managed_instance_ids"]
            )
        )
    if "report_type" in value:
        out["ReportType"] = value["report_type"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_cbor(data: dict) -> Assessment:
    out: Assessment = {}  # type: ignore[typeddict-item]
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
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("CustomerDnsIps") is not None:
        import capo_directory_service.types.customer_dns_ips

        out["customer_dns_ips"] = (
            capo_directory_service.types.customer_dns_ips.deserialize_cbor(
                data["CustomerDnsIps"]
            )
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_directory_service.types.subnet_ids

        out["subnet_ids"] = capo_directory_service.types.subnet_ids.deserialize_cbor(
            data["SubnetIds"]
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_directory_service.types.security_group_ids

        out["security_group_ids"] = (
            capo_directory_service.types.security_group_ids.deserialize_cbor(
                data["SecurityGroupIds"]
            )
        )
    if data.get("SelfManagedInstanceIds") is not None:
        import capo_directory_service.types.assessment_instance_ids

        out["self_managed_instance_ids"] = (
            capo_directory_service.types.assessment_instance_ids.deserialize_cbor(
                data["SelfManagedInstanceIds"]
            )
        )
    if data.get("ReportType") is not None:
        out["report_type"] = data["ReportType"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
