"""Generated from Smithy shape ``com.amazonaws.directoryservice#DomainControllers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.domain_controller

DomainControllers: TypeAlias = list[
    "capo_directory_service.types.domain_controller.DomainController"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainControllers) -> list:
    import capo_directory_service.types.domain_controller

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.domain_controller.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DomainControllers:
    import capo_directory_service.types.domain_controller

    out: DomainControllers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.domain_controller.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainControllers) -> list:
    import capo_directory_service.types.domain_controller

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.domain_controller.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DomainControllers:
    import capo_directory_service.types.domain_controller

    out: DomainControllers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.domain_controller.deserialize_cbor(item)
        )
    return out
