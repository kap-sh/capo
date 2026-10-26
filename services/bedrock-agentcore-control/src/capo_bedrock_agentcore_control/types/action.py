"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Action``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_action
    import capo_bedrock_agentcore_control.types.route_to_target_action


class _Action_configurationBundle(TypedDict, closed=True):
    configurationBundle: "capo_bedrock_agentcore_control.types.configuration_bundle_action.ConfigurationBundleAction"


class _Action_routeToTarget(TypedDict, closed=True):
    routeToTarget: "capo_bedrock_agentcore_control.types.route_to_target_action.RouteToTargetAction"


Action: TypeAlias = (
    _Action_configurationBundle | _Action_routeToTarget | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Action: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "configurationBundle" in value:
        import capo_bedrock_agentcore_control.types.configuration_bundle_action

        return {
            "configurationBundle": capo_bedrock_agentcore_control.types.configuration_bundle_action.serialize_json(
                value["configurationBundle"]
            )
        }
    elif "routeToTarget" in value:
        import capo_bedrock_agentcore_control.types.route_to_target_action

        return {
            "routeToTarget": capo_bedrock_agentcore_control.types.route_to_target_action.serialize_json(
                value["routeToTarget"]
            )
        }
    else:
        raise SerializationError("Action: no variant present")


def deserialize_json(data: dict) -> Action:
    if data.get("configurationBundle") is not None:
        import capo_bedrock_agentcore_control.types.configuration_bundle_action

        return {
            "configurationBundle": capo_bedrock_agentcore_control.types.configuration_bundle_action.deserialize_json(
                data["configurationBundle"]
            )
        }
    elif data.get("routeToTarget") is not None:
        import capo_bedrock_agentcore_control.types.route_to_target_action

        return {
            "routeToTarget": capo_bedrock_agentcore_control.types.route_to_target_action.deserialize_json(
                data["routeToTarget"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Action: no recognized variant key")


def redact_sensitive(value: Action) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "routeToTarget" in value:
        import capo_bedrock_agentcore_control.types.route_to_target_action

        out["routeToTarget"] = (
            capo_bedrock_agentcore_control.types.route_to_target_action.redact_sensitive(
                value["routeToTarget"]
            )
        )
    return out
