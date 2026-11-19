"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_point

IngressPointsList: TypeAlias = list["capo_mailmanager.types.ingress_point.IngressPoint"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointsList) -> list:
    import capo_mailmanager.types.ingress_point

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.ingress_point.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> IngressPointsList:
    import capo_mailmanager.types.ingress_point

    out: IngressPointsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.ingress_point.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressPointsList) -> list:
    import capo_mailmanager.types.ingress_point

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.ingress_point.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IngressPointsList:
    import capo_mailmanager.types.ingress_point

    out: IngressPointsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.ingress_point.deserialize_cbor(item))
    return out
