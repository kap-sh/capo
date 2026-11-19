"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConfigurationSettingRequestDetailedStatus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.directory_configuration_status
    import capo_directory_service.types.region_name

DirectoryConfigurationSettingRequestDetailedStatus: TypeAlias = dict[
    "capo_directory_service.types.region_name.RegionName",
    "capo_directory_service.types.directory_configuration_status.DirectoryConfigurationStatus",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: DirectoryConfigurationSettingRequestDetailedStatus,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_directory_service.types.directory_configuration_status

        out[key] = (
            capo_directory_service.types.directory_configuration_status.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DirectoryConfigurationSettingRequestDetailedStatus:
    out: DirectoryConfigurationSettingRequestDetailedStatus = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_directory_service.types.directory_configuration_status

        out[key] = (
            capo_directory_service.types.directory_configuration_status.deserialize_aws_json_1_1(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(
    input_to_serialize: DirectoryConfigurationSettingRequestDetailedStatus,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_directory_service.types.directory_configuration_status

        out[key] = (
            capo_directory_service.types.directory_configuration_status.serialize_cbor(
                value
            )
        )
    return out


def deserialize_cbor(data: dict) -> DirectoryConfigurationSettingRequestDetailedStatus:
    out: DirectoryConfigurationSettingRequestDetailedStatus = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_directory_service.types.directory_configuration_status

        out[key] = (
            capo_directory_service.types.directory_configuration_status.deserialize_cbor(
                value
            )
        )
    return out
