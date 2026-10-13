"""Generated from Smithy shape ``com.amazonaws.frauddetector#RuleDetailList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.rule_detail

RuleDetailList: TypeAlias = list["capo_frauddetector.types.rule_detail.RuleDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleDetailList) -> list:
    import capo_frauddetector.types.rule_detail

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.rule_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleDetailList:
    import capo_frauddetector.types.rule_detail

    out: RuleDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_frauddetector.types.rule_detail.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: RuleDetailList) -> list[Any]:
    import capo_frauddetector.types.rule_detail

    return [
        capo_frauddetector.types.rule_detail.redact_sensitive(item) for item in value
    ]
