"""Generated from Smithy shape ``com.amazonaws.rdsdata#Field``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_rds_data.errors import DeserializationError, SerializationError
from capo_rds_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_rds_data.types.array_value
    import capo_rds_data.types.blob
    import capo_rds_data.types.boxed_boolean
    import capo_rds_data.types.boxed_double
    import capo_rds_data.types.boxed_long
    import capo_rds_data.types.string


class FieldIsNullMember(TypedDict, closed=True):
    isNull: "capo_rds_data.types.boxed_boolean.BoxedBoolean"


class FieldBooleanValueMember(TypedDict, closed=True):
    booleanValue: "capo_rds_data.types.boxed_boolean.BoxedBoolean"


class FieldLongValueMember(TypedDict, closed=True):
    longValue: "capo_rds_data.types.boxed_long.BoxedLong"


class FieldDoubleValueMember(TypedDict, closed=True):
    doubleValue: "capo_rds_data.types.boxed_double.BoxedDouble"


class FieldStringValueMember(TypedDict, closed=True):
    stringValue: "capo_rds_data.types.string.String"


class FieldBlobValueMember(TypedDict, closed=True):
    blobValue: "capo_rds_data.types.blob.Blob"


class FieldArrayValueMember(TypedDict, closed=True):
    arrayValue: "capo_rds_data.types.array_value.ArrayValue"


Field: TypeAlias = (
    FieldIsNullMember
    | FieldBooleanValueMember
    | FieldLongValueMember
    | FieldDoubleValueMember
    | FieldStringValueMember
    | FieldBlobValueMember
    | FieldArrayValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Field) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Field: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "isNull" in value:
        return {"isNull": value["isNull"]}
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
    elif "longValue" in value:
        return {"longValue": value["longValue"]}
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
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "blobValue" in value:
        import capo_rds_data.types.blob

        return {
            "blobValue": capo_rds_data.types.blob.serialize_json(value["blobValue"])
        }
    elif "arrayValue" in value:
        import capo_rds_data.types.array_value

        return {
            "arrayValue": capo_rds_data.types.array_value.serialize_json(
                value["arrayValue"]
            )
        }
    else:
        raise SerializationError("Field: no variant present")


def deserialize_json(data: dict) -> Field:
    if data.get("isNull") is not None:
        return {"isNull": data["isNull"]}
    elif data.get("booleanValue") is not None:
        return {"booleanValue": data["booleanValue"]}
    elif data.get("longValue") is not None:
        return {"longValue": data["longValue"]}
    elif data.get("doubleValue") is not None:
        return {"doubleValue": float(data["doubleValue"])}
    elif data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("blobValue") is not None:
        import capo_rds_data.types.blob

        return {
            "blobValue": capo_rds_data.types.blob.deserialize_json(data["blobValue"])
        }
    elif data.get("arrayValue") is not None:
        import capo_rds_data.types.array_value

        return {
            "arrayValue": capo_rds_data.types.array_value.deserialize_json(
                data["arrayValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Field: no recognized variant key")
