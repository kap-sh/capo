"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetAssetPropertyValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.id


class GetAssetPropertyValueRequest(TypedDict, closed=True):
    asset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset, in UUID format.</p>"""
    property_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property, in UUID format.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetPropertyValueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetPropertyValueRequest:
    out: GetAssetPropertyValueRequest = {}  # type: ignore[typeddict-item]
    return out
