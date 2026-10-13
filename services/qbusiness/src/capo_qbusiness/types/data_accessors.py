"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessors``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessor

DataAccessors: TypeAlias = list["capo_qbusiness.types.data_accessor.DataAccessor"]


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessors) -> list:
    import capo_qbusiness.types.data_accessor

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.data_accessor.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataAccessors:
    import capo_qbusiness.types.data_accessor

    out: DataAccessors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qbusiness.types.data_accessor.deserialize_json(item))
    return out


def redact_sensitive(value: DataAccessors) -> list[Any]:
    import capo_qbusiness.types.data_accessor

    return [capo_qbusiness.types.data_accessor.redact_sensitive(item) for item in value]
