"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListDependenciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.dependency_summary_list
    import capo_resiliencehubv2.types.next_token


class ListDependenciesResponse(TypedDict, closed=True):
    dependency_summaries: (
        "capo_resiliencehubv2.types.dependency_summary_list.DependencySummaryList"
    )
    """<p>The list of dependency summaries.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDependenciesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.dependency_summary_list

    out["dependencySummaries"] = (
        capo_resiliencehubv2.types.dependency_summary_list.serialize_json(
            value["dependency_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDependenciesResponse:
    out: ListDependenciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("dependencySummaries") is not None:
        import capo_resiliencehubv2.types.dependency_summary_list

        out["dependency_summaries"] = (
            capo_resiliencehubv2.types.dependency_summary_list.deserialize_json(
                data["dependencySummaries"]
            )
        )
    else:
        out["dependency_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
