"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceLogicalExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_network_security_manager.types.resource_criteria
    import capo_network_security_manager.types.resource_logical_expression
    import capo_network_security_manager.types.resource_logical_expression_list


class ResourceLogicalExpressionCriteriaMember(TypedDict, closed=True):
    criteria: "capo_network_security_manager.types.resource_criteria.ResourceCriteria"


ResourceLogicalExpressionAndMember = TypedDict(
    "ResourceLogicalExpressionAndMember",
    {
        "and": "capo_network_security_manager.types.resource_logical_expression_list.ResourceLogicalExpressionList",
    },
    closed=True,
)
ResourceLogicalExpressionOrMember = TypedDict(
    "ResourceLogicalExpressionOrMember",
    {
        "or": "capo_network_security_manager.types.resource_logical_expression_list.ResourceLogicalExpressionList",
    },
    closed=True,
)
ResourceLogicalExpressionNotMember = TypedDict(
    "ResourceLogicalExpressionNotMember",
    {
        "not": "capo_network_security_manager.types.resource_logical_expression.ResourceLogicalExpression",
    },
    closed=True,
)

ResourceLogicalExpression: TypeAlias = (
    ResourceLogicalExpressionCriteriaMember
    | ResourceLogicalExpressionAndMember
    | ResourceLogicalExpressionOrMember
    | ResourceLogicalExpressionNotMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLogicalExpression) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResourceLogicalExpression: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "criteria" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ResourceLogicalExpression: no recognized variant key"
        )
