"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.field_value


class _FieldFilter_equalTo(TypedDict, closed=True):
    equalTo: "capo_connectcases.types.field_value.FieldValue"


class _FieldFilter_contains(TypedDict, closed=True):
    contains: "capo_connectcases.types.field_value.FieldValue"


class _FieldFilter_greaterThan(TypedDict, closed=True):
    greaterThan: "capo_connectcases.types.field_value.FieldValue"


class _FieldFilter_greaterThanOrEqualTo(TypedDict, closed=True):
    greaterThanOrEqualTo: "capo_connectcases.types.field_value.FieldValue"


class _FieldFilter_lessThan(TypedDict, closed=True):
    lessThan: "capo_connectcases.types.field_value.FieldValue"


class _FieldFilter_lessThanOrEqualTo(TypedDict, closed=True):
    lessThanOrEqualTo: "capo_connectcases.types.field_value.FieldValue"


FieldFilter: TypeAlias = (
    _FieldFilter_equalTo
    | _FieldFilter_contains
    | _FieldFilter_greaterThan
    | _FieldFilter_greaterThanOrEqualTo
    | _FieldFilter_lessThan
    | _FieldFilter_lessThanOrEqualTo
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FieldFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"FieldFilter: cannot serialize unknown variant {value.name!r}"
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
            return UnknownUnionMember(name)
        raise DeserializationError("FieldFilter: no recognized variant key")
