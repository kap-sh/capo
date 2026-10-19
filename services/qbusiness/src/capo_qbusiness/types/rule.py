"""Generated from Smithy shape ``com.amazonaws.qbusiness#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.rule_configuration
    import capo_qbusiness.types.rule_type
    import capo_qbusiness.types.users_and_groups


class Rule(TypedDict, closed=True):
    included_users_and_groups: NotRequired[
        "capo_qbusiness.types.users_and_groups.UsersAndGroups"
    ]
    """<p>Users and groups to be included in a rule.</p>"""
    excluded_users_and_groups: NotRequired[
        "capo_qbusiness.types.users_and_groups.UsersAndGroups"
    ]
    """<p>Users and groups to be excluded from a rule.</p>"""
    rule_type: "capo_qbusiness.types.rule_type.RuleType"
    """<p>The type of rule.</p>"""
    rule_configuration: NotRequired[
        "capo_qbusiness.types.rule_configuration.RuleConfiguration"
    ]
    """<p>The configuration information for a rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    if "included_users_and_groups" in value:
        import capo_qbusiness.types.users_and_groups

        out["includedUsersAndGroups"] = (
            capo_qbusiness.types.users_and_groups.serialize_json(
                value["included_users_and_groups"]
            )
        )
    if "excluded_users_and_groups" in value:
        import capo_qbusiness.types.users_and_groups

        out["excludedUsersAndGroups"] = (
            capo_qbusiness.types.users_and_groups.serialize_json(
                value["excluded_users_and_groups"]
            )
        )
    import capo_qbusiness.types.rule_type

    out["ruleType"] = capo_qbusiness.types.rule_type.serialize_json(value["rule_type"])
    if "rule_configuration" in value:
        import capo_qbusiness.types.rule_configuration

        out["ruleConfiguration"] = (
            capo_qbusiness.types.rule_configuration.serialize_json(
                value["rule_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("includedUsersAndGroups") is not None:
        import capo_qbusiness.types.users_and_groups

        out["included_users_and_groups"] = (
            capo_qbusiness.types.users_and_groups.deserialize_json(
                data["includedUsersAndGroups"]
            )
        )
    if data.get("excludedUsersAndGroups") is not None:
        import capo_qbusiness.types.users_and_groups

        out["excluded_users_and_groups"] = (
            capo_qbusiness.types.users_and_groups.deserialize_json(
                data["excludedUsersAndGroups"]
            )
        )
    if data.get("ruleType") is not None:
        import capo_qbusiness.types.rule_type

        out["rule_type"] = capo_qbusiness.types.rule_type.deserialize_json(
            data["ruleType"]
        )
    else:
        import typing

        out["rule_type"] = typing.cast("capo_qbusiness.types.rule_type.RuleType", "")
    if data.get("ruleConfiguration") is not None:
        import capo_qbusiness.types.rule_configuration

        out["rule_configuration"] = (
            capo_qbusiness.types.rule_configuration.deserialize_json(
                data["ruleConfiguration"]
            )
        )
    return out
