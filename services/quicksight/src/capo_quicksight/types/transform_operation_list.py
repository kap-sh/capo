"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformOperationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.transform_operation

TransformOperationList: TypeAlias = list[
    "capo_quicksight.types.transform_operation.TransformOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransformOperationList) -> list:
    import capo_quicksight.types.transform_operation

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.transform_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> TransformOperationList:
    import capo_quicksight.types.transform_operation

    out: TransformOperationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.transform_operation.deserialize_json(item))
    return out


def redact_sensitive(value: TransformOperationList) -> list[Any]:
    import capo_quicksight.types.transform_operation

    return [
        capo_quicksight.types.transform_operation.redact_sensitive(item)
        for item in value
    ]
