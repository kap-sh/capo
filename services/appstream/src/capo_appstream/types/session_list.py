"""Generated from Smithy shape ``com.amazonaws.appstream#SessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.session

SessionList: TypeAlias = list["capo_appstream.types.session.Session"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionList) -> list:
    import capo_appstream.types.session

    out: list = []
    for item in value:
        out.append(capo_appstream.types.session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SessionList:
    import capo_appstream.types.session

    out: SessionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.session.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SessionList) -> list:
    import capo_appstream.types.session

    out: list = []
    for item in value:
        out.append(capo_appstream.types.session.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SessionList:
    import capo_appstream.types.session

    out: SessionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.session.deserialize_cbor(item))
    return out
