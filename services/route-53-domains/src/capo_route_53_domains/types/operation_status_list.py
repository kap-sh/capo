"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.operation_status

OperationStatusList: TypeAlias = list[
    "capo_route_53_domains.types.operation_status.OperationStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationStatusList) -> list:
    import capo_route_53_domains.types.operation_status

    out: list = []
    for item in value:
        out.append(
            capo_route_53_domains.types.operation_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperationStatusList:
    import capo_route_53_domains.types.operation_status

    out: OperationStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route_53_domains.types.operation_status.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationStatusList) -> list:
    import capo_route_53_domains.types.operation_status

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.operation_status.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OperationStatusList:
    import capo_route_53_domains.types.operation_status

    out: OperationStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_route_53_domains.types.operation_status.deserialize_cbor(item))
    return out
