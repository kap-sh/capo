"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionEventSourceMappingMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.event_source_mapping
    import capo_arc_region_switch.types.region

RegionEventSourceMappingMap: TypeAlias = dict[
    "capo_arc_region_switch.types.region.Region",
    "capo_arc_region_switch.types.event_source_mapping.EventSourceMapping",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionEventSourceMappingMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.event_source_mapping

        out[key] = (
            capo_arc_region_switch.types.event_source_mapping.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionEventSourceMappingMap:
    out: RegionEventSourceMappingMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_arc_region_switch.types.event_source_mapping

        out[key] = (
            capo_arc_region_switch.types.event_source_mapping.deserialize_aws_json_1_0(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: RegionEventSourceMappingMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.event_source_mapping

        out[key] = capo_arc_region_switch.types.event_source_mapping.serialize_cbor(
            value
        )
    return out


def deserialize_cbor(data: dict) -> RegionEventSourceMappingMap:
    out: RegionEventSourceMappingMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_arc_region_switch.types.event_source_mapping

        out[key] = capo_arc_region_switch.types.event_source_mapping.deserialize_cbor(
            value
        )
    return out
