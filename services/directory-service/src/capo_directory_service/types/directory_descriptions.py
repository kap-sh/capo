"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryDescriptions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.directory_description

DirectoryDescriptions: TypeAlias = list[
    "capo_directory_service.types.directory_description.DirectoryDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryDescriptions) -> list:
    import capo_directory_service.types.directory_description

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.directory_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DirectoryDescriptions:
    import capo_directory_service.types.directory_description

    out: DirectoryDescriptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.directory_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryDescriptions) -> list:
    import capo_directory_service.types.directory_description

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.directory_description.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> DirectoryDescriptions:
    import capo_directory_service.types.directory_description

    out: DirectoryDescriptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.directory_description.deserialize_cbor(item)
        )
    return out


def redact_sensitive(value: DirectoryDescriptions) -> list[Any]:
    import capo_directory_service.types.directory_description

    return [
        capo_directory_service.types.directory_description.redact_sensitive(item)
        for item in value
    ]
