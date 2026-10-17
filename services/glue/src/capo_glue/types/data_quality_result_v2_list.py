"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultV2List``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_result_v2_item

DataQualityResultV2List: TypeAlias = list[
    "capo_glue.types.data_quality_result_v2_item.DataQualityResultV2Item"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultV2List) -> list:
    import capo_glue.types.data_quality_result_v2_item

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_result_v2_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityResultV2List:
    import capo_glue.types.data_quality_result_v2_item

    out: DataQualityResultV2List = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.data_quality_result_v2_item.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: DataQualityResultV2List) -> list[Any]:
    import capo_glue.types.data_quality_result_v2_item

    return [
        capo_glue.types.data_quality_result_v2_item.redact_sensitive(item)
        for item in value
    ]
