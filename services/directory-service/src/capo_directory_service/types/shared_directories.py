"""Generated from Smithy shape ``com.amazonaws.directoryservice#SharedDirectories``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.shared_directory

SharedDirectories: TypeAlias = list[
    "capo_directory_service.types.shared_directory.SharedDirectory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharedDirectories) -> list:
    import capo_directory_service.types.shared_directory

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.shared_directory.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SharedDirectories:
    import capo_directory_service.types.shared_directory

    out: SharedDirectories = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.shared_directory.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: SharedDirectories) -> list[Any]:
    import capo_directory_service.types.shared_directory

    return [
        capo_directory_service.types.shared_directory.redact_sensitive(item)
        for item in value
    ]
