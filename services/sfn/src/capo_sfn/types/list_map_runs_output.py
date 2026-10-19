"""Generated from Smithy shape ``com.amazonaws.sfn#ListMapRunsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.map_run_list
    import capo_sfn.types.page_token


class ListMapRunsOutput(TypedDict, closed=True):
    map_runs: "capo_sfn.types.map_run_list.MapRunList"
    """<p>An array that lists information related to a Map Run, such as the Amazon Resource Name (ARN) of the Map Run and the ARN of the state machine that started the Map Run.</p>"""
    next_token: NotRequired["capo_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMapRunsOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.map_run_list

    out["mapRuns"] = capo_sfn.types.map_run_list.serialize_aws_json_1_0(
        value["map_runs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMapRunsOutput:
    out: ListMapRunsOutput = {}  # type: ignore[typeddict-item]
    if data.get("mapRuns") is not None:
        import capo_sfn.types.map_run_list

        out["map_runs"] = capo_sfn.types.map_run_list.deserialize_aws_json_1_0(
            data["mapRuns"]
        )
    else:
        out["map_runs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
