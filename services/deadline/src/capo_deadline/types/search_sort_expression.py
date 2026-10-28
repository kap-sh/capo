"""Generated from Smithy shape ``com.amazonaws.deadline#SearchSortExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.field_sort_expression
    import capo_deadline.types.parameter_sort_expression
    import capo_deadline.types.user_jobs_first


class SearchSortExpressionUserJobsFirstMember(TypedDict, closed=True):
    userJobsFirst: "capo_deadline.types.user_jobs_first.UserJobsFirst"


class SearchSortExpressionFieldSortMember(TypedDict, closed=True):
    fieldSort: "capo_deadline.types.field_sort_expression.FieldSortExpression"


class SearchSortExpressionParameterSortMember(TypedDict, closed=True):
    parameterSort: (
        "capo_deadline.types.parameter_sort_expression.ParameterSortExpression"
    )


SearchSortExpression: TypeAlias = (
    SearchSortExpressionUserJobsFirstMember
    | SearchSortExpressionFieldSortMember
    | SearchSortExpressionParameterSortMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchSortExpression) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SearchSortExpression: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "userJobsFirst" in value:
        import capo_deadline.types.user_jobs_first

        return {
            "userJobsFirst": capo_deadline.types.user_jobs_first.serialize_json(
                value["userJobsFirst"]
            )
        }
    elif "fieldSort" in value:
        import capo_deadline.types.field_sort_expression

        return {
            "fieldSort": capo_deadline.types.field_sort_expression.serialize_json(
                value["fieldSort"]
            )
        }
    elif "parameterSort" in value:
        import capo_deadline.types.parameter_sort_expression

        return {
            "parameterSort": capo_deadline.types.parameter_sort_expression.serialize_json(
                value["parameterSort"]
            )
        }
    else:
        raise SerializationError("SearchSortExpression: no variant present")


def deserialize_json(data: dict) -> SearchSortExpression:
    if data.get("userJobsFirst") is not None:
        import capo_deadline.types.user_jobs_first

        return {
            "userJobsFirst": capo_deadline.types.user_jobs_first.deserialize_json(
                data["userJobsFirst"]
            )
        }
    elif data.get("fieldSort") is not None:
        import capo_deadline.types.field_sort_expression

        return {
            "fieldSort": capo_deadline.types.field_sort_expression.deserialize_json(
                data["fieldSort"]
            )
        }
    elif data.get("parameterSort") is not None:
        import capo_deadline.types.parameter_sort_expression

        return {
            "parameterSort": capo_deadline.types.parameter_sort_expression.deserialize_json(
                data["parameterSort"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SearchSortExpression: no recognized variant key")
