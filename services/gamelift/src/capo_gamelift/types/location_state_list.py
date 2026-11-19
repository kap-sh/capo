"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.location_state

LocationStateList: TypeAlias = list["capo_gamelift.types.location_state.LocationState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationStateList) -> list:
    import capo_gamelift.types.location_state

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.location_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationStateList:
    import capo_gamelift.types.location_state

    out: LocationStateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.location_state.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationStateList) -> list:
    import capo_gamelift.types.location_state

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.location_state.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LocationStateList:
    import capo_gamelift.types.location_state

    out: LocationStateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.location_state.deserialize_cbor(item))
    return out
