"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.list_asset_properties_filter
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListAssetPropertiesRequest(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request. If not specified, the default value is 50.</p>"""
    filter: NotRequired[
        "capo_iotsitewise.types.list_asset_properties_filter.ListAssetPropertiesFilter"
    ]
    """<p> Filters the requested list of asset properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetPropertiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetPropertiesRequest:
    out: ListAssetPropertiesRequest = {}  # type: ignore[typeddict-item]
    return out
