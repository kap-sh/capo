"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#PlanWarnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.resource_warning

PlanWarnings: TypeAlias = list[
    "capo_arc_region_switch.types.resource_warning.ResourceWarning"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PlanWarnings) -> list:
    import capo_arc_region_switch.types.resource_warning

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.resource_warning.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PlanWarnings:
    import capo_arc_region_switch.types.resource_warning

    out: PlanWarnings = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.resource_warning.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlanWarnings) -> list:
    import capo_arc_region_switch.types.resource_warning

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.resource_warning.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PlanWarnings:
    import capo_arc_region_switch.types.resource_warning

    out: PlanWarnings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.resource_warning.deserialize_cbor(item))
    return out
