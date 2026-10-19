"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_summary_list


class ListTestsResponse(TypedDict, closed=True):
    tests: "capo_resiliencehubv2.types.test_summary_list.TestSummaryList"
    """<p>The list of test summaries.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_summary_list

    out["tests"] = capo_resiliencehubv2.types.test_summary_list.serialize_json(
        value["tests"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestsResponse:
    out: ListTestsResponse = {}  # type: ignore[typeddict-item]
    if data.get("tests") is not None:
        import capo_resiliencehubv2.types.test_summary_list

        out["tests"] = capo_resiliencehubv2.types.test_summary_list.deserialize_json(
            data["tests"]
        )
    else:
        out["tests"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
