"""Generated from Smithy shape ``com.amazonaws.finspacedata#DatasetList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.dataset

DatasetList: TypeAlias = list["capo_finspace_data.types.dataset.Dataset"]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetList) -> list:
    import capo_finspace_data.types.dataset

    out: list = []
    for item in value:
        out.append(capo_finspace_data.types.dataset.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasetList:
    import capo_finspace_data.types.dataset

    out: DatasetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_finspace_data.types.dataset.deserialize_json(item))
    return out


def redact_sensitive(value: DatasetList) -> list[Any]:
    import capo_finspace_data.types.dataset

    return [capo_finspace_data.types.dataset.redact_sensitive(item) for item in value]
