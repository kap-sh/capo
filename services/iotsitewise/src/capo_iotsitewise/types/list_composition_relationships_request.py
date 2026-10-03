"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListCompositionRelationshipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListCompositionRelationshipsRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCompositionRelationshipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCompositionRelationshipsRequest:
    out: ListCompositionRelationshipsRequest = {}  # type: ignore[typeddict-item]
    return out
