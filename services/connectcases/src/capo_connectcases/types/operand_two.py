"""Generated from Smithy shape ``com.amazonaws.connectcases#OperandTwo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.empty_operand_value


class OperandTwoStringValueMember(TypedDict, closed=True):
    stringValue: "str"


class OperandTwoBooleanValueMember(TypedDict, closed=True):
    booleanValue: "bool"


class OperandTwoDoubleValueMember(TypedDict, closed=True):
    doubleValue: "float"


class OperandTwoEmptyValueMember(TypedDict, closed=True):
    emptyValue: "capo_connectcases.types.empty_operand_value.EmptyOperandValue"


OperandTwo: TypeAlias = (
    OperandTwoStringValueMember
    | OperandTwoBooleanValueMember
    | OperandTwoDoubleValueMember
    | OperandTwoEmptyValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OperandTwo) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OperandTwo: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
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
    elif "emptyValue" in value:
        import capo_connectcases.types.empty_operand_value

        return {
            "emptyValue": capo_connectcases.types.empty_operand_value.serialize_json(
                value["emptyValue"]
            )
        }
    else:
        raise SerializationError("OperandTwo: no variant present")


def deserialize_json(data: dict) -> OperandTwo:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("booleanValue") is not None:
        return {"booleanValue": data["booleanValue"]}
    elif data.get("doubleValue") is not None:
        return {"doubleValue": float(data["doubleValue"])}
    elif data.get("emptyValue") is not None:
        import capo_connectcases.types.empty_operand_value

        return {
            "emptyValue": capo_connectcases.types.empty_operand_value.deserialize_json(
                data["emptyValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OperandTwo: no recognized variant key")
