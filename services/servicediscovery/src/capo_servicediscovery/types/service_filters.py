"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.service_filter

ServiceFilters: TypeAlias = list[
    "capo_servicediscovery.types.service_filter.ServiceFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceFilters) -> list:
    import capo_servicediscovery.types.service_filter

    out: list = []
    for item in value:
        out.append(
            capo_servicediscovery.types.service_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceFilters:
    import capo_servicediscovery.types.service_filter

    out: ServiceFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_servicediscovery.types.service_filter.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceFilters) -> list:
    import capo_servicediscovery.types.service_filter

    out: list = []
    for item in value:
        out.append(capo_servicediscovery.types.service_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ServiceFilters:
    import capo_servicediscovery.types.service_filter

    out: ServiceFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_servicediscovery.types.service_filter.deserialize_cbor(item))
    return out
