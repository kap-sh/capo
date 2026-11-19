"""Generated from Smithy shape ``com.amazonaws.route53domains#NameserverList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.nameserver

NameserverList: TypeAlias = list["capo_route_53_domains.types.nameserver.Nameserver"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NameserverList) -> list:
    import capo_route_53_domains.types.nameserver

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.nameserver.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NameserverList:
    import capo_route_53_domains.types.nameserver

    out: NameserverList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route_53_domains.types.nameserver.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NameserverList) -> list:
    import capo_route_53_domains.types.nameserver

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.nameserver.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> NameserverList:
    import capo_route_53_domains.types.nameserver

    out: NameserverList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_route_53_domains.types.nameserver.deserialize_cbor(item))
    return out
