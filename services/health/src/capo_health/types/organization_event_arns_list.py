"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_arn

OrganizationEventArnsList: TypeAlias = list["capo_health.types.event_arn.eventArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventArnsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationEventArnsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationEventArnsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> OrganizationEventArnsList:
    return [item for item in data if item is not None]
