"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListStorageConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.pagination_token
    import capo_ivs_realtime.types.storage_configuration_summary_list


class ListStorageConfigurationsResponse(TypedDict, closed=True):
    storage_configurations: "capo_ivs_realtime.types.storage_configuration_summary_list.StorageConfigurationSummaryList"
    """<p>List of the matching storage configurations.</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>If there are more storage configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStorageConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_ivs_realtime.types.storage_configuration_summary_list

    out["storageConfigurations"] = (
        capo_ivs_realtime.types.storage_configuration_summary_list.serialize_json(
            value["storage_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStorageConfigurationsResponse:
    out: ListStorageConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("storageConfigurations") is not None:
        import capo_ivs_realtime.types.storage_configuration_summary_list

        out["storage_configurations"] = (
            capo_ivs_realtime.types.storage_configuration_summary_list.deserialize_json(
                data["storageConfigurations"]
            )
        )
    else:
        out["storage_configurations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
