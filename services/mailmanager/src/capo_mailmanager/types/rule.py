"""Generated from Smithy shape ``com.amazonaws.mailmanager#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_actions
    import capo_mailmanager.types.rule_conditions
    import capo_mailmanager.types.rule_name


class Rule(TypedDict, closed=True):
    name: NotRequired["capo_mailmanager.types.rule_name.RuleName"]
    """<p>The user-friendly name of the rule.</p>"""
    conditions: NotRequired["capo_mailmanager.types.rule_conditions.RuleConditions"]
    """<p>The conditions of this rule. All conditions must match the email for the actions to be executed. An empty list of conditions means that all emails match, but are still subject to any "unless conditions"</p>"""
    unless: NotRequired["capo_mailmanager.types.rule_conditions.RuleConditions"]
    """<p>The "unless conditions" of this rule. None of the conditions can match the email for the actions to be executed. If any of these conditions do match the email, then the actions are not executed.</p>"""
    actions: "capo_mailmanager.types.rule_actions.RuleActions"
    """<p>The list of actions to execute when the conditions match the incoming email, and none of the "unless conditions" match.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Rule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "conditions" in value:
        import capo_mailmanager.types.rule_conditions

        out["Conditions"] = (
            capo_mailmanager.types.rule_conditions.serialize_aws_json_1_0(
                value["conditions"]
            )
        )
    if "unless" in value:
        import capo_mailmanager.types.rule_conditions

        out["Unless"] = capo_mailmanager.types.rule_conditions.serialize_aws_json_1_0(
            value["unless"]
        )
    import capo_mailmanager.types.rule_actions

    out["Actions"] = capo_mailmanager.types.rule_actions.serialize_aws_json_1_0(
        value["actions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Conditions") is not None:
        import capo_mailmanager.types.rule_conditions

        out["conditions"] = (
            capo_mailmanager.types.rule_conditions.deserialize_aws_json_1_0(
                data["Conditions"]
            )
        )
    if data.get("Unless") is not None:
        import capo_mailmanager.types.rule_conditions

        out["unless"] = capo_mailmanager.types.rule_conditions.deserialize_aws_json_1_0(
            data["Unless"]
        )
    if data.get("Actions") is not None:
        import capo_mailmanager.types.rule_actions

        out["actions"] = capo_mailmanager.types.rule_actions.deserialize_aws_json_1_0(
            data["Actions"]
        )
    else:
        raise DeserializationError("Rule.actions required")
    return out
