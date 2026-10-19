"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ServiceQuotaWarningSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.account_id
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.service_quota_warning_status


class ServiceQuotaWarningSummary(TypedDict, closed=True):
    account_id: "capo_arc_region_switch.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID that owns the plan that the warning applies to.</p>"""
    quota_region: "capo_arc_region_switch.types.region.Region"
    """<p>The Amazon Web Services Region that the quota applies to.</p>"""
    service_code: NotRequired["str"]
    """<p>The service code of the service that the quota belongs to, as defined in Service Quotas. For example, <code>ec2</code>.</p>"""
    quota_code: NotRequired["str"]
    """<p>The quota code of the quota that the warning applies to, as defined in Service Quotas.</p>"""
    quota_name: NotRequired["str"]
    """<p>The name of the quota that the warning applies to, as defined in Service Quotas.</p>"""
    status: "capo_arc_region_switch.types.service_quota_warning_status.ServiceQuotaWarningStatus"
    """<p>The status of the service quota warning.</p>"""
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan that the warning applies to.</p>"""
    request_id: NotRequired["str"]
    """<p>The ID of the quota increase request that Region switch submitted, if it submitted one for this quota.</p>"""
    case_id: NotRequired["str"]
    """<p>The ID of the support case associated with the quota increase request, if Region switch submitted one for this quota.</p>"""
    warning_message: NotRequired["str"]
    """<p>A message that describes the service quota warning.</p>"""
    last_checked_at: NotRequired["datetime.datetime"]
    """<p>The time (UTC) when Region switch last checked this quota.</p>"""
    warning_created_at: NotRequired["datetime.datetime"]
    """<p>The time (UTC) when Region switch created this warning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaWarningSummary) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["quotaRegion"] = value["quota_region"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "quota_name" in value:
        out["quotaName"] = value["quota_name"]
    import capo_arc_region_switch.types.service_quota_warning_status

    out["status"] = (
        capo_arc_region_switch.types.service_quota_warning_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    out["planArn"] = value["plan_arn"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    if "warning_message" in value:
        out["warningMessage"] = value["warning_message"]
    if "last_checked_at" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["lastCheckedAt"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_checked_at"]
            )
        )
    if "warning_created_at" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["warningCreatedAt"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["warning_created_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaWarningSummary:
    out: ServiceQuotaWarningSummary = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("quotaRegion") is not None:
        out["quota_region"] = data["quotaRegion"]
    else:
        out["quota_region"] = ""
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    if data.get("quotaName") is not None:
        out["quota_name"] = data["quotaName"]
    if data.get("status") is not None:
        import capo_arc_region_switch.types.service_quota_warning_status

        out["status"] = (
            capo_arc_region_switch.types.service_quota_warning_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_arc_region_switch.types.service_quota_warning_status.ServiceQuotaWarningStatus",
            "",
        )
    if data.get("planArn") is not None:
        out["plan_arn"] = data["planArn"]
    else:
        out["plan_arn"] = ""
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    if data.get("warningMessage") is not None:
        out["warning_message"] = data["warningMessage"]
    if data.get("lastCheckedAt") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["last_checked_at"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastCheckedAt"]
            )
        )
    if data.get("warningCreatedAt") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["warning_created_at"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["warningCreatedAt"]
            )
        )
    return out
