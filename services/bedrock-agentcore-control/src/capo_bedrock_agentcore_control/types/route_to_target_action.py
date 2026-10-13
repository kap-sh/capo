"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RouteToTargetAction``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.static_route
    import capo_bedrock_agentcore_control.types.weighted_route


class _RouteToTargetAction_staticRoute(TypedDict, closed=True):
    staticRoute: "capo_bedrock_agentcore_control.types.static_route.StaticRoute"


class _RouteToTargetAction_weightedRoute(TypedDict, closed=True):
    weightedRoute: "capo_bedrock_agentcore_control.types.weighted_route.WeightedRoute"


RouteToTargetAction: TypeAlias = (
    _RouteToTargetAction_staticRoute | _RouteToTargetAction_weightedRoute
)


# --- restJson1 ser/de ---
def serialize_json(value: RouteToTargetAction) -> dict:
    if "staticRoute" in value:
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
