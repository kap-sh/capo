"""Generated from Smithy shape ``com.amazonaws.route53domains#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.value

Values: TypeAlias = list["capo_route_53_domains.types.value.Value"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Values) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Values:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Values) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Values:
    return [item for item in data if item is not None]
