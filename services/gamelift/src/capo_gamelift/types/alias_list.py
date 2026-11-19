"""Generated from Smithy shape ``com.amazonaws.gamelift#AliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.alias

AliasList: TypeAlias = list["capo_gamelift.types.alias.Alias"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasList) -> list:
    import capo_gamelift.types.alias

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.alias.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AliasList:
    import capo_gamelift.types.alias

    out: AliasList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.alias.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AliasList) -> list:
    import capo_gamelift.types.alias

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.alias.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AliasList:
    import capo_gamelift.types.alias

    out: AliasList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.alias.deserialize_cbor(item))
    return out
