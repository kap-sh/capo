"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListDatasetsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.dataset_list
    import capo_finspace_data.types.pagination_token


class ListDatasetsResponse(TypedDict, closed=True):
    datasets: NotRequired["capo_finspace_data.types.dataset_list.DatasetList"]
    """<p>List of Datasets.</p>"""
    next_token: NotRequired["capo_finspace_data.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "datasets" in value:
        import capo_finspace_data.types.dataset_list

        out["datasets"] = capo_finspace_data.types.dataset_list.serialize_json(
            value["datasets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasets") is not None:
        import capo_finspace_data.types.dataset_list

        out["datasets"] = capo_finspace_data.types.dataset_list.deserialize_json(
            data["datasets"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListDatasetsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "datasets" in value:
        import capo_finspace_data.types.dataset_list

        out["datasets"] = capo_finspace_data.types.dataset_list.redact_sensitive(
            value["datasets"]
        )
    return out
