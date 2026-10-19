"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListTriggersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.trigger_list


class ListTriggersResponse(TypedDict, closed=True):
    items: "capo_devops_agent.types.trigger_list.TriggerList"
    """<p>The list of Triggers</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token to retrieve the next page of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTriggersResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.trigger_list

    out["items"] = capo_devops_agent.types.trigger_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTriggersResponse:
    out: ListTriggersResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_devops_agent.types.trigger_list

        out["items"] = capo_devops_agent.types.trigger_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
