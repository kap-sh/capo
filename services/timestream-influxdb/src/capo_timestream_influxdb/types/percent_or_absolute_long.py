"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#PercentOrAbsoluteLong``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_timestream_influxdb.errors import DeserializationError, SerializationError
from capo_timestream_influxdb.types._unknown import UnknownUnionMember


class _PercentOrAbsoluteLong_percent(TypedDict, closed=True):
    percent: "str"


class _PercentOrAbsoluteLong_absolute(TypedDict, closed=True):
    absolute: "int"


PercentOrAbsoluteLong: TypeAlias = (
    _PercentOrAbsoluteLong_percent
    | _PercentOrAbsoluteLong_absolute
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PercentOrAbsoluteLong) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PercentOrAbsoluteLong: cannot serialize unknown variant {value.name!r}"
        )
    elif "percent" in value:
        return {"percent": value["percent"]}
    elif "absolute" in value:
        return {"absolute": value["absolute"]}
    else:
        raise SerializationError("PercentOrAbsoluteLong: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PercentOrAbsoluteLong:
    if data.get("percent") is not None:
        return {"percent": data["percent"]}
    elif data.get("absolute") is not None:
        return {"absolute": data["absolute"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PercentOrAbsoluteLong: no recognized variant key")
