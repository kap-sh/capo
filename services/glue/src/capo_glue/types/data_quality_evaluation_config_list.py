"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_config_list_details

DataQualityEvaluationConfigList: TypeAlias = list[
    "capo_glue.types.data_quality_evaluation_config_list_details.DataQualityEvaluationConfigListDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigList) -> list:
    import capo_glue.types.data_quality_evaluation_config_list_details

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_evaluation_config_list_details.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityEvaluationConfigList:
    import capo_glue.types.data_quality_evaluation_config_list_details

    out: DataQualityEvaluationConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.data_quality_evaluation_config_list_details.deserialize_aws_json_1_1(
                item
            )
        )
    return out
