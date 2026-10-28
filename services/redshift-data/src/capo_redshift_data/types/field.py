"""Generated from Smithy shape ``com.amazonaws.redshiftdata#Field``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift_data.errors import DeserializationError, SerializationError
from capo_redshift_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_redshift_data.types.blob
    import capo_redshift_data.types.boxed_boolean
    import capo_redshift_data.types.boxed_double
    import capo_redshift_data.types.boxed_long
    import capo_redshift_data.types.string


class FieldIsNullMember(TypedDict, closed=True):
    isNull: "capo_redshift_data.types.boxed_boolean.BoxedBoolean"


class FieldBooleanValueMember(TypedDict, closed=True):
    booleanValue: "capo_redshift_data.types.boxed_boolean.BoxedBoolean"


class FieldLongValueMember(TypedDict, closed=True):
    longValue: "capo_redshift_data.types.boxed_long.BoxedLong"


class FieldDoubleValueMember(TypedDict, closed=True):
    doubleValue: "capo_redshift_data.types.boxed_double.BoxedDouble"


class FieldStringValueMember(TypedDict, closed=True):
    stringValue: "capo_redshift_data.types.string.String"


class FieldBlobValueMember(TypedDict, closed=True):
    blobValue: "capo_redshift_data.types.blob.Blob"


Field: TypeAlias = (
    FieldIsNullMember
    | FieldBooleanValueMember
    | FieldLongValueMember
    | FieldDoubleValueMember
    | FieldStringValueMember
    | FieldBlobValueMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Field) -> dict:
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
        import capo_redshift_data.types.blob

        return {
            "blobValue": capo_redshift_data.types.blob.serialize_aws_json_1_1(
                value["blobValue"]
            )
        }
    else:
        raise SerializationError("Field: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Field:
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
        import capo_redshift_data.types.blob

        return {
            "blobValue": capo_redshift_data.types.blob.deserialize_aws_json_1_1(
                data["blobValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Field: no recognized variant key")
