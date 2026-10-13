"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleConditions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_condition

RuleConditions: TypeAlias = list["capo_mailmanager.types.rule_condition.RuleCondition"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleConditions) -> list:
    import capo_mailmanager.types.rule_condition

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.rule_condition.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RuleConditions:
    import capo_mailmanager.types.rule_condition

    out: RuleConditions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.rule_condition.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: RuleConditions) -> list[Any]:
    import capo_mailmanager.types.rule_condition

    return [
        capo_mailmanager.types.rule_condition.redact_sensitive(item) for item in value
    ]
