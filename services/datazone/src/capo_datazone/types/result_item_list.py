"""Generated from Smithy shape ``com.amazonaws.datazone#ResultItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.result_item

ResultItemList: TypeAlias = list["capo_datazone.types.result_item.ResultItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ResultItemList) -> list:
    import capo_datazone.types.result_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResultItemList:
    import capo_datazone.types.result_item

    out: ResultItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.result_item.deserialize_json(item))
    return out


def redact_sensitive(value: ResultItemList) -> list[Any]:
    import capo_datazone.types.result_item

    return [capo_datazone.types.result_item.redact_sensitive(item) for item in value]
