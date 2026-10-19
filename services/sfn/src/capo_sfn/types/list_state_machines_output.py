"""Generated from Smithy shape ``com.amazonaws.sfn#ListStateMachinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.page_token
    import capo_sfn.types.state_machine_list


class ListStateMachinesOutput(TypedDict, closed=True):
    state_machines: "capo_sfn.types.state_machine_list.StateMachineList"
    next_token: NotRequired["capo_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStateMachinesOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.state_machine_list

    out["stateMachines"] = capo_sfn.types.state_machine_list.serialize_aws_json_1_0(
        value["state_machines"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStateMachinesOutput:
    out: ListStateMachinesOutput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachines") is not None:
        import capo_sfn.types.state_machine_list

        out["state_machines"] = (
            capo_sfn.types.state_machine_list.deserialize_aws_json_1_0(
                data["stateMachines"]
            )
        )
    else:
        out["state_machines"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
