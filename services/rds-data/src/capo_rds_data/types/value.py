"""Generated from Smithy shape ``com.amazonaws.rdsdata#Value``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_rds_data.errors import DeserializationError, SerializationError
from capo_rds_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_rds_data.types.array_value_list
    import capo_rds_data.types.blob
    import capo_rds_data.types.boxed_boolean
    import capo_rds_data.types.boxed_double
    import capo_rds_data.types.boxed_float
    import capo_rds_data.types.boxed_integer
    import capo_rds_data.types.boxed_long
    import capo_rds_data.types.string
    import capo_rds_data.types.struct_value


class ValueIsNullMember(TypedDict, closed=True):
    isNull: "capo_rds_data.types.boxed_boolean.BoxedBoolean"


class ValueBitValueMember(TypedDict, closed=True):
    bitValue: "capo_rds_data.types.boxed_boolean.BoxedBoolean"


class ValueBigIntValueMember(TypedDict, closed=True):
    bigIntValue: "capo_rds_data.types.boxed_long.BoxedLong"


class ValueIntValueMember(TypedDict, closed=True):
    intValue: "capo_rds_data.types.boxed_integer.BoxedInteger"


class ValueDoubleValueMember(TypedDict, closed=True):
    doubleValue: "capo_rds_data.types.boxed_double.BoxedDouble"


class ValueRealValueMember(TypedDict, closed=True):
    realValue: "capo_rds_data.types.boxed_float.BoxedFloat"


class ValueStringValueMember(TypedDict, closed=True):
    stringValue: "capo_rds_data.types.string.String"


class ValueBlobValueMember(TypedDict, closed=True):
    blobValue: "capo_rds_data.types.blob.Blob"


class ValueArrayValuesMember(TypedDict, closed=True):
    arrayValues: "capo_rds_data.types.array_value_list.ArrayValueList"


class ValueStructValueMember(TypedDict, closed=True):
    structValue: "capo_rds_data.types.struct_value.StructValue"


Value: TypeAlias = (
    ValueIsNullMember
    | ValueBitValueMember
    | ValueBigIntValueMember
    | ValueIntValueMember
    | ValueDoubleValueMember
    | ValueRealValueMember
    | ValueStringValueMember
    | ValueBlobValueMember
    | ValueArrayValuesMember
    | ValueStructValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Value) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Value: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "isNull" in value:
        return {"isNull": value["isNull"]}
    elif "bitValue" in value:
        return {"bitValue": value["bitValue"]}
    elif "bigIntValue" in value:
        return {"bigIntValue": value["bigIntValue"]}
    elif "intValue" in value:
        return {"intValue": value["intValue"]}
    elif "doubleValue" in value:
        return {
            "doubleValue": (
                "NaN"
                if value["doubleValue"] != value["doubleValue"]
                else "Infinity"
                if value["doubleValue"] == float("inf")
                else "-Infinity"
                if value["doubleValue"] == float("-inf")
                else value["doubleValue"]
            )
        }
    elif "realValue" in value:
        return {
            "realValue": (
                "NaN"
                if value["realValue"] != value["realValue"]
                else "Infinity"
                if value["realValue"] == float("inf")
                else "-Infinity"
                if value["realValue"] == float("-inf")
                else value["realValue"]
            )
        }
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "blobValue" in value:
        import capo_rds_data.types.blob

        return {
            "blobValue": capo_rds_data.types.blob.serialize_json(value["blobValue"])
        }
    elif "arrayValues" in value:
        import capo_rds_data.types.array_value_list

        return {
            "arrayValues": capo_rds_data.types.array_value_list.serialize_json(
                value["arrayValues"]
            )
        }
    elif "structValue" in value:
        import capo_rds_data.types.struct_value

        return {
            "structValue": capo_rds_data.types.struct_value.serialize_json(
                value["structValue"]
            )
        }
    else:
        raise SerializationError("Value: no variant present")


def deserialize_json(data: dict) -> Value:
    if data.get("isNull") is not None:
        return {"isNull": data["isNull"]}
    elif data.get("bitValue") is not None:
        return {"bitValue": data["bitValue"]}
    elif data.get("bigIntValue") is not None:
        return {"bigIntValue": data["bigIntValue"]}
    elif data.get("intValue") is not None:
        return {"intValue": data["intValue"]}
    elif data.get("doubleValue") is not None:
        return {"doubleValue": float(data["doubleValue"])}
    elif data.get("realValue") is not None:
        return {"realValue": float(data["realValue"])}
    elif data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("blobValue") is not None:
        import capo_rds_data.types.blob

        return {
            "blobValue": capo_rds_data.types.blob.deserialize_json(data["blobValue"])
        }
    elif data.get("arrayValues") is not None:
        import capo_rds_data.types.array_value_list

        return {
            "arrayValues": capo_rds_data.types.array_value_list.deserialize_json(
                data["arrayValues"]
            )
        }
    elif data.get("structValue") is not None:
        import capo_rds_data.types.struct_value

        return {
            "structValue": capo_rds_data.types.struct_value.deserialize_json(
                data["structValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Value: no recognized variant key")
