"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceLogicalExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_network_security_manager.types.resource_criteria
    import capo_network_security_manager.types.resource_logical_expression
    import capo_network_security_manager.types.resource_logical_expression_list


class _ResourceLogicalExpression_criteria(TypedDict, closed=True):
    criteria: "capo_network_security_manager.types.resource_criteria.ResourceCriteria"


_ResourceLogicalExpression_and = TypedDict(
    "_ResourceLogicalExpression_and",
    {
        "and": "capo_network_security_manager.types.resource_logical_expression_list.ResourceLogicalExpressionList",
    },
    closed=True,
)
_ResourceLogicalExpression_or = TypedDict(
    "_ResourceLogicalExpression_or",
    {
        "or": "capo_network_security_manager.types.resource_logical_expression_list.ResourceLogicalExpressionList",
    },
    closed=True,
)
_ResourceLogicalExpression_not = TypedDict(
    "_ResourceLogicalExpression_not",
    {
        "not": "capo_network_security_manager.types.resource_logical_expression.ResourceLogicalExpression",
    },
    closed=True,
)

ResourceLogicalExpression: TypeAlias = (
    _ResourceLogicalExpression_criteria
    | _ResourceLogicalExpression_and
    | _ResourceLogicalExpression_or
    | _ResourceLogicalExpression_not
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLogicalExpression) -> dict:
    if "criteria" in value:
        import capo_network_security_manager.types.resource_criteria

        return {
            "criteria": capo_network_security_manager.types.resource_criteria.serialize_json(
                value["criteria"]
            )
        }
    elif "and" in value:
        import capo_network_security_manager.types.resource_logical_expression_list

        return {
            "and": capo_network_security_manager.types.resource_logical_expression_list.serialize_json(
                value["and"]
            )
        }
    elif "or" in value:
        import capo_network_security_manager.types.resource_logical_expression_list

        return {
            "or": capo_network_security_manager.types.resource_logical_expression_list.serialize_json(
                value["or"]
            )
        }
    elif "not" in value:
        import capo_network_security_manager.types.resource_logical_expression

        return {
            "not": capo_network_security_manager.types.resource_logical_expression.serialize_json(
                value["not"]
            )
        }
    else:
        raise SerializationError("ResourceLogicalExpression: no variant present")


def deserialize_json(data: dict) -> ResourceLogicalExpression:
    if data.get("criteria") is not None:
        import capo_network_security_manager.types.resource_criteria

        return {
            "criteria": capo_network_security_manager.types.resource_criteria.deserialize_json(
                data["criteria"]
            )
        }
    elif data.get("and") is not None:
        import capo_network_security_manager.types.resource_logical_expression_list

        return {
            "and": capo_network_security_manager.types.resource_logical_expression_list.deserialize_json(
                data["and"]
            )
        }
    elif data.get("or") is not None:
        import capo_network_security_manager.types.resource_logical_expression_list

        return {
            "or": capo_network_security_manager.types.resource_logical_expression_list.deserialize_json(
                data["or"]
            )
        }
    elif data.get("not") is not None:
        import capo_network_security_manager.types.resource_logical_expression

        return {
            "not": capo_network_security_manager.types.resource_logical_expression.deserialize_json(
                data["not"]
            )
        }
    else:
        raise DeserializationError(
            "ResourceLogicalExpression: no recognized variant key"
        )
