"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AccountInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.account_id
    import capo_compute_optimizer_automation.types.enrollment_status
    import capo_compute_optimizer_automation.types.organization_rule_mode


class AccountInfo(TypedDict, closed=True):
    account_id: "capo_compute_optimizer_automation.types.account_id.AccountId"
    """<p> The ID of the Amazon Web Services account. </p>"""
    status: "capo_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus"
    """<p> The enrollment status of the account: Active, Inactive, Pending, or Failed. </p>"""
    organization_rule_mode: "capo_compute_optimizer_automation.types.organization_rule_mode.OrganizationRuleMode"
    """<p>Specifies whether the management account can create Automation rules that implement optimization actions for this account. </p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current Automation enrollment status. </p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p>The timestamp when the account's Automation enrollment status was last updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountInfo) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_compute_optimizer_automation.types.enrollment_status

    out["status"] = (
        capo_compute_optimizer_automation.types.enrollment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_compute_optimizer_automation.types.organization_rule_mode

    out["organizationRuleMode"] = (
        capo_compute_optimizer_automation.types.organization_rule_mode.serialize_aws_json_1_0(
            value["organization_rule_mode"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_compute_optimizer_automation.types._prelude.timestamp

    out["lastUpdatedTimestamp"] = (
        capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_updated_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountInfo:
    out: AccountInfo = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("status") is not None:
        import capo_compute_optimizer_automation.types.enrollment_status

        out["status"] = (
            capo_compute_optimizer_automation.types.enrollment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus",
            "",
        )
    if data.get("organizationRuleMode") is not None:
        import capo_compute_optimizer_automation.types.organization_rule_mode

        out["organization_rule_mode"] = (
            capo_compute_optimizer_automation.types.organization_rule_mode.deserialize_aws_json_1_0(
                data["organizationRuleMode"]
            )
        )
    else:
        import typing

        out["organization_rule_mode"] = typing.cast(
            "capo_compute_optimizer_automation.types.organization_rule_mode.OrganizationRuleMode",
            "",
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    else:
        import datetime

        out["last_updated_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
