"""Generated from Smithy shape ``com.amazonaws.ec2#ReportInstanceStatusRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.instance_id_string_list
    import capo_ec2.types.reason_codes_list
    import capo_ec2.types.report_instance_status_request_description
    import capo_ec2.types.report_status_type


class ReportInstanceStatusRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instances: NotRequired[
        "capo_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The instances.</p>"""
    status: NotRequired["capo_ec2.types.report_status_type.ReportStatusType"]
    """<p>The status of all instances listed.</p>"""
    start_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time at which the reported instance health state began.</p>"""
    end_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time at which the reported instance health state ended.</p>"""
    reason_codes: NotRequired["capo_ec2.types.reason_codes_list.ReasonCodesList"]
    """<p>The reason codes that describe the health state of your instance.</p> <ul> <li> <p> <code>instance-stuck-in-state</code>: My instance is stuck in a state.</p> </li> <li> <p> <code>unresponsive</code>: My instance is unresponsive.</p> </li> <li> <p> <code>not-accepting-credentials</code>: My instance is not accepting my credentials.</p> </li> <li> <p> <code>password-not-available</code>: A password is not available for my instance.</p> </li> <li> <p> <code>performance-network</code>: My instance is experiencing performance problems that I believe are network related.</p> </li> <li> <p> <code>performance-instance-store</code>: My instance is experiencing performance problems that I believe are related to the instance stores.</p> </li> <li> <p> <code>performance-ebs-volume</code>: My instance is experiencing performance problems that I believe are related to an EBS volume.</p> </li> <li> <p> <code>performance-other</code>: My instance is experiencing performance problems.</p> </li> <li> <p> <code>other</code>: [explain using the description parameter]</p> </li> </ul>"""
    description: NotRequired[
        "capo_ec2.types.report_instance_status_request_description.ReportInstanceStatusRequestDescription"
    ]
    """<p>Descriptive text about the health state of your instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReportInstanceStatusRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instances" in value:
        import capo_ec2.types.instance_id_string_list

        capo_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instances"], pairs, f"{key_prefix}InstanceId"
        )
    if "status" in value:
        import capo_ec2.types.report_status_type

        capo_ec2.types.report_status_type.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "start_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "reason_codes" in value:
        import capo_ec2.types.reason_codes_list

        capo_ec2.types.reason_codes_list.serialize_ec2_query(
            value["reason_codes"], pairs, f"{key_prefix}ReasonCode"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_ec2_query(el: Element) -> ReportInstanceStatusRequest:
    out: ReportInstanceStatusRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instances = el.find("instanceId")
    if child_instances is not None:
        import capo_ec2.types.instance_id_string_list

        out["instances"] = capo_ec2.types.instance_id_string_list.deserialize_ec2_query(
            child_instances
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.report_status_type

        out["status"] = capo_ec2.types.report_status_type.deserialize_ec2_query(
            child_status
        )
    child_start_time = el.find("startTime")
    if child_start_time is not None:
        import capo_ec2.types.date_time

        out["start_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_start_time
        )
    child_end_time = el.find("endTime")
    if child_end_time is not None:
        import capo_ec2.types.date_time

        out["end_time"] = capo_ec2.types.date_time.deserialize_ec2_query(child_end_time)
    child_reason_codes = el.find("reasonCode")
    if child_reason_codes is not None:
        import capo_ec2.types.reason_codes_list

        out["reason_codes"] = capo_ec2.types.reason_codes_list.deserialize_ec2_query(
            child_reason_codes
        )
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out


def redact_sensitive(value: ReportInstanceStatusRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
