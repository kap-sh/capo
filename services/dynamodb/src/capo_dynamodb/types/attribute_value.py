"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError, SerializationError
from capo_dynamodb.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_dynamodb.types.binary_attribute_value
    import capo_dynamodb.types.binary_set_attribute_value
    import capo_dynamodb.types.boolean_attribute_value
    import capo_dynamodb.types.list_attribute_value
    import capo_dynamodb.types.map_attribute_value
    import capo_dynamodb.types.null_attribute_value
    import capo_dynamodb.types.number_attribute_value
    import capo_dynamodb.types.number_set_attribute_value
    import capo_dynamodb.types.string_attribute_value
    import capo_dynamodb.types.string_set_attribute_value


class AttributeValueSMember(TypedDict, closed=True):
    S: "capo_dynamodb.types.string_attribute_value.StringAttributeValue"


class AttributeValueNMember(TypedDict, closed=True):
    N: "capo_dynamodb.types.number_attribute_value.NumberAttributeValue"


class AttributeValueBMember(TypedDict, closed=True):
    B: "capo_dynamodb.types.binary_attribute_value.BinaryAttributeValue"


class AttributeValueSSMember(TypedDict, closed=True):
    SS: "capo_dynamodb.types.string_set_attribute_value.StringSetAttributeValue"


class AttributeValueNSMember(TypedDict, closed=True):
    NS: "capo_dynamodb.types.number_set_attribute_value.NumberSetAttributeValue"


class AttributeValueBSMember(TypedDict, closed=True):
    BS: "capo_dynamodb.types.binary_set_attribute_value.BinarySetAttributeValue"


class AttributeValueMMember(TypedDict, closed=True):
    M: "capo_dynamodb.types.map_attribute_value.MapAttributeValue"


class AttributeValueLMember(TypedDict, closed=True):
    L: "capo_dynamodb.types.list_attribute_value.ListAttributeValue"


class AttributeValueNULLMember(TypedDict, closed=True):
    NULL: "capo_dynamodb.types.null_attribute_value.NullAttributeValue"


class AttributeValueBOOLMember(TypedDict, closed=True):
    BOOL: "capo_dynamodb.types.boolean_attribute_value.BooleanAttributeValue"


AttributeValue: TypeAlias = (
    AttributeValueSMember
    | AttributeValueNMember
    | AttributeValueBMember
    | AttributeValueSSMember
    | AttributeValueNSMember
    | AttributeValueBSMember
    | AttributeValueMMember
    | AttributeValueLMember
    | AttributeValueNULLMember
    | AttributeValueBOOLMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AttributeValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "S" in value:
        return {"S": value["S"]}
    elif "N" in value:
        return {"N": value["N"]}
    elif "B" in value:
        import capo_dynamodb.types.binary_attribute_value

        return {
            "B": capo_dynamodb.types.binary_attribute_value.serialize_aws_json_1_0(
                value["B"]
            )
        }
    elif "SS" in value:
        import capo_dynamodb.types.string_set_attribute_value

        return {
            "SS": capo_dynamodb.types.string_set_attribute_value.serialize_aws_json_1_0(
                value["SS"]
            )
        }
    elif "NS" in value:
        import capo_dynamodb.types.number_set_attribute_value

        return {
            "NS": capo_dynamodb.types.number_set_attribute_value.serialize_aws_json_1_0(
                value["NS"]
            )
        }
    elif "BS" in value:
        import capo_dynamodb.types.binary_set_attribute_value

        return {
            "BS": capo_dynamodb.types.binary_set_attribute_value.serialize_aws_json_1_0(
                value["BS"]
            )
        }
    elif "M" in value:
        import capo_dynamodb.types.map_attribute_value

        return {
            "M": capo_dynamodb.types.map_attribute_value.serialize_aws_json_1_0(
                value["M"]
            )
        }
    elif "L" in value:
        import capo_dynamodb.types.list_attribute_value

        return {
            "L": capo_dynamodb.types.list_attribute_value.serialize_aws_json_1_0(
                value["L"]
            )
        }
    elif "NULL" in value:
        return {"NULL": value["NULL"]}
    elif "BOOL" in value:
        return {"BOOL": value["BOOL"]}
    else:
        raise SerializationError("AttributeValue: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AttributeValue:
    if data.get("S") is not None:
        return {"S": data["S"]}
    elif data.get("N") is not None:
        return {"N": data["N"]}
    elif data.get("B") is not None:
        import capo_dynamodb.types.binary_attribute_value

        return {
            "B": capo_dynamodb.types.binary_attribute_value.deserialize_aws_json_1_0(
                data["B"]
            )
        }
    elif data.get("SS") is not None:
        import capo_dynamodb.types.string_set_attribute_value

        return {
            "SS": capo_dynamodb.types.string_set_attribute_value.deserialize_aws_json_1_0(
                data["SS"]
            )
        }
    elif data.get("NS") is not None:
        import capo_dynamodb.types.number_set_attribute_value

        return {
            "NS": capo_dynamodb.types.number_set_attribute_value.deserialize_aws_json_1_0(
                data["NS"]
            )
        }
    elif data.get("BS") is not None:
        import capo_dynamodb.types.binary_set_attribute_value

        return {
            "BS": capo_dynamodb.types.binary_set_attribute_value.deserialize_aws_json_1_0(
                data["BS"]
            )
        }
    elif data.get("M") is not None:
        import capo_dynamodb.types.map_attribute_value

        return {
            "M": capo_dynamodb.types.map_attribute_value.deserialize_aws_json_1_0(
                data["M"]
            )
        }
    elif data.get("L") is not None:
        import capo_dynamodb.types.list_attribute_value

        return {
            "L": capo_dynamodb.types.list_attribute_value.deserialize_aws_json_1_0(
                data["L"]
            )
        }
    elif data.get("NULL") is not None:
        return {"NULL": data["NULL"]}
    elif data.get("BOOL") is not None:
        return {"BOOL": data["BOOL"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AttributeValue: no recognized variant key")
