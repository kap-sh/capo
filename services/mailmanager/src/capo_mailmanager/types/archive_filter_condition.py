"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveFilterCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_boolean_expression
    import capo_mailmanager.types.archive_string_expression


class ArchiveFilterConditionStringExpressionMember(TypedDict, closed=True):
    StringExpression: (
        "capo_mailmanager.types.archive_string_expression.ArchiveStringExpression"
    )


class ArchiveFilterConditionBooleanExpressionMember(TypedDict, closed=True):
    BooleanExpression: (
        "capo_mailmanager.types.archive_boolean_expression.ArchiveBooleanExpression"
    )


ArchiveFilterCondition: TypeAlias = (
    ArchiveFilterConditionStringExpressionMember
    | ArchiveFilterConditionBooleanExpressionMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveFilterCondition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ArchiveFilterCondition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "StringExpression" in value:
        import capo_mailmanager.types.archive_string_expression

        return {
            "StringExpression": capo_mailmanager.types.archive_string_expression.serialize_aws_json_1_0(
                value["StringExpression"]
            )
        }
    elif "BooleanExpression" in value:
        import capo_mailmanager.types.archive_boolean_expression

        return {
            "BooleanExpression": capo_mailmanager.types.archive_boolean_expression.serialize_aws_json_1_0(
                value["BooleanExpression"]
            )
        }
    else:
        raise SerializationError("ArchiveFilterCondition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ArchiveFilterCondition:
    if data.get("StringExpression") is not None:
        import capo_mailmanager.types.archive_string_expression

        return {
            "StringExpression": capo_mailmanager.types.archive_string_expression.deserialize_aws_json_1_0(
                data["StringExpression"]
            )
        }
    elif data.get("BooleanExpression") is not None:
        import capo_mailmanager.types.archive_boolean_expression

        return {
            "BooleanExpression": capo_mailmanager.types.archive_boolean_expression.deserialize_aws_json_1_0(
                data["BooleanExpression"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ArchiveFilterCondition: no recognized variant key")
