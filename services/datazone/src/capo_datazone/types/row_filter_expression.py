"""Generated from Smithy shape ``com.amazonaws.datazone#RowFilterExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.equal_to_expression
    import capo_datazone.types.greater_than_expression
    import capo_datazone.types.greater_than_or_equal_to_expression
    import capo_datazone.types.in_expression
    import capo_datazone.types.is_not_null_expression
    import capo_datazone.types.is_null_expression
    import capo_datazone.types.less_than_expression
    import capo_datazone.types.less_than_or_equal_to_expression
    import capo_datazone.types.like_expression
    import capo_datazone.types.not_equal_to_expression
    import capo_datazone.types.not_in_expression
    import capo_datazone.types.not_like_expression


class _RowFilterExpression_equalTo(TypedDict, closed=True):
    equalTo: "capo_datazone.types.equal_to_expression.EqualToExpression"


class _RowFilterExpression_notEqualTo(TypedDict, closed=True):
    notEqualTo: "capo_datazone.types.not_equal_to_expression.NotEqualToExpression"


class _RowFilterExpression_greaterThan(TypedDict, closed=True):
    greaterThan: "capo_datazone.types.greater_than_expression.GreaterThanExpression"


class _RowFilterExpression_lessThan(TypedDict, closed=True):
    lessThan: "capo_datazone.types.less_than_expression.LessThanExpression"


class _RowFilterExpression_greaterThanOrEqualTo(TypedDict, closed=True):
    greaterThanOrEqualTo: "capo_datazone.types.greater_than_or_equal_to_expression.GreaterThanOrEqualToExpression"


class _RowFilterExpression_lessThanOrEqualTo(TypedDict, closed=True):
    lessThanOrEqualTo: "capo_datazone.types.less_than_or_equal_to_expression.LessThanOrEqualToExpression"


class _RowFilterExpression_isNull(TypedDict, closed=True):
    isNull: "capo_datazone.types.is_null_expression.IsNullExpression"


class _RowFilterExpression_isNotNull(TypedDict, closed=True):
    isNotNull: "capo_datazone.types.is_not_null_expression.IsNotNullExpression"


_RowFilterExpression_in = TypedDict(
    "_RowFilterExpression_in",
    {
        "in": "capo_datazone.types.in_expression.InExpression",
    },
    closed=True,
)


class _RowFilterExpression_notIn(TypedDict, closed=True):
    notIn: "capo_datazone.types.not_in_expression.NotInExpression"


class _RowFilterExpression_like(TypedDict, closed=True):
    like: "capo_datazone.types.like_expression.LikeExpression"


class _RowFilterExpression_notLike(TypedDict, closed=True):
    notLike: "capo_datazone.types.not_like_expression.NotLikeExpression"


RowFilterExpression: TypeAlias = (
    _RowFilterExpression_equalTo
    | _RowFilterExpression_notEqualTo
    | _RowFilterExpression_greaterThan
    | _RowFilterExpression_lessThan
    | _RowFilterExpression_greaterThanOrEqualTo
    | _RowFilterExpression_lessThanOrEqualTo
    | _RowFilterExpression_isNull
    | _RowFilterExpression_isNotNull
    | _RowFilterExpression_in
    | _RowFilterExpression_notIn
    | _RowFilterExpression_like
    | _RowFilterExpression_notLike
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RowFilterExpression) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RowFilterExpression: cannot serialize unknown variant {value.name!r}"
        )
    elif "equalTo" in value:
        import capo_datazone.types.equal_to_expression

        return {
            "equalTo": capo_datazone.types.equal_to_expression.serialize_json(
                value["equalTo"]
            )
        }
    elif "notEqualTo" in value:
        import capo_datazone.types.not_equal_to_expression

        return {
            "notEqualTo": capo_datazone.types.not_equal_to_expression.serialize_json(
                value["notEqualTo"]
            )
        }
    elif "greaterThan" in value:
        import capo_datazone.types.greater_than_expression

        return {
            "greaterThan": capo_datazone.types.greater_than_expression.serialize_json(
                value["greaterThan"]
            )
        }
    elif "lessThan" in value:
        import capo_datazone.types.less_than_expression

        return {
            "lessThan": capo_datazone.types.less_than_expression.serialize_json(
                value["lessThan"]
            )
        }
    elif "greaterThanOrEqualTo" in value:
        import capo_datazone.types.greater_than_or_equal_to_expression

        return {
            "greaterThanOrEqualTo": capo_datazone.types.greater_than_or_equal_to_expression.serialize_json(
                value["greaterThanOrEqualTo"]
            )
        }
    elif "lessThanOrEqualTo" in value:
        import capo_datazone.types.less_than_or_equal_to_expression

        return {
            "lessThanOrEqualTo": capo_datazone.types.less_than_or_equal_to_expression.serialize_json(
                value["lessThanOrEqualTo"]
            )
        }
    elif "isNull" in value:
        import capo_datazone.types.is_null_expression

        return {
            "isNull": capo_datazone.types.is_null_expression.serialize_json(
                value["isNull"]
            )
        }
    elif "isNotNull" in value:
        import capo_datazone.types.is_not_null_expression

        return {
            "isNotNull": capo_datazone.types.is_not_null_expression.serialize_json(
                value["isNotNull"]
            )
        }
    elif "in" in value:
        import capo_datazone.types.in_expression

        return {"in": capo_datazone.types.in_expression.serialize_json(value["in"])}
    elif "notIn" in value:
        import capo_datazone.types.not_in_expression

        return {
            "notIn": capo_datazone.types.not_in_expression.serialize_json(
                value["notIn"]
            )
        }
    elif "like" in value:
        import capo_datazone.types.like_expression

        return {
            "like": capo_datazone.types.like_expression.serialize_json(value["like"])
        }
    elif "notLike" in value:
        import capo_datazone.types.not_like_expression

        return {
            "notLike": capo_datazone.types.not_like_expression.serialize_json(
                value["notLike"]
            )
        }
    else:
        raise SerializationError("RowFilterExpression: no variant present")


def deserialize_json(data: dict) -> RowFilterExpression:
    if data.get("equalTo") is not None:
        import capo_datazone.types.equal_to_expression

        return {
            "equalTo": capo_datazone.types.equal_to_expression.deserialize_json(
                data["equalTo"]
            )
        }
    elif data.get("notEqualTo") is not None:
        import capo_datazone.types.not_equal_to_expression

        return {
            "notEqualTo": capo_datazone.types.not_equal_to_expression.deserialize_json(
                data["notEqualTo"]
            )
        }
    elif data.get("greaterThan") is not None:
        import capo_datazone.types.greater_than_expression

        return {
            "greaterThan": capo_datazone.types.greater_than_expression.deserialize_json(
                data["greaterThan"]
            )
        }
    elif data.get("lessThan") is not None:
        import capo_datazone.types.less_than_expression

        return {
            "lessThan": capo_datazone.types.less_than_expression.deserialize_json(
                data["lessThan"]
            )
        }
    elif data.get("greaterThanOrEqualTo") is not None:
        import capo_datazone.types.greater_than_or_equal_to_expression

        return {
            "greaterThanOrEqualTo": capo_datazone.types.greater_than_or_equal_to_expression.deserialize_json(
                data["greaterThanOrEqualTo"]
            )
        }
    elif data.get("lessThanOrEqualTo") is not None:
        import capo_datazone.types.less_than_or_equal_to_expression

        return {
            "lessThanOrEqualTo": capo_datazone.types.less_than_or_equal_to_expression.deserialize_json(
                data["lessThanOrEqualTo"]
            )
        }
    elif data.get("isNull") is not None:
        import capo_datazone.types.is_null_expression

        return {
            "isNull": capo_datazone.types.is_null_expression.deserialize_json(
                data["isNull"]
            )
        }
    elif data.get("isNotNull") is not None:
        import capo_datazone.types.is_not_null_expression

        return {
            "isNotNull": capo_datazone.types.is_not_null_expression.deserialize_json(
                data["isNotNull"]
            )
        }
    elif data.get("in") is not None:
        import capo_datazone.types.in_expression

        return {"in": capo_datazone.types.in_expression.deserialize_json(data["in"])}
    elif data.get("notIn") is not None:
        import capo_datazone.types.not_in_expression

        return {
            "notIn": capo_datazone.types.not_in_expression.deserialize_json(
                data["notIn"]
            )
        }
    elif data.get("like") is not None:
        import capo_datazone.types.like_expression

        return {
            "like": capo_datazone.types.like_expression.deserialize_json(data["like"])
        }
    elif data.get("notLike") is not None:
        import capo_datazone.types.not_like_expression

        return {
            "notLike": capo_datazone.types.not_like_expression.deserialize_json(
                data["notLike"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("RowFilterExpression: no recognized variant key")
