"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftStorageProperties``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember


class _RedshiftStorageProperties_clusterName(TypedDict, closed=True):
    clusterName: "str"


class _RedshiftStorageProperties_workgroupName(TypedDict, closed=True):
    workgroupName: "str"


RedshiftStorageProperties: TypeAlias = (
    _RedshiftStorageProperties_clusterName
    | _RedshiftStorageProperties_workgroupName
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftStorageProperties) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RedshiftStorageProperties: cannot serialize unknown variant {value.name!r}"
        )
    elif "clusterName" in value:
        return {"clusterName": value["clusterName"]}
    elif "workgroupName" in value:
        return {"workgroupName": value["workgroupName"]}
    else:
        raise SerializationError("RedshiftStorageProperties: no variant present")


def deserialize_json(data: dict) -> RedshiftStorageProperties:
    if data.get("clusterName") is not None:
        return {"clusterName": data["clusterName"]}
    elif data.get("workgroupName") is not None:
        return {"workgroupName": data["workgroupName"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "RedshiftStorageProperties: no recognized variant key"
        )
