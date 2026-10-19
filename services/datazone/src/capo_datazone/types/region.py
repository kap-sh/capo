"""Generated from Smithy shape ``com.amazonaws.datazone#Region``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.parameter_store_path
    import capo_datazone.types.region_name


class _Region_regionName(TypedDict, closed=True):
    regionName: "capo_datazone.types.region_name.RegionName"


class _Region_regionNamePath(TypedDict, closed=True):
    regionNamePath: "capo_datazone.types.parameter_store_path.ParameterStorePath"


Region: TypeAlias = _Region_regionName | _Region_regionNamePath | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Region) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Region: cannot serialize unknown variant {value.name!r}"
        )
    elif "regionName" in value:
        return {"regionName": value["regionName"]}
    elif "regionNamePath" in value:
        return {"regionNamePath": value["regionNamePath"]}
    else:
        raise SerializationError("Region: no variant present")


def deserialize_json(data: dict) -> Region:
    if data.get("regionName") is not None:
        return {"regionName": data["regionName"]}
    elif data.get("regionNamePath") is not None:
        return {"regionNamePath": data["regionNamePath"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Region: no recognized variant key")
