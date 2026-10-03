"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetPropertyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id


class DescribeAssetPropertyRequest(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetPropertyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAssetPropertyRequest:
    out: DescribeAssetPropertyRequest = {}  # type: ignore[typeddict-item]
    return out
