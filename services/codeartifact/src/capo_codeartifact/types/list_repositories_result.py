"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListRepositoriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.pagination_token
    import capo_codeartifact.types.repository_summary_list


class ListRepositoriesResult(TypedDict, closed=True):
    repositories: NotRequired[
        "capo_codeartifact.types.repository_summary_list.RepositorySummaryList"
    ]
    """<p> The returned list of <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html">RepositorySummary</a> objects. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> If there are additional results, this is the token for the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRepositoriesResult) -> dict:
    out: dict = {}
    if "repositories" in value:
        import capo_codeartifact.types.repository_summary_list

        out["repositories"] = (
            capo_codeartifact.types.repository_summary_list.serialize_json(
                value["repositories"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRepositoriesResult:
    out: ListRepositoriesResult = {}  # type: ignore[typeddict-item]
    if data.get("repositories") is not None:
        import capo_codeartifact.types.repository_summary_list

        out["repositories"] = (
            capo_codeartifact.types.repository_summary_list.deserialize_json(
                data["repositories"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
