"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_status

DomainStatusList: TypeAlias = list[
    "capo_route_53_domains.types.domain_status.DomainStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainStatusList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DomainStatusList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainStatusList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DomainStatusList:
    return [item for item in data if item is not None]
