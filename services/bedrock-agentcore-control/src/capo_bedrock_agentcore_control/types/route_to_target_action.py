"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RouteToTargetAction``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.static_route
    import capo_bedrock_agentcore_control.types.weighted_route


class RouteToTargetActionStaticRouteMember(TypedDict, closed=True):
    staticRoute: "capo_bedrock_agentcore_control.types.static_route.StaticRoute"


class RouteToTargetActionWeightedRouteMember(TypedDict, closed=True):
    weightedRoute: "capo_bedrock_agentcore_control.types.weighted_route.WeightedRoute"


RouteToTargetAction: TypeAlias = (
    RouteToTargetActionStaticRouteMember
    | RouteToTargetActionWeightedRouteMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouteToTargetAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouteToTargetAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "staticRoute" in value:
        import capo_bedrock_agentcore_control.types.static_route

        return {
            "staticRoute": capo_bedrock_agentcore_control.types.static_route.serialize_json(
                value["staticRoute"]
            )
        }
    elif "weightedRoute" in value:
        import capo_bedrock_agentcore_control.types.weighted_route

        return {
            "weightedRoute": capo_bedrock_agentcore_control.types.weighted_route.serialize_json(
                value["weightedRoute"]
            )
        }
    else:
        raise SerializationError("RouteToTargetAction: no variant present")


def deserialize_json(data: dict) -> RouteToTargetAction:
    if data.get("staticRoute") is not None:
        import capo_bedrock_agentcore_control.types.static_route

        return {
            "staticRoute": capo_bedrock_agentcore_control.types.static_route.deserialize_json(
                data["staticRoute"]
            )
        }
    elif data.get("weightedRoute") is not None:
        import capo_bedrock_agentcore_control.types.weighted_route

        return {
            "weightedRoute": capo_bedrock_agentcore_control.types.weighted_route.deserialize_json(
                data["weightedRoute"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RouteToTargetAction: no recognized variant key")


def redact_sensitive(value: RouteToTargetAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "staticRoute" in value:
        import capo_bedrock_agentcore_control.types.static_route

        out["staticRoute"] = (
            capo_bedrock_agentcore_control.types.static_route.redact_sensitive(
                value["staticRoute"]
            )
        )
    if "weightedRoute" in value:
        import capo_bedrock_agentcore_control.types.weighted_route

        out["weightedRoute"] = (
            capo_bedrock_agentcore_control.types.weighted_route.redact_sensitive(
                value["weightedRoute"]
            )
        )
    return out
