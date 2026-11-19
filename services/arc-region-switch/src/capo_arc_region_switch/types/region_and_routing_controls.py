"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionAndRoutingControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.arc_routing_control_states

RegionAndRoutingControls: TypeAlias = dict[
    "str",
    "capo_arc_region_switch.types.arc_routing_control_states.ArcRoutingControlStates",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionAndRoutingControls) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.arc_routing_control_states

        out[key] = (
            capo_arc_region_switch.types.arc_routing_control_states.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionAndRoutingControls:
    out: RegionAndRoutingControls = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_arc_region_switch.types.arc_routing_control_states

        out[key] = (
            capo_arc_region_switch.types.arc_routing_control_states.deserialize_aws_json_1_0(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: RegionAndRoutingControls) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.arc_routing_control_states

        out[key] = (
            capo_arc_region_switch.types.arc_routing_control_states.serialize_cbor(
                value
            )
        )
    return out


def deserialize_cbor(data: dict) -> RegionAndRoutingControls:
    out: RegionAndRoutingControls = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_arc_region_switch.types.arc_routing_control_states

        out[key] = (
            capo_arc_region_switch.types.arc_routing_control_states.deserialize_cbor(
                value
            )
        )
    return out
