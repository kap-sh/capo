"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AbbreviatedExecutionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.abbreviated_execution

AbbreviatedExecutionsList: TypeAlias = list[
    "capo_arc_region_switch.types.abbreviated_execution.AbbreviatedExecution"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AbbreviatedExecutionsList) -> list:
    import capo_arc_region_switch.types.abbreviated_execution

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.abbreviated_execution.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AbbreviatedExecutionsList:
    import capo_arc_region_switch.types.abbreviated_execution

    out: AbbreviatedExecutionsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.abbreviated_execution.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AbbreviatedExecutionsList) -> list:
    import capo_arc_region_switch.types.abbreviated_execution

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.abbreviated_execution.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AbbreviatedExecutionsList:
    import capo_arc_region_switch.types.abbreviated_execution

    out: AbbreviatedExecutionsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.abbreviated_execution.deserialize_cbor(item)
        )
    return out
