"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_source_summary_list


class ListTestSourcesResponse(TypedDict, closed=True):
    test_sources: (
        "capo_resiliencehubv2.types.test_source_summary_list.TestSourceSummaryList"
    )
    """<p>The list of configured monitoring sources.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestSourcesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_source_summary_list

    out["testSources"] = (
        capo_resiliencehubv2.types.test_source_summary_list.serialize_json(
            value["test_sources"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestSourcesResponse:
    out: ListTestSourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("testSources") is not None:
        import capo_resiliencehubv2.types.test_source_summary_list

        out["test_sources"] = (
            capo_resiliencehubv2.types.test_source_summary_list.deserialize_json(
                data["testSources"]
            )
        )
    else:
        out["test_sources"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
