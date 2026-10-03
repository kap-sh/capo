"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssociatedAssetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.traversal_direction


class ListAssociatedAssetsRequest(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset to query. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    hierarchy_id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>(Optional) If you don't provide a <code>hierarchyId</code>, all the immediate assets in the <code>traversalDirection</code> will be returned. </p> <p> The ID of the hierarchy by which child assets are associated to the asset. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.)</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    traversal_direction: NotRequired[
        "capo_iotsitewise.types.traversal_direction.TraversalDirection"
    ]
    """<p>The direction to list associated assets. Choose one of the following options:</p> <ul> <li> <p> <code>CHILD</code> – The list includes all child assets associated to the asset.</p> </li> <li> <p> <code>PARENT</code> – The list includes the asset's parent asset.</p> </li> </ul> <p>Default: <code>CHILD</code> </p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedAssetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociatedAssetsRequest:
    out: ListAssociatedAssetsRequest = {}  # type: ignore[typeddict-item]
    return out
