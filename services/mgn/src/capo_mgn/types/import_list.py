"""Generated from Smithy shape ``com.amazonaws.mgn#ImportList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.import_task

ImportList: TypeAlias = list["capo_mgn.types.import_task.ImportTask"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportList) -> list:
    import capo_mgn.types.import_task

    out: list = []
    for item in value:
        out.append(capo_mgn.types.import_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportList:
    import capo_mgn.types.import_task

    out: ImportList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.import_task.deserialize_json(item))
    return out


def redact_sensitive(value: ImportList) -> list[Any]:
    import capo_mgn.types.import_task

    return [capo_mgn.types.import_task.redact_sensitive(item) for item in value]
