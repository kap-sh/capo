"""Generated from Smithy shape ``com.amazonaws.workdocs#ResponseItemsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.response_item

ResponseItemsList: TypeAlias = list["capo_workdocs.types.response_item.ResponseItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseItemsList) -> list:
    import capo_workdocs.types.response_item

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.response_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResponseItemsList:
    import capo_workdocs.types.response_item

    out: ResponseItemsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.response_item.deserialize_json(item))
    return out


def redact_sensitive(value: ResponseItemsList) -> list[Any]:
    import capo_workdocs.types.response_item

    return [capo_workdocs.types.response_item.redact_sensitive(item) for item in value]
