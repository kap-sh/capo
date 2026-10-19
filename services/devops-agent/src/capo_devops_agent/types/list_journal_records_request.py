"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListJournalRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.order_type
    import capo_devops_agent.types.resource_id


class ListJournalRecordsRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space containing the execution</p>"""
    execution_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the execution whose journal records to retrieve</p>"""
    limit: NotRequired["int"]
    """<p>Maximum number of records to return in a single response (1-100, default: 100)</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results</p>"""
    record_type: NotRequired["str"]
    """<p>Filter records by type (empty string returns all types)</p>"""
    order: NotRequired["capo_devops_agent.types.order_type.OrderType"]
    """<p>Sort order for the records based on timestamp (default: DESC)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJournalRecordsRequest) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "record_type" in value:
        out["recordType"] = value["record_type"]
    if "order" in value:
        import capo_devops_agent.types.order_type

        out["order"] = capo_devops_agent.types.order_type.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> ListJournalRecordsRequest:
    out: ListJournalRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recordType") is not None:
        out["record_type"] = data["recordType"]
    if data.get("order") is not None:
        import capo_devops_agent.types.order_type

        out["order"] = capo_devops_agent.types.order_type.deserialize_json(
            data["order"]
        )
    return out
