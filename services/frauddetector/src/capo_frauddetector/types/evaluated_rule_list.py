"""Generated from Smithy shape ``com.amazonaws.frauddetector#EvaluatedRuleList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.evaluated_rule

EvaluatedRuleList: TypeAlias = list[
    "capo_frauddetector.types.evaluated_rule.EvaluatedRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatedRuleList) -> list:
    import capo_frauddetector.types.evaluated_rule

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.evaluated_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EvaluatedRuleList:
    import capo_frauddetector.types.evaluated_rule

    out: EvaluatedRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_frauddetector.types.evaluated_rule.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: EvaluatedRuleList) -> list[Any]:
    import capo_frauddetector.types.evaluated_rule

    return [
        capo_frauddetector.types.evaluated_rule.redact_sensitive(item) for item in value
    ]
