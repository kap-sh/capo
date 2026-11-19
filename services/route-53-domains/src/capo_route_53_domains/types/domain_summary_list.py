"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_summary

DomainSummaryList: TypeAlias = list[
    "capo_route_53_domains.types.domain_summary.DomainSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainSummaryList) -> list:
    import capo_route_53_domains.types.domain_summary

    out: list = []
    for item in value:
        out.append(
            capo_route_53_domains.types.domain_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DomainSummaryList:
    import capo_route_53_domains.types.domain_summary

    out: DomainSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route_53_domains.types.domain_summary.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainSummaryList) -> list:
    import capo_route_53_domains.types.domain_summary

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.domain_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DomainSummaryList:
    import capo_route_53_domains.types.domain_summary

    out: DomainSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_route_53_domains.types.domain_summary.deserialize_cbor(item))
    return out
