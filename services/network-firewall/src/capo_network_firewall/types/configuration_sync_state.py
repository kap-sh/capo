"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ConfigurationSyncState``."""

from typing import Literal, TypeAlias, cast

ConfigurationSyncState: TypeAlias = Literal[
    "PENDING",
    "IN_SYNC",
    "CAPACITY_CONSTRAINED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationSyncState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConfigurationSyncState:
    return cast(ConfigurationSyncState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigurationSyncState) -> str:
    return value


def deserialize_cbor(data: str) -> ConfigurationSyncState:
    return cast(ConfigurationSyncState, data)
