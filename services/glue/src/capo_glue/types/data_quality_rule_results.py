"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleResults``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_rule_result

DataQualityRuleResults: TypeAlias = list[
    "capo_glue.types.data_quality_rule_result.DataQualityRuleResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleResults) -> list:
    import capo_glue.types.data_quality_rule_result

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_rule_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityRuleResults:
    import capo_glue.types.data_quality_rule_result

    out: DataQualityRuleResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.data_quality_rule_result.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: DataQualityRuleResults) -> list[Any]:
    import capo_glue.types.data_quality_rule_result

    return [
        capo_glue.types.data_quality_rule_result.redact_sensitive(item)
        for item in value
    ]
