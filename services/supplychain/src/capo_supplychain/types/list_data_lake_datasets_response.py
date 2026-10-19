"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataLakeDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_list
    import capo_supplychain.types.data_lake_dataset_next_token


class ListDataLakeDatasetsResponse(TypedDict, closed=True):
    datasets: "capo_supplychain.types.data_lake_dataset_list.DataLakeDatasetList"
    """<p>The list of fetched dataset details.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_lake_dataset_next_token.DataLakeDatasetNextToken"
    ]
    """<p>The pagination token to fetch next page of datasets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakeDatasetsResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_lake_dataset_list

    out["datasets"] = capo_supplychain.types.data_lake_dataset_list.serialize_json(
        value["datasets"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataLakeDatasetsResponse:
    out: ListDataLakeDatasetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasets") is not None:
        import capo_supplychain.types.data_lake_dataset_list

        out["datasets"] = (
            capo_supplychain.types.data_lake_dataset_list.deserialize_json(
                data["datasets"]
            )
        )
    else:
        out["datasets"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
