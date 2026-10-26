"""Generated from Smithy shape ``com.amazonaws.rdsdata#ArrayValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_rds_data.errors import DeserializationError, SerializationError
from capo_rds_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_rds_data.types.array_of_array
    import capo_rds_data.types.boolean_array
    import capo_rds_data.types.double_array
    import capo_rds_data.types.long_array
    import capo_rds_data.types.string_array


class _ArrayValue_booleanValues(TypedDict, closed=True):
    booleanValues: "capo_rds_data.types.boolean_array.BooleanArray"


class _ArrayValue_longValues(TypedDict, closed=True):
    longValues: "capo_rds_data.types.long_array.LongArray"


class _ArrayValue_doubleValues(TypedDict, closed=True):
    doubleValues: "capo_rds_data.types.double_array.DoubleArray"


class _ArrayValue_stringValues(TypedDict, closed=True):
    stringValues: "capo_rds_data.types.string_array.StringArray"


class _ArrayValue_arrayValues(TypedDict, closed=True):
    arrayValues: "capo_rds_data.types.array_of_array.ArrayOfArray"


ArrayValue: TypeAlias = (
    _ArrayValue_booleanValues
    | _ArrayValue_longValues
    | _ArrayValue_doubleValues
    | _ArrayValue_stringValues
    | _ArrayValue_arrayValues
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ArrayValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ArrayValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "booleanValues" in value:
        import capo_rds_data.types.boolean_array

        return {
            "booleanValues": capo_rds_data.types.boolean_array.serialize_json(
                value["booleanValues"]
            )
        }
    elif "longValues" in value:
        import capo_rds_data.types.long_array

        return {
            "longValues": capo_rds_data.types.long_array.serialize_json(
                value["longValues"]
            )
        }
    elif "doubleValues" in value:
        import capo_rds_data.types.double_array

        return {
            "doubleValues": capo_rds_data.types.double_array.serialize_json(
                value["doubleValues"]
            )
        }
    elif "stringValues" in value:
        import capo_rds_data.types.string_array

        return {
            "stringValues": capo_rds_data.types.string_array.serialize_json(
                value["stringValues"]
            )
        }
    elif "arrayValues" in value:
        import capo_rds_data.types.array_of_array

        return {
            "arrayValues": capo_rds_data.types.array_of_array.serialize_json(
                value["arrayValues"]
            )
        }
    else:
        raise SerializationError("ArrayValue: no variant present")


def deserialize_json(data: dict) -> ArrayValue:
    if data.get("booleanValues") is not None:
        import capo_rds_data.types.boolean_array

        return {
            "booleanValues": capo_rds_data.types.boolean_array.deserialize_json(
                data["booleanValues"]
            )
        }
    elif data.get("longValues") is not None:
        import capo_rds_data.types.long_array

        return {
            "longValues": capo_rds_data.types.long_array.deserialize_json(
                data["longValues"]
            )
        }
    elif data.get("doubleValues") is not None:
        import capo_rds_data.types.double_array

        return {
            "doubleValues": capo_rds_data.types.double_array.deserialize_json(
                data["doubleValues"]
            )
        }
    elif data.get("stringValues") is not None:
        import capo_rds_data.types.string_array

        return {
            "stringValues": capo_rds_data.types.string_array.deserialize_json(
                data["stringValues"]
            )
        }
    elif data.get("arrayValues") is not None:
        import capo_rds_data.types.array_of_array

        return {
            "arrayValues": capo_rds_data.types.array_of_array.deserialize_json(
                data["arrayValues"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ArrayValue: no recognized variant key")
