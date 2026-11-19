"""Generated from Smithy shape ``com.amazonaws.backupgateway#DaysOfWeek``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup_gateway.types.day_of_week

DaysOfWeek: TypeAlias = list["capo_backup_gateway.types.day_of_week.DayOfWeek"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DaysOfWeek) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> DaysOfWeek:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DaysOfWeek) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DaysOfWeek:
    return [item for item in data if item is not None]
