"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.field_value


class FieldFilterEqualToMember(TypedDict, closed=True):
    equalTo: "capo_connectcases.types.field_value.FieldValue"


class FieldFilterContainsMember(TypedDict, closed=True):
    contains: "capo_connectcases.types.field_value.FieldValue"


class FieldFilterGreaterThanMember(TypedDict, closed=True):
    greaterThan: "capo_connectcases.types.field_value.FieldValue"


class FieldFilterGreaterThanOrEqualToMember(TypedDict, closed=True):
    greaterThanOrEqualTo: "capo_connectcases.types.field_value.FieldValue"


class FieldFilterLessThanMember(TypedDict, closed=True):
    lessThan: "capo_connectcases.types.field_value.FieldValue"


class FieldFilterLessThanOrEqualToMember(TypedDict, closed=True):
    lessThanOrEqualTo: "capo_connectcases.types.field_value.FieldValue"


FieldFilter: TypeAlias = (
    FieldFilterEqualToMember
    | FieldFilterContainsMember
    | FieldFilterGreaterThanMember
    | FieldFilterGreaterThanOrEqualToMember
    | FieldFilterLessThanMember
    | FieldFilterLessThanOrEqualToMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FieldFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FieldFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "equalTo" in value:
        import capo_connectcases.types.field_value

        return {
            "equalTo": capo_connectcases.types.field_value.serialize_json(
                value["equalTo"]
            )
        }
    elif "contains" in value:
        import capo_connectcases.types.field_value

        return {
            "contains": capo_connectcases.types.field_value.serialize_json(
                value["contains"]
            )
        }
    elif "greaterThan" in value:
        import capo_connectcases.types.field_value

        return {
            "greaterThan": capo_connectcases.types.field_value.serialize_json(
                value["greaterThan"]
            )
        }
    elif "greaterThanOrEqualTo" in value:
        import capo_connectcases.types.field_value

        return {
            "greaterThanOrEqualTo": capo_connectcases.types.field_value.serialize_json(
                value["greaterThanOrEqualTo"]
            )
        }
    elif "lessThan" in value:
        import capo_connectcases.types.field_value

        return {
            "lessThan": capo_connectcases.types.field_value.serialize_json(
                value["lessThan"]
            )
        }
    elif "lessThanOrEqualTo" in value:
        import capo_connectcases.types.field_value

        return {
            "lessThanOrEqualTo": capo_connectcases.types.field_value.serialize_json(
                value["lessThanOrEqualTo"]
            )
        }
    else:
        raise SerializationError("FieldFilter: no variant present")


def deserialize_json(data: dict) -> FieldFilter:
    if data.get("equalTo") is not None:
        import capo_connectcases.types.field_value

        return {
            "equalTo": capo_connectcases.types.field_value.deserialize_json(
                data["equalTo"]
            )
        }
    elif data.get("contains") is not None:
        import capo_connectcases.types.field_value

        return {
            "contains": capo_connectcases.types.field_value.deserialize_json(
                data["contains"]
            )
        }
    elif data.get("greaterThan") is not None:
        import capo_connectcases.types.field_value

        return {
            "greaterThan": capo_connectcases.types.field_value.deserialize_json(
                data["greaterThan"]
            )
        }
    elif data.get("greaterThanOrEqualTo") is not None:
        import capo_connectcases.types.field_value

        return {
            "greaterThanOrEqualTo": capo_connectcases.types.field_value.deserialize_json(
                data["greaterThanOrEqualTo"]
            )
        }
    elif data.get("lessThan") is not None:
        import capo_connectcases.types.field_value

        return {
            "lessThan": capo_connectcases.types.field_value.deserialize_json(
                data["lessThan"]
            )
        }
    elif data.get("lessThanOrEqualTo") is not None:
        import capo_connectcases.types.field_value

        return {
            "lessThanOrEqualTo": capo_connectcases.types.field_value.deserialize_json(
                data["lessThanOrEqualTo"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FieldFilter: no recognized variant key")
