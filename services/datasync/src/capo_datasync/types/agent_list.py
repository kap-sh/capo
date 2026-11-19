"""Generated from Smithy shape ``com.amazonaws.datasync#AgentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.agent_list_entry

AgentList: TypeAlias = list["capo_datasync.types.agent_list_entry.AgentListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentList) -> list:
    import capo_datasync.types.agent_list_entry

    out: list = []
    for item in value:
        out.append(capo_datasync.types.agent_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AgentList:
    import capo_datasync.types.agent_list_entry

    out: AgentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.agent_list_entry.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgentList) -> list:
    import capo_datasync.types.agent_list_entry

    out: list = []
    for item in value:
        out.append(capo_datasync.types.agent_list_entry.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AgentList:
    import capo_datasync.types.agent_list_entry

    out: AgentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.agent_list_entry.deserialize_cbor(item))
    return out
