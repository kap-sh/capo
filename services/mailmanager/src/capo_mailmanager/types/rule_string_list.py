"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_string_value

RuleStringList: TypeAlias = list[
    "capo_mailmanager.types.rule_string_value.RuleStringValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStringList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RuleStringList:
    return [item for item in data if item is not None]


def redact_sensitive(value: RuleStringList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
