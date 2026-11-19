"""Generated from Smithy shape ``com.amazonaws.gamelift#RoutingStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.free_text
    import capo_gamelift.types.routing_strategy_type


class RoutingStrategy(TypedDict, closed=True):
    type: NotRequired["capo_gamelift.types.routing_strategy_type.RoutingStrategyType"]
    """<p>The type of routing strategy for the alias.</p> <p>Possible routing types include the following:</p> <ul> <li> <p> <b>SIMPLE</b> - The alias resolves to one specific fleet. Use this type when routing to active fleets.</p> </li> <li> <p> <b>TERMINAL</b> - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the message embedded.</p> </li> </ul>"""
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that the alias points to. This value is the fleet ID, not the fleet ARN.</p>"""
    message: NotRequired["capo_gamelift.types.free_text.FreeText"]
    """<p>The message text to be used with a terminal routing strategy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingStrategy) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_gamelift.types.routing_strategy_type

        out["Type"] = capo_gamelift.types.routing_strategy_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RoutingStrategy:
    out: RoutingStrategy = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_gamelift.types.routing_strategy_type

        out["type"] = (
            capo_gamelift.types.routing_strategy_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RoutingStrategy) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_gamelift.types.routing_strategy_type

        out["Type"] = capo_gamelift.types.routing_strategy_type.serialize_cbor(
            value["type"]
        )
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> RoutingStrategy:
    out: RoutingStrategy = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_gamelift.types.routing_strategy_type

        out["type"] = capo_gamelift.types.routing_strategy_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
