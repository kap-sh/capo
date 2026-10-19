"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_string_list_value
    import capo_qbusiness.types.document_attribute_string_value
    import capo_qbusiness.types.long
    import capo_qbusiness.types.timestamp


class _DocumentAttributeValue_stringValue(TypedDict, closed=True):
    stringValue: "capo_qbusiness.types.document_attribute_string_value.DocumentAttributeStringValue"


class _DocumentAttributeValue_stringListValue(TypedDict, closed=True):
    stringListValue: "capo_qbusiness.types.document_attribute_string_list_value.DocumentAttributeStringListValue"


class _DocumentAttributeValue_longValue(TypedDict, closed=True):
    longValue: "capo_qbusiness.types.long.Long"


class _DocumentAttributeValue_dateValue(TypedDict, closed=True):
    dateValue: "capo_qbusiness.types.timestamp.Timestamp"


DocumentAttributeValue: TypeAlias = (
    _DocumentAttributeValue_stringValue
    | _DocumentAttributeValue_stringListValue
    | _DocumentAttributeValue_longValue
    | _DocumentAttributeValue_dateValue
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeValue) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DocumentAttributeValue: cannot serialize unknown variant {value.name!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "stringListValue" in value:
        import capo_qbusiness.types.document_attribute_string_list_value

        return {
            "stringListValue": capo_qbusiness.types.document_attribute_string_list_value.serialize_json(
                value["stringListValue"]
            )
        }
    elif "longValue" in value:
        return {"longValue": value["longValue"]}
    elif "dateValue" in value:
        import capo_qbusiness.types.timestamp

        return {
            "dateValue": capo_qbusiness.types.timestamp.serialize_json(
                value["dateValue"]
            )
        }
    else:
        raise SerializationError("DocumentAttributeValue: no variant present")


def deserialize_json(data: dict) -> DocumentAttributeValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("stringListValue") is not None:
        import capo_qbusiness.types.document_attribute_string_list_value

        return {
            "stringListValue": capo_qbusiness.types.document_attribute_string_list_value.deserialize_json(
                data["stringListValue"]
            )
        }
    elif data.get("longValue") is not None:
        return {"longValue": data["longValue"]}
    elif data.get("dateValue") is not None:
        import capo_qbusiness.types.timestamp

        return {
            "dateValue": capo_qbusiness.types.timestamp.deserialize_json(
                data["dateValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DocumentAttributeValue: no recognized variant key")
