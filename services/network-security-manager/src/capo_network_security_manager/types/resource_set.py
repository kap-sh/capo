"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.resource_arn_list
    import capo_network_security_manager.types.resource_logical_expression


class ResourceSet(TypedDict, closed=True):
    explicit_arns: NotRequired[
        "capo_network_security_manager.types.resource_arn_list.ResourceArnList"
    ]
    """<p>An explicit list of resource ARNs.</p>"""
    expression: NotRequired[
        "capo_network_security_manager.types.resource_logical_expression.ResourceLogicalExpression"
    ]
    """<p>A logical expression that selects resources by combining criteria with AND, OR, and NOT operators.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSet) -> dict:
    out: dict = {}
    if "explicit_arns" in value:
        import capo_network_security_manager.types.resource_arn_list

        out["explicitArns"] = (
            capo_network_security_manager.types.resource_arn_list.serialize_json(
                value["explicit_arns"]
            )
        )
    if "expression" in value:
        import capo_network_security_manager.types.resource_logical_expression

        out["expression"] = (
            capo_network_security_manager.types.resource_logical_expression.serialize_json(
                value["expression"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceSet:
    out: ResourceSet = {}  # type: ignore[typeddict-item]
    if data.get("explicitArns") is not None:
        import capo_network_security_manager.types.resource_arn_list

        out["explicit_arns"] = (
            capo_network_security_manager.types.resource_arn_list.deserialize_json(
                data["explicitArns"]
            )
        )
    if data.get("expression") is not None:
        import capo_network_security_manager.types.resource_logical_expression

        out["expression"] = (
            capo_network_security_manager.types.resource_logical_expression.deserialize_json(
                data["expression"]
            )
        )
    return out
