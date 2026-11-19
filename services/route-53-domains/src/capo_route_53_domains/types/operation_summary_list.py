"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.operation_summary

OperationSummaryList: TypeAlias = list[
    "capo_route_53_domains.types.operation_summary.OperationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationSummaryList) -> list:
    import capo_route_53_domains.types.operation_summary

    out: list = []
    for item in value:
        out.append(
            capo_route_53_domains.types.operation_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperationSummaryList:
    import capo_route_53_domains.types.operation_summary

    out: OperationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route_53_domains.types.operation_summary.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationSummaryList) -> list:
    import capo_route_53_domains.types.operation_summary

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.operation_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OperationSummaryList:
    import capo_route_53_domains.types.operation_summary

    out: OperationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_route_53_domains.types.operation_summary.deserialize_cbor(item))
    return out
