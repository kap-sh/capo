"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetRelationshipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.traversal_type


class ListAssetRelationshipsRequest(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    traversal_type: "capo_iotsitewise.types.traversal_type.TraversalType"
    """<p>The type of traversal to use to identify asset relationships. Choose the following option:</p> <ul> <li> <p> <code>PATH_TO_ROOT</code> – Identify the asset's parent assets up to the root asset. The asset that you specify in <code>assetId</code> is the first result in the list of <code>assetRelationshipSummaries</code>, and the root asset is the last result.</p> </li> </ul>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetRelationshipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetRelationshipsRequest:
    out: ListAssetRelationshipsRequest = {}  # type: ignore[typeddict-item]
    return out
