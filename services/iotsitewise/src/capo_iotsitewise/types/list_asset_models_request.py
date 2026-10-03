"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_version_filter
    import capo_iotsitewise.types.list_asset_models_type_filter
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListAssetModelsRequest(TypedDict, closed=True):
    asset_model_types: NotRequired[
        "capo_iotsitewise.types.list_asset_models_type_filter.ListAssetModelsTypeFilter"
    ]
    """<p>The type of asset model. If you don't provide an <code>assetModelTypes</code>, all types of asset models are returned.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> <li> <p> <b>INTERFACE</b> – An interface is a type of model that defines a standard structure that can be applied to different asset models.</p> </li> </ul>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>"""
    asset_model_version: NotRequired[
        "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
    ]
    """<p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetModelsRequest:
    out: ListAssetModelsRequest = {}  # type: ignore[typeddict-item]
    return out
