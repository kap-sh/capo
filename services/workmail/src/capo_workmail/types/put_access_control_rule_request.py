"""Generated from Smithy shape ``com.amazonaws.workmail#PutAccessControlRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.access_control_rule_description
    import capo_workmail.types.access_control_rule_effect
    import capo_workmail.types.access_control_rule_name
    import capo_workmail.types.actions_list
    import capo_workmail.types.impersonation_role_id_list
    import capo_workmail.types.ip_range_list
    import capo_workmail.types.organization_id
    import capo_workmail.types.user_id_list


class PutAccessControlRuleRequest(TypedDict, closed=True):
    name: "capo_workmail.types.access_control_rule_name.AccessControlRuleName"
    """<p>The rule name.</p>"""
    effect: "capo_workmail.types.access_control_rule_effect.AccessControlRuleEffect"
    """<p>The rule effect.</p>"""
    description: "capo_workmail.types.access_control_rule_description.AccessControlRuleDescription"
    """<p>The rule description.</p>"""
    ip_ranges: NotRequired["capo_workmail.types.ip_range_list.IpRangeList"]
    """<p>IPv4 CIDR ranges to include in the rule.</p>"""
    not_ip_ranges: NotRequired["capo_workmail.types.ip_range_list.IpRangeList"]
    """<p>IPv4 CIDR ranges to exclude from the rule.</p>"""
    actions: NotRequired["capo_workmail.types.actions_list.ActionsList"]
    """<p>Access protocol actions to include in the rule. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>"""
    not_actions: NotRequired["capo_workmail.types.actions_list.ActionsList"]
    """<p>Access protocol actions to exclude from the rule. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>"""
    user_ids: NotRequired["capo_workmail.types.user_id_list.UserIdList"]
    """<p>User IDs to include in the rule.</p>"""
    not_user_ids: NotRequired["capo_workmail.types.user_id_list.UserIdList"]
    """<p>User IDs to exclude from the rule.</p>"""
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier of the organization.</p>"""
    impersonation_role_ids: NotRequired[
        "capo_workmail.types.impersonation_role_id_list.ImpersonationRoleIdList"
    ]
    """<p>Impersonation role IDs to include in the rule.</p>"""
    not_impersonation_role_ids: NotRequired[
        "capo_workmail.types.impersonation_role_id_list.ImpersonationRoleIdList"
    ]
    """<p>Impersonation role IDs to exclude from the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAccessControlRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_workmail.types.access_control_rule_effect

    out["Effect"] = (
        capo_workmail.types.access_control_rule_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    out["Description"] = value["description"]
    if "ip_ranges" in value:
        import capo_workmail.types.ip_range_list

        out["IpRanges"] = capo_workmail.types.ip_range_list.serialize_aws_json_1_1(
            value["ip_ranges"]
        )
    if "not_ip_ranges" in value:
        import capo_workmail.types.ip_range_list

        out["NotIpRanges"] = capo_workmail.types.ip_range_list.serialize_aws_json_1_1(
            value["not_ip_ranges"]
        )
    if "actions" in value:
        import capo_workmail.types.actions_list

        out["Actions"] = capo_workmail.types.actions_list.serialize_aws_json_1_1(
            value["actions"]
        )
    if "not_actions" in value:
        import capo_workmail.types.actions_list

        out["NotActions"] = capo_workmail.types.actions_list.serialize_aws_json_1_1(
            value["not_actions"]
        )
    if "user_ids" in value:
        import capo_workmail.types.user_id_list

        out["UserIds"] = capo_workmail.types.user_id_list.serialize_aws_json_1_1(
            value["user_ids"]
        )
    if "not_user_ids" in value:
        import capo_workmail.types.user_id_list

        out["NotUserIds"] = capo_workmail.types.user_id_list.serialize_aws_json_1_1(
            value["not_user_ids"]
        )
    out["OrganizationId"] = value["organization_id"]
    if "impersonation_role_ids" in value:
        import capo_workmail.types.impersonation_role_id_list

        out["ImpersonationRoleIds"] = (
            capo_workmail.types.impersonation_role_id_list.serialize_aws_json_1_1(
                value["impersonation_role_ids"]
            )
        )
    if "not_impersonation_role_ids" in value:
        import capo_workmail.types.impersonation_role_id_list

        out["NotImpersonationRoleIds"] = (
            capo_workmail.types.impersonation_role_id_list.serialize_aws_json_1_1(
                value["not_impersonation_role_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAccessControlRuleRequest:
    out: PutAccessControlRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Effect") is not None:
        import capo_workmail.types.access_control_rule_effect

        out["effect"] = (
            capo_workmail.types.access_control_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    else:
        import typing

        out["effect"] = typing.cast(
            "capo_workmail.types.access_control_rule_effect.AccessControlRuleEffect", ""
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("IpRanges") is not None:
        import capo_workmail.types.ip_range_list

        out["ip_ranges"] = capo_workmail.types.ip_range_list.deserialize_aws_json_1_1(
            data["IpRanges"]
        )
    if data.get("NotIpRanges") is not None:
        import capo_workmail.types.ip_range_list

        out["not_ip_ranges"] = (
            capo_workmail.types.ip_range_list.deserialize_aws_json_1_1(
                data["NotIpRanges"]
            )
        )
    if data.get("Actions") is not None:
        import capo_workmail.types.actions_list

        out["actions"] = capo_workmail.types.actions_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    if data.get("NotActions") is not None:
        import capo_workmail.types.actions_list

        out["not_actions"] = capo_workmail.types.actions_list.deserialize_aws_json_1_1(
            data["NotActions"]
        )
    if data.get("UserIds") is not None:
        import capo_workmail.types.user_id_list

        out["user_ids"] = capo_workmail.types.user_id_list.deserialize_aws_json_1_1(
            data["UserIds"]
        )
    if data.get("NotUserIds") is not None:
        import capo_workmail.types.user_id_list

        out["not_user_ids"] = capo_workmail.types.user_id_list.deserialize_aws_json_1_1(
            data["NotUserIds"]
        )
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("ImpersonationRoleIds") is not None:
        import capo_workmail.types.impersonation_role_id_list

        out["impersonation_role_ids"] = (
            capo_workmail.types.impersonation_role_id_list.deserialize_aws_json_1_1(
                data["ImpersonationRoleIds"]
            )
        )
    if data.get("NotImpersonationRoleIds") is not None:
        import capo_workmail.types.impersonation_role_id_list

        out["not_impersonation_role_ids"] = (
            capo_workmail.types.impersonation_role_id_list.deserialize_aws_json_1_1(
                data["NotImpersonationRoleIds"]
            )
        )
    return out
