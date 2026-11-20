"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ValidationExceptionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.validation_exception_field

ValidationExceptionFieldList: TypeAlias = list[
    "capo_opensearchmemory.types.validation_exception_field.ValidationExceptionField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionFieldList) -> list:
    import capo_opensearchmemory.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.validation_exception_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ValidationExceptionFieldList:
    import capo_opensearchmemory.types.validation_exception_field

    out: ValidationExceptionFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.validation_exception_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
