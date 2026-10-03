"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackagesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_summary_list
    import capo_codeartifact.types.pagination_token


class ListPackagesResult(TypedDict, closed=True):
    packages: NotRequired[
        "capo_codeartifact.types.package_summary_list.PackageSummaryList"
    ]
    """<p> The list of returned <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html">PackageSummary</a> objects. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> If there are additional results, this is the token for the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesResult) -> dict:
    out: dict = {}
    if "packages" in value:
        import capo_codeartifact.types.package_summary_list

        out["packages"] = capo_codeartifact.types.package_summary_list.serialize_json(
            value["packages"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackagesResult:
    out: ListPackagesResult = {}  # type: ignore[typeddict-item]
    if data.get("packages") is not None:
        import capo_codeartifact.types.package_summary_list

        out["packages"] = capo_codeartifact.types.package_summary_list.deserialize_json(
            data["packages"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
