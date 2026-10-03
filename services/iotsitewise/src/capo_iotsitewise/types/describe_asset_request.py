"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.exclude_properties


class DescribeAssetRequest(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    exclude_properties: "capo_iotsitewise.types.exclude_properties.ExcludeProperties"
    """<p> Whether or not to exclude asset properties from the response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAssetRequest:
    out: DescribeAssetRequest = {}  # type: ignore[typeddict-item]
    return out
