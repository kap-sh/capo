"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CapacityReservationPreferenceEnum``."""

from typing import Literal, TypeAlias, cast

CapacityReservationPreferenceEnum: TypeAlias = Literal[
    "capacity-reservations-only",
    "open",
    "none",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityReservationPreferenceEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CapacityReservationPreferenceEnum:
    return cast(CapacityReservationPreferenceEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CapacityReservationPreferenceEnum) -> str:
    return value


def deserialize_cbor(data: str) -> CapacityReservationPreferenceEnum:
    return cast(CapacityReservationPreferenceEnum, data)
