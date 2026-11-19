"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.operation_type

OperationTypeList: TypeAlias = list[
    "capo_route_53_domains.types.operation_type.OperationType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationTypeList) -> list:
    import capo_route_53_domains.types.operation_type

    out: list = []
    for item in value:
        out.append(
            capo_route_53_domains.types.operation_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperationTypeList:
    import capo_route_53_domains.types.operation_type

    out: OperationTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route_53_domains.types.operation_type.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationTypeList) -> list:
    import capo_route_53_domains.types.operation_type

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.operation_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OperationTypeList:
    import capo_route_53_domains.types.operation_type

    out: OperationTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_route_53_domains.types.operation_type.deserialize_cbor(item))
    return out
