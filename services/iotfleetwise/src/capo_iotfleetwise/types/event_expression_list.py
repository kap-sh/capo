"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#EventExpressionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.action_event_expression

EventExpressionList: TypeAlias = list[
    "capo_iotfleetwise.types.action_event_expression.actionEventExpression"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventExpressionList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> EventExpressionList:
    return [item for item in data if item is not None]


def redact_sensitive(value: EventExpressionList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
