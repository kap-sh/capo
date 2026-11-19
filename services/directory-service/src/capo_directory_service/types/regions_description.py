"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegionsDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.region_description

RegionsDescription: TypeAlias = list[
    "capo_directory_service.types.region_description.RegionDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionsDescription) -> list:
    import capo_directory_service.types.region_description

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.region_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegionsDescription:
    import capo_directory_service.types.region_description

    out: RegionsDescription = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.region_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegionsDescription) -> list:
    import capo_directory_service.types.region_description

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.region_description.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RegionsDescription:
    import capo_directory_service.types.region_description

    out: RegionsDescription = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.region_description.deserialize_cbor(item)
        )
    return out
