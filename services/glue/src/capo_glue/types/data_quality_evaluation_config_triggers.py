"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigTriggers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_config_trigger

DataQualityEvaluationConfigTriggers: TypeAlias = list[
    "capo_glue.types.data_quality_evaluation_config_trigger.DataQualityEvaluationConfigTrigger"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigTriggers) -> list:
    import capo_glue.types.data_quality_evaluation_config_trigger

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_evaluation_config_trigger.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityEvaluationConfigTriggers:
    import capo_glue.types.data_quality_evaluation_config_trigger

    out: DataQualityEvaluationConfigTriggers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.data_quality_evaluation_config_trigger.deserialize_aws_json_1_1(
                item
            )
        )
    return out
