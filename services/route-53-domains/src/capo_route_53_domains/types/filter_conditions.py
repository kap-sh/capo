"""Generated from Smithy shape ``com.amazonaws.route53domains#FilterConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.filter_condition

FilterConditions: TypeAlias = list[
    "capo_route_53_domains.types.filter_condition.FilterCondition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterConditions) -> list:
    import capo_route_53_domains.types.filter_condition

    out: list = []
    for item in value:
        out.append(
            capo_route_53_domains.types.filter_condition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FilterConditions:
    import capo_route_53_domains.types.filter_condition

    out: FilterConditions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route_53_domains.types.filter_condition.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterConditions) -> list:
    import capo_route_53_domains.types.filter_condition

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.filter_condition.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FilterConditions:
    import capo_route_53_domains.types.filter_condition

    out: FilterConditions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_route_53_domains.types.filter_condition.deserialize_cbor(item))
    return out
