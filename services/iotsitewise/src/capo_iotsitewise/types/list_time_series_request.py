"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListTimeSeriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.list_time_series_type
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.property_alias
    import capo_iotsitewise.types.workspace_name


class ListTimeSeriesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p>"""
    asset_id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    alias_prefix: NotRequired["capo_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias prefix of the time series.</p>"""
    time_series_type: NotRequired[
        "capo_iotsitewise.types.list_time_series_type.ListTimeSeriesType"
    ]
    """<p>The type of the time series. The time series type can be one of the following values:</p> <ul> <li> <p> <code>ASSOCIATED</code> – The time series is associated with an asset property.</p> </li> <li> <p> <code>DISASSOCIATED</code> – The time series isn't associated with any asset property.</p> </li> </ul>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTimeSeriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTimeSeriesRequest:
    out: ListTimeSeriesRequest = {}  # type: ignore[typeddict-item]
    return out
