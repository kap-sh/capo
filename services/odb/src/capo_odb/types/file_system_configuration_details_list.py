"""Generated from Smithy shape ``com.amazonaws.odb#FileSystemConfigurationDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.file_system_configuration_details

FileSystemConfigurationDetailsList: TypeAlias = list[
    "capo_odb.types.file_system_configuration_details.FileSystemConfigurationDetails"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileSystemConfigurationDetailsList) -> list:
    import capo_odb.types.file_system_configuration_details

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.file_system_configuration_details.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FileSystemConfigurationDetailsList:
    import capo_odb.types.file_system_configuration_details

    out: FileSystemConfigurationDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_odb.types.file_system_configuration_details.deserialize_aws_json_1_0(
                item
            )
        )
    return out
