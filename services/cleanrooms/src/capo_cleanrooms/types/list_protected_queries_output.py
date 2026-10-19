"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListProtectedQueriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.protected_query_summary_list


class ListProtectedQueriesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    protected_queries: (
        "capo_cleanrooms.types.protected_query_summary_list.ProtectedQuerySummaryList"
    )
    """<p>A list of protected queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProtectedQueriesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.protected_query_summary_list

    out["protectedQueries"] = (
        capo_cleanrooms.types.protected_query_summary_list.serialize_json(
            value["protected_queries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListProtectedQueriesOutput:
    out: ListProtectedQueriesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("protectedQueries") is not None:
        import capo_cleanrooms.types.protected_query_summary_list

        out["protected_queries"] = (
            capo_cleanrooms.types.protected_query_summary_list.deserialize_json(
                data["protectedQueries"]
            )
        )
    else:
        out["protected_queries"] = []
    return out
