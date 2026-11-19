"""Generated from Smithy shape ``com.amazonaws.servicecatalog#NotificationArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.notification_arn

NotificationArns: TypeAlias = list[
    "capo_service_catalog.types.notification_arn.NotificationArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NotificationArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NotificationArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> NotificationArns:
    return [item for item in data if item is not None]
