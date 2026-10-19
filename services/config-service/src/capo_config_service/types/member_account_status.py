"""Generated from Smithy shape ``com.amazonaws.configservice#MemberAccountStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.date
    import capo_config_service.types.member_account_rule_status
    import capo_config_service.types.string
    import capo_config_service.types.string_with_char_limit64


class MemberAccountStatus(TypedDict, closed=True):
    account_id: "capo_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of a member account.</p>"""
    config_rule_name: (
        "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64"
    )
    """<p>The name of Config rule deployed in the member account.</p>"""
    member_account_rule_status: (
        "capo_config_service.types.member_account_rule_status.MemberAccountRuleStatus"
    )
    """<p>Indicates deployment status for Config rule in the member account. When management account calls <code>PutOrganizationConfigRule</code> action for the first time, Config rule status is created in the member account. When management account calls <code>PutOrganizationConfigRule</code> action for the second time, Config rule status is updated in the member account. Config rule status is deleted when the management account deletes <code>OrganizationConfigRule</code> and disables service access for <code>config-multiaccountsetup.amazonaws.com</code>. </p> <p> Config sets the state of the rule to:</p> <ul> <li> <p> <code>CREATE_SUCCESSFUL</code> when Config rule has been created in the member account. </p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> when Config rule is being created in the member account.</p> </li> <li> <p> <code>CREATE_FAILED</code> when Config rule creation has failed in the member account.</p> </li> <li> <p> <code>DELETE_FAILED</code> when Config rule deletion has failed in the member account.</p> </li> <li> <p> <code>DELETE_IN_PROGRESS</code> when Config rule is being deleted in the member account.</p> </li> <li> <p> <code>DELETE_SUCCESSFUL</code> when Config rule has been deleted in the member account. </p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> when Config rule has been updated in the member account.</p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> when Config rule is being updated in the member account.</p> </li> <li> <p> <code>UPDATE_FAILED</code> when Config rule deletion has failed in the member account.</p> </li> </ul>"""
    error_code: NotRequired["capo_config_service.types.string.String"]
    """<p>An error code that is returned when Config rule creation or deletion failed in the member account.</p>"""
    error_message: NotRequired["capo_config_service.types.string.String"]
    """<p>An error message indicating that Config rule account creation or deletion has failed due to an error in the member account.</p>"""
    last_update_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The timestamp of the last status update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberAccountStatus) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["ConfigRuleName"] = value["config_rule_name"]
    import capo_config_service.types.member_account_rule_status

    out["MemberAccountRuleStatus"] = (
        capo_config_service.types.member_account_rule_status.serialize_aws_json_1_1(
            value["member_account_rule_status"]
        )
    )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "last_update_time" in value:
        import capo_config_service.types.date

        out["LastUpdateTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["last_update_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MemberAccountStatus:
    out: MemberAccountStatus = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("MemberAccountRuleStatus") is not None:
        import capo_config_service.types.member_account_rule_status

        out["member_account_rule_status"] = (
            capo_config_service.types.member_account_rule_status.deserialize_aws_json_1_1(
                data["MemberAccountRuleStatus"]
            )
        )
    else:
        import typing

        out["member_account_rule_status"] = typing.cast(
            "capo_config_service.types.member_account_rule_status.MemberAccountRuleStatus",
            "",
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("LastUpdateTime") is not None:
        import capo_config_service.types.date

        out["last_update_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    return out
