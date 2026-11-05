"""Generated from Smithy shape ``com.amazonaws.dynamodb#OutputTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.output_type_enum

OutputTypeList: TypeAlias = list["capo_dynamodb.types.output_type_enum.OutputTypeEnum"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputTypeList) -> list:
    import capo_dynamodb.types.output_type_enum

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.output_type_enum.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> OutputTypeList:
    import capo_dynamodb.types.output_type_enum

    out: OutputTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dynamodb.types.output_type_enum.deserialize_aws_json_1_0(item))
    return out
