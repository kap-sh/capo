"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#BatchGetEventErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.batch_get_event_error

BatchGetEventErrorList: TypeAlias = list[
    "capo_opensearchmemory.types.batch_get_event_error.BatchGetEventError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetEventErrorList) -> list:
    import capo_opensearchmemory.types.batch_get_event_error

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.batch_get_event_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchGetEventErrorList:
    import capo_opensearchmemory.types.batch_get_event_error

    out: BatchGetEventErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.batch_get_event_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
