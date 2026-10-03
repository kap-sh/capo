"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_version_filter
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.list_asset_model_properties_filter
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListAssetModelPropertiesRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request. If not specified, the default value is 50.</p>"""
    filter: NotRequired[
        "capo_iotsitewise.types.list_asset_model_properties_filter.ListAssetModelPropertiesFilter"
    ]
    """<p> Filters the requested list of asset model properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset model properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset model properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>"""
    asset_model_version: NotRequired[
        "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
    ]
    """<p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetModelPropertiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetModelPropertiesRequest:
    out: ListAssetModelPropertiesRequest = {}  # type: ignore[typeddict-item]
    return out
