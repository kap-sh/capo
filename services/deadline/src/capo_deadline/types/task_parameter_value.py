"""Generated from Smithy shape ``com.amazonaws.deadline#TaskParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.float_string
    import capo_deadline.types.int_string
    import capo_deadline.types.parameter_string
    import capo_deadline.types.path_string
    import capo_deadline.types.string


class _TaskParameterValue_int(TypedDict, closed=True):
    int: "capo_deadline.types.int_string.IntString"


class _TaskParameterValue_float(TypedDict, closed=True):
    float: "capo_deadline.types.float_string.FloatString"


class _TaskParameterValue_string(TypedDict, closed=True):
    string: "capo_deadline.types.parameter_string.ParameterString"


class _TaskParameterValue_path(TypedDict, closed=True):
    path: "capo_deadline.types.path_string.PathString"


class _TaskParameterValue_chunkInt(TypedDict, closed=True):
    chunkInt: "capo_deadline.types.string.String"


TaskParameterValue: TypeAlias = (
    _TaskParameterValue_int
    | _TaskParameterValue_float
    | _TaskParameterValue_string
    | _TaskParameterValue_path
    | _TaskParameterValue_chunkInt
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TaskParameterValue) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TaskParameterValue: cannot serialize unknown variant {value.name!r}"
        )
    elif "int" in value:
        return {"int": value["int"]}
    elif "float" in value:
        return {"float": value["float"]}
    elif "string" in value:
        return {"string": value["string"]}
    elif "path" in value:
        return {"path": value["path"]}
    elif "chunkInt" in value:
        return {"chunkInt": value["chunkInt"]}
    else:
        raise SerializationError("TaskParameterValue: no variant present")


def deserialize_json(data: dict) -> TaskParameterValue:
    if data.get("int") is not None:
        return {"int": data["int"]}
    elif data.get("float") is not None:
        return {"float": data["float"]}
    elif data.get("string") is not None:
        return {"string": data["string"]}
    elif data.get("path") is not None:
        return {"path": data["path"]}
    elif data.get("chunkInt") is not None:
        return {"chunkInt": data["chunkInt"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("TaskParameterValue: no recognized variant key")
