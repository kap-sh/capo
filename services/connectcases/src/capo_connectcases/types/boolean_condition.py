"""Generated from Smithy shape ``com.amazonaws.connectcases#BooleanCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.boolean_operands
    import capo_connectcases.types.compound_condition


class BooleanConditionEqualToMember(TypedDict, closed=True):
    equalTo: "capo_connectcases.types.boolean_operands.BooleanOperands"


class BooleanConditionNotEqualToMember(TypedDict, closed=True):
    notEqualTo: "capo_connectcases.types.boolean_operands.BooleanOperands"


class BooleanConditionAndAllMember(TypedDict, closed=True):
    andAll: "capo_connectcases.types.compound_condition.CompoundCondition"


class BooleanConditionOrAllMember(TypedDict, closed=True):
    orAll: "capo_connectcases.types.compound_condition.CompoundCondition"


BooleanCondition: TypeAlias = (
    BooleanConditionEqualToMember
    | BooleanConditionNotEqualToMember
    | BooleanConditionAndAllMember
    | BooleanConditionOrAllMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BooleanCondition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BooleanCondition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "equalTo" in value:
        import capo_connectcases.types.boolean_operands

        return {
            "equalTo": capo_connectcases.types.boolean_operands.serialize_json(
                value["equalTo"]
            )
        }
    elif "notEqualTo" in value:
        import capo_connectcases.types.boolean_operands

        return {
            "notEqualTo": capo_connectcases.types.boolean_operands.serialize_json(
                value["notEqualTo"]
            )
        }
    elif "andAll" in value:
        import capo_connectcases.types.compound_condition

        return {
            "andAll": capo_connectcases.types.compound_condition.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import capo_connectcases.types.compound_condition

        return {
            "orAll": capo_connectcases.types.compound_condition.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("BooleanCondition: no variant present")


def deserialize_json(data: dict) -> BooleanCondition:
    if data.get("equalTo") is not None:
        import capo_connectcases.types.boolean_operands

        return {
            "equalTo": capo_connectcases.types.boolean_operands.deserialize_json(
                data["equalTo"]
            )
        }
    elif data.get("notEqualTo") is not None:
        import capo_connectcases.types.boolean_operands

        return {
            "notEqualTo": capo_connectcases.types.boolean_operands.deserialize_json(
                data["notEqualTo"]
            )
        }
    elif data.get("andAll") is not None:
        import capo_connectcases.types.compound_condition

        return {
            "andAll": capo_connectcases.types.compound_condition.deserialize_json(
                data["andAll"]
            )
        }
    elif data.get("orAll") is not None:
        import capo_connectcases.types.compound_condition

        return {
            "orAll": capo_connectcases.types.compound_condition.deserialize_json(
                data["orAll"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BooleanCondition: no recognized variant key")
