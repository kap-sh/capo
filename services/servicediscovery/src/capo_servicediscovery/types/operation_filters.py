"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.operation_filter

OperationFilters: TypeAlias = list[
    "capo_servicediscovery.types.operation_filter.OperationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationFilters) -> list:
    import capo_servicediscovery.types.operation_filter

    out: list = []
    for item in value:
        out.append(
            capo_servicediscovery.types.operation_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperationFilters:
    import capo_servicediscovery.types.operation_filter

    out: OperationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_servicediscovery.types.operation_filter.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationFilters) -> list:
    import capo_servicediscovery.types.operation_filter

    out: list = []
    for item in value:
        out.append(capo_servicediscovery.types.operation_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OperationFilters:
    import capo_servicediscovery.types.operation_filter

    out: OperationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_servicediscovery.types.operation_filter.deserialize_cbor(item))
    return out
