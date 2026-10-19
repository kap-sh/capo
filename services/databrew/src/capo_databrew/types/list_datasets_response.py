"""Generated from Smithy shape ``com.amazonaws.databrew#ListDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.dataset_list
    import capo_databrew.types.next_token


class ListDatasetsResponse(TypedDict, closed=True):
    datasets: "capo_databrew.types.dataset_list.DatasetList"
    """<p>A list of datasets that are defined.</p>"""
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    import capo_databrew.types.dataset_list

    out["Datasets"] = capo_databrew.types.dataset_list.serialize_json(value["datasets"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Datasets") is not None:
        import capo_databrew.types.dataset_list

        out["datasets"] = capo_databrew.types.dataset_list.deserialize_json(
            data["Datasets"]
        )
    else:
        out["datasets"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
