"""Generated from Smithy shape ``com.amazonaws.snowball#DependentServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.dependent_service

DependentServiceList: TypeAlias = list[
    "capo_snowball.types.dependent_service.DependentService"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentServiceList) -> list:
    import capo_snowball.types.dependent_service

    out: list = []
    for item in value:
        out.append(capo_snowball.types.dependent_service.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DependentServiceList:
    import capo_snowball.types.dependent_service

    out: DependentServiceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.dependent_service.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DependentServiceList) -> list:
    import capo_snowball.types.dependent_service

    out: list = []
    for item in value:
        out.append(capo_snowball.types.dependent_service.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DependentServiceList:
    import capo_snowball.types.dependent_service

    out: DependentServiceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.dependent_service.deserialize_cbor(item))
    return out
