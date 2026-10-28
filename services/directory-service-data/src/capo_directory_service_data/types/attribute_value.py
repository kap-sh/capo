"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#AttributeValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_directory_service_data.errors import DeserializationError, SerializationError
from capo_directory_service_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_directory_service_data.types.boolean_attribute_value
    import capo_directory_service_data.types.number_attribute_value
    import capo_directory_service_data.types.string_attribute_value
    import capo_directory_service_data.types.string_set_attribute_value


class AttributeValueSMember(TypedDict, closed=True):
    S: "capo_directory_service_data.types.string_attribute_value.StringAttributeValue"


class AttributeValueNMember(TypedDict, closed=True):
    N: "capo_directory_service_data.types.number_attribute_value.NumberAttributeValue"


class AttributeValueBOOLMember(TypedDict, closed=True):
    BOOL: "capo_directory_service_data.types.boolean_attribute_value.BooleanAttributeValue"


class AttributeValueSSMember(TypedDict, closed=True):
    SS: "capo_directory_service_data.types.string_set_attribute_value.StringSetAttributeValue"


AttributeValue: TypeAlias = (
    AttributeValueSMember
    | AttributeValueNMember
    | AttributeValueBOOLMember
    | AttributeValueSSMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AttributeValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "S" in value:
        return {"S": value["S"]}
    elif "N" in value:
        return {"N": value["N"]}
    elif "BOOL" in value:
        return {"BOOL": value["BOOL"]}
    elif "SS" in value:
        import capo_directory_service_data.types.string_set_attribute_value

        return {
            "SS": capo_directory_service_data.types.string_set_attribute_value.serialize_json(
                value["SS"]
            )
        }
    else:
        raise SerializationError("AttributeValue: no variant present")


def deserialize_json(data: dict) -> AttributeValue:
    if data.get("S") is not None:
        return {"S": data["S"]}
    elif data.get("N") is not None:
        return {"N": data["N"]}
    elif data.get("BOOL") is not None:
        return {"BOOL": data["BOOL"]}
    elif data.get("SS") is not None:
        import capo_directory_service_data.types.string_set_attribute_value

        return {
            "SS": capo_directory_service_data.types.string_set_attribute_value.deserialize_json(
                data["SS"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AttributeValue: no recognized variant key")


def redact_sensitive(value: AttributeValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "S" in value:
        out["S"] = "*** Sensitive Data Redacted ***"
    if "N" in value:
        out["N"] = "*** Sensitive Data Redacted ***"
    if "BOOL" in value:
        out["BOOL"] = "*** Sensitive Data Redacted ***"
    if "SS" in value:
        out["SS"] = "*** Sensitive Data Redacted ***"
    return out
