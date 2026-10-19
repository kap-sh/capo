"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_run_summary_list


class ListTestRunsResponse(TypedDict, closed=True):
    test_runs: "capo_resiliencehubv2.types.test_run_summary_list.TestRunSummaryList"
    """<p>The list of test run summaries.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRunsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_run_summary_list

    out["testRuns"] = capo_resiliencehubv2.types.test_run_summary_list.serialize_json(
        value["test_runs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestRunsResponse:
    out: ListTestRunsResponse = {}  # type: ignore[typeddict-item]
    if data.get("testRuns") is not None:
        import capo_resiliencehubv2.types.test_run_summary_list

        out["test_runs"] = (
            capo_resiliencehubv2.types.test_run_summary_list.deserialize_json(
                data["testRuns"]
            )
        )
    else:
        out["test_runs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
