"""Generated from Smithy shape ``com.amazonaws.datasync#AgentArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn

AgentArnList: TypeAlias = list["capo_datasync.types.agent_arn.AgentArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AgentArnList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgentArnList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AgentArnList:
    return [item for item in data if item is not None]
