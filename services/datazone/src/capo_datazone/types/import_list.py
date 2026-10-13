"""Generated from Smithy shape ``com.amazonaws.datazone#ImportList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.import_

ImportList: TypeAlias = list["capo_datazone.types.import_.Import"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportList) -> list:
    import capo_datazone.types.import_

    out: list = []
    for item in value:
        out.append(capo_datazone.types.import_.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportList:
    import capo_datazone.types.import_

    out: ImportList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.import_.deserialize_json(item))
    return out


def redact_sensitive(value: ImportList) -> list[Any]:
    import capo_datazone.types.import_

    return [capo_datazone.types.import_.redact_sensitive(item) for item in value]
