"""Generated from Smithy shape ``com.amazonaws.appfabric#ListIngestionDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.ingestion_destination_list


class ListIngestionDestinationsResponse(TypedDict, closed=True):
    ingestion_destinations: (
        "capo_appfabric.types.ingestion_destination_list.IngestionDestinationList"
    )
    """<p>Contains a list of ingestion destination summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIngestionDestinationsResponse) -> dict:
    out: dict = {}
    import capo_appfabric.types.ingestion_destination_list

    out["ingestionDestinations"] = (
        capo_appfabric.types.ingestion_destination_list.serialize_json(
            value["ingestion_destinations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIngestionDestinationsResponse:
    out: ListIngestionDestinationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestionDestinations") is not None:
        import capo_appfabric.types.ingestion_destination_list

        out["ingestion_destinations"] = (
            capo_appfabric.types.ingestion_destination_list.deserialize_json(
                data["ingestionDestinations"]
            )
        )
    else:
        out["ingestion_destinations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
