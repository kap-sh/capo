"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListChatsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.chat_execution_list


class ListChatsResponse(TypedDict, closed=True):
    executions: "capo_devops_agent.types.chat_execution_list.ChatExecutionList"
    """<p>List of recent chat executions</p>"""
    next_token: NotRequired["str"]
    """<p>Token for retrieving the next page of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChatsResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.chat_execution_list

    out["executions"] = capo_devops_agent.types.chat_execution_list.serialize_json(
        value["executions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChatsResponse:
    out: ListChatsResponse = {}  # type: ignore[typeddict-item]
    if data.get("executions") is not None:
        import capo_devops_agent.types.chat_execution_list

        out["executions"] = (
            capo_devops_agent.types.chat_execution_list.deserialize_json(
                data["executions"]
            )
        )
    else:
        out["executions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
