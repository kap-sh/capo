"""Generated from Smithy shape ``com.amazonaws.datasync#ListAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.agent_list
    import capo_datasync.types.next_token


class ListAgentsResponse(TypedDict, closed=True):
    agents: NotRequired["capo_datasync.types.agent_list.AgentList"]
    """<p>A list of DataSync agents in your Amazon Web Services account in the Amazon Web Services Region specified in the request. The list is ordered by the agents' Amazon Resource Names (ARNs).</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>The opaque string that indicates the position to begin the next list of results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAgentsResponse) -> dict:
    out: dict = {}
    if "agents" in value:
        import capo_datasync.types.agent_list

        out["Agents"] = capo_datasync.types.agent_list.serialize_aws_json_1_1(
            value["agents"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAgentsResponse:
    out: ListAgentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Agents") is not None:
        import capo_datasync.types.agent_list

        out["agents"] = capo_datasync.types.agent_list.deserialize_aws_json_1_1(
            data["Agents"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAgentsResponse) -> dict:
    out: dict = {}
    if "agents" in value:
        import capo_datasync.types.agent_list

        out["Agents"] = capo_datasync.types.agent_list.serialize_cbor(value["agents"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAgentsResponse:
    out: ListAgentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Agents") is not None:
        import capo_datasync.types.agent_list

        out["agents"] = capo_datasync.types.agent_list.deserialize_cbor(data["Agents"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
