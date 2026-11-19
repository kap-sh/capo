"""Generated from Smithy shape ``com.amazonaws.fms#Routes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.route

Routes: TypeAlias = list["capo_fms.types.route.Route"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Routes) -> list:
    import capo_fms.types.route

    out: list = []
    for item in value:
        out.append(capo_fms.types.route.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Routes:
    import capo_fms.types.route

    out: Routes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.route.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Routes) -> list:
    import capo_fms.types.route

    out: list = []
    for item in value:
        out.append(capo_fms.types.route.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Routes:
    import capo_fms.types.route

    out: Routes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.route.deserialize_cbor(item))
    return out
