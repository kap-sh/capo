"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConfigurationSettingLastUpdatedDateTime``."""

import datetime
from typing import TypeAlias

DirectoryConfigurationSettingLastUpdatedDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DirectoryConfigurationSettingLastUpdatedDateTime,
) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(
    data: float,
) -> DirectoryConfigurationSettingLastUpdatedDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(
    value: DirectoryConfigurationSettingLastUpdatedDateTime,
) -> DirectoryConfigurationSettingLastUpdatedDateTime:
    return value


def deserialize_cbor(
    data: DirectoryConfigurationSettingLastUpdatedDateTime,
) -> DirectoryConfigurationSettingLastUpdatedDateTime:
    return data
