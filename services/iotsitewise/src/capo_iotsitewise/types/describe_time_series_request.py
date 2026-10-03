"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeTimeSeriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.property_alias
    import capo_iotsitewise.types.workspace_name


class DescribeTimeSeriesRequest(TypedDict, closed=True):
    alias: NotRequired["capo_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias that identifies the time series.</p>"""
    asset_id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTimeSeriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTimeSeriesRequest:
    out: DescribeTimeSeriesRequest = {}  # type: ignore[typeddict-item]
    return out
