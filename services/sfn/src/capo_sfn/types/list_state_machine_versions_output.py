"""Generated from Smithy shape ``com.amazonaws.sfn#ListStateMachineVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.page_token
    import capo_sfn.types.state_machine_version_list


class ListStateMachineVersionsOutput(TypedDict, closed=True):
    state_machine_versions: (
        "capo_sfn.types.state_machine_version_list.StateMachineVersionList"
    )
    """<p>Versions for the state machine.</p>"""
    next_token: NotRequired["capo_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStateMachineVersionsOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.state_machine_version_list

    out["stateMachineVersions"] = (
        capo_sfn.types.state_machine_version_list.serialize_aws_json_1_0(
            value["state_machine_versions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStateMachineVersionsOutput:
    out: ListStateMachineVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineVersions") is not None:
        import capo_sfn.types.state_machine_version_list

        out["state_machine_versions"] = (
            capo_sfn.types.state_machine_version_list.deserialize_aws_json_1_0(
                data["stateMachineVersions"]
            )
        )
    else:
        out["state_machine_versions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
