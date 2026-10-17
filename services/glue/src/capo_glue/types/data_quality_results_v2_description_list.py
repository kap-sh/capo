"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultsV2DescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_results_v2_description

DataQualityResultsV2DescriptionList: TypeAlias = list[
    "capo_glue.types.data_quality_results_v2_description.DataQualityResultsV2Description"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultsV2DescriptionList) -> list:
    import capo_glue.types.data_quality_results_v2_description

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_results_v2_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityResultsV2DescriptionList:
    import capo_glue.types.data_quality_results_v2_description

    out: DataQualityResultsV2DescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.data_quality_results_v2_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
