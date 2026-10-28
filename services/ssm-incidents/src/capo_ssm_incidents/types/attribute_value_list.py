"""Generated from Smithy shape ``com.amazonaws.ssmincidents#AttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.integer_list
    import capo_ssm_incidents.types.string_list


class AttributeValueListStringValuesMember(TypedDict, closed=True):
    stringValues: "capo_ssm_incidents.types.string_list.StringList"


class AttributeValueListIntegerValuesMember(TypedDict, closed=True):
    integerValues: "capo_ssm_incidents.types.integer_list.IntegerList"


AttributeValueList: TypeAlias = (
    AttributeValueListStringValuesMember
    | AttributeValueListIntegerValuesMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValueList) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AttributeValueList: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "stringValues" in value:
        import capo_ssm_incidents.types.string_list

        return {
            "stringValues": capo_ssm_incidents.types.string_list.serialize_json(
                value["stringValues"]
            )
        }
    elif "integerValues" in value:
        import capo_ssm_incidents.types.integer_list

        return {
            "integerValues": capo_ssm_incidents.types.integer_list.serialize_json(
                value["integerValues"]
            )
        }
    else:
        raise SerializationError("AttributeValueList: no variant present")


def deserialize_json(data: dict) -> AttributeValueList:
    if data.get("stringValues") is not None:
        import capo_ssm_incidents.types.string_list

        return {
            "stringValues": capo_ssm_incidents.types.string_list.deserialize_json(
                data["stringValues"]
            )
        }
    elif data.get("integerValues") is not None:
        import capo_ssm_incidents.types.integer_list

        return {
            "integerValues": capo_ssm_incidents.types.integer_list.deserialize_json(
                data["integerValues"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AttributeValueList: no recognized variant key")
