"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceLogicalExpressionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.resource_logical_expression

ResourceLogicalExpressionList: TypeAlias = list[
    "capo_network_security_manager.types.resource_logical_expression.ResourceLogicalExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLogicalExpressionList) -> list:
    import capo_network_security_manager.types.resource_logical_expression

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.resource_logical_expression.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourceLogicalExpressionList:
    import capo_network_security_manager.types.resource_logical_expression

    out: ResourceLogicalExpressionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.resource_logical_expression.deserialize_json(
                item
            )
        )
    return out
