"""Generated from Smithy shape ``com.amazonaws.fms#AppsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.app

AppsList: TypeAlias = list["capo_fms.types.app.App"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppsList) -> list:
    import capo_fms.types.app

    out: list = []
    for item in value:
        out.append(capo_fms.types.app.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppsList:
    import capo_fms.types.app

    out: AppsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.app.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppsList) -> list:
    import capo_fms.types.app

    out: list = []
    for item in value:
        out.append(capo_fms.types.app.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AppsList:
    import capo_fms.types.app

    out: AppsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.app.deserialize_cbor(item))
    return out
