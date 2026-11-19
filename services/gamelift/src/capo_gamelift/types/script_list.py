"""Generated from Smithy shape ``com.amazonaws.gamelift#ScriptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.script

ScriptList: TypeAlias = list["capo_gamelift.types.script.Script"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScriptList) -> list:
    import capo_gamelift.types.script

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.script.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ScriptList:
    import capo_gamelift.types.script

    out: ScriptList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.script.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScriptList) -> list:
    import capo_gamelift.types.script

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.script.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ScriptList:
    import capo_gamelift.types.script

    out: ScriptList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.script.deserialize_cbor(item))
    return out
