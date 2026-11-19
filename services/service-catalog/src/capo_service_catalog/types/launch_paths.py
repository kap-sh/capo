"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LaunchPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.launch_path

LaunchPaths: TypeAlias = list["capo_service_catalog.types.launch_path.LaunchPath"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaunchPaths) -> list:
    import capo_service_catalog.types.launch_path

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.launch_path.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LaunchPaths:
    import capo_service_catalog.types.launch_path

    out: LaunchPaths = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.launch_path.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LaunchPaths) -> list:
    import capo_service_catalog.types.launch_path

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.launch_path.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LaunchPaths:
    import capo_service_catalog.types.launch_path

    out: LaunchPaths = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.launch_path.deserialize_cbor(item))
    return out
