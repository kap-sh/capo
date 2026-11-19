"""Generated from Smithy shape ``com.amazonaws.route53domains#DnssecKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.dnssec_key

DnssecKeyList: TypeAlias = list["capo_route_53_domains.types.dnssec_key.DnssecKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnssecKeyList) -> list:
    import capo_route_53_domains.types.dnssec_key

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.dnssec_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DnssecKeyList:
    import capo_route_53_domains.types.dnssec_key

    out: DnssecKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route_53_domains.types.dnssec_key.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DnssecKeyList) -> list:
    import capo_route_53_domains.types.dnssec_key

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.dnssec_key.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DnssecKeyList:
    import capo_route_53_domains.types.dnssec_key

    out: DnssecKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_route_53_domains.types.dnssec_key.deserialize_cbor(item))
    return out
