"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestRunSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_run_source_summary_list


class ListTestRunSourcesResponse(TypedDict, closed=True):
    test_run_sources: "capo_resiliencehubv2.types.test_run_source_summary_list.TestRunSourceSummaryList"
    """<p>The list of monitoring source snapshots.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRunSourcesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_run_source_summary_list

    out["testRunSources"] = (
        capo_resiliencehubv2.types.test_run_source_summary_list.serialize_json(
            value["test_run_sources"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestRunSourcesResponse:
    out: ListTestRunSourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("testRunSources") is not None:
        import capo_resiliencehubv2.types.test_run_source_summary_list

        out["test_run_sources"] = (
            capo_resiliencehubv2.types.test_run_source_summary_list.deserialize_json(
                data["testRunSources"]
            )
        )
    else:
        out["test_run_sources"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
