"""Generated from Smithy shape ``com.amazonaws.workspaces#StreamingExperiencePreferredProtocolEnum``."""

from typing import Literal, TypeAlias, cast

StreamingExperiencePreferredProtocolEnum: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamingExperiencePreferredProtocolEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamingExperiencePreferredProtocolEnum:
    return cast(StreamingExperiencePreferredProtocolEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StreamingExperiencePreferredProtocolEnum) -> str:
    return value


def deserialize_cbor(data: str) -> StreamingExperiencePreferredProtocolEnum:
    return cast(StreamingExperiencePreferredProtocolEnum, data)
