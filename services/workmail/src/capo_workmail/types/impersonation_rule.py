"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.access_effect
    import capo_workmail.types.impersonation_rule_description
    import capo_workmail.types.impersonation_rule_id
    import capo_workmail.types.impersonation_rule_name
    import capo_workmail.types.target_users


class ImpersonationRule(TypedDict, closed=True):
    impersonation_rule_id: (
        "capo_workmail.types.impersonation_rule_id.ImpersonationRuleId"
    )
    """<p>The identifier of the rule.</p>"""
    name: NotRequired[
        "capo_workmail.types.impersonation_rule_name.ImpersonationRuleName"
    ]
    """<p>The rule name.</p>"""
    description: NotRequired[
        "capo_workmail.types.impersonation_rule_description.ImpersonationRuleDescription"
    ]
    """<p>The rule description.</p>"""
    effect: "capo_workmail.types.access_effect.AccessEffect"
    """<p>The effect of the rule when it matches the input. Allowed effect values are <code>ALLOW</code> or <code>DENY</code>.</p>"""
    target_users: NotRequired["capo_workmail.types.target_users.TargetUsers"]
    """<p>A list of user IDs that match the rule.</p>"""
    not_target_users: NotRequired["capo_workmail.types.target_users.TargetUsers"]
    """<p>A list of user IDs that don't match the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRule) -> dict:
    out: dict = {}
    out["ImpersonationRuleId"] = value["impersonation_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_workmail.types.access_effect

    out["Effect"] = capo_workmail.types.access_effect.serialize_aws_json_1_1(
        value["effect"]
    )
    if "target_users" in value:
        import capo_workmail.types.target_users

        out["TargetUsers"] = capo_workmail.types.target_users.serialize_aws_json_1_1(
            value["target_users"]
        )
    if "not_target_users" in value:
        import capo_workmail.types.target_users

        out["NotTargetUsers"] = capo_workmail.types.target_users.serialize_aws_json_1_1(
            value["not_target_users"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImpersonationRule:
    out: ImpersonationRule = {}  # type: ignore[typeddict-item]
    if data.get("ImpersonationRuleId") is not None:
        out["impersonation_rule_id"] = data["ImpersonationRuleId"]
    else:
        out["impersonation_rule_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Effect") is not None:
        import capo_workmail.types.access_effect

        out["effect"] = capo_workmail.types.access_effect.deserialize_aws_json_1_1(
            data["Effect"]
        )
    else:
        import typing

        out["effect"] = typing.cast(
            "capo_workmail.types.access_effect.AccessEffect", ""
        )
    if data.get("TargetUsers") is not None:
        import capo_workmail.types.target_users

        out["target_users"] = capo_workmail.types.target_users.deserialize_aws_json_1_1(
            data["TargetUsers"]
        )
    if data.get("NotTargetUsers") is not None:
        import capo_workmail.types.target_users

        out["not_target_users"] = (
            capo_workmail.types.target_users.deserialize_aws_json_1_1(
                data["NotTargetUsers"]
            )
        )
    return out
