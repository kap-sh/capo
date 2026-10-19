"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListIngestConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_list
    import capo_ivs_realtime.types.pagination_token


class ListIngestConfigurationsResponse(TypedDict, closed=True):
    ingest_configurations: (
        "capo_ivs_realtime.types.ingest_configuration_list.IngestConfigurationList"
    )
    """<p>List of the matching ingest configurations (summary information only).</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>If there are more IngestConfigurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIngestConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_ivs_realtime.types.ingest_configuration_list

    out["ingestConfigurations"] = (
        capo_ivs_realtime.types.ingest_configuration_list.serialize_json(
            value["ingest_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIngestConfigurationsResponse:
    out: ListIngestConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestConfigurations") is not None:
        import capo_ivs_realtime.types.ingest_configuration_list

        out["ingest_configurations"] = (
            capo_ivs_realtime.types.ingest_configuration_list.deserialize_json(
                data["ingestConfigurations"]
            )
        )
    else:
        out["ingest_configurations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
