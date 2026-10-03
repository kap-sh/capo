"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetCompositeModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id


class DescribeAssetCompositeModelRequest(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_composite_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of a composite model on this asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetCompositeModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAssetCompositeModelRequest:
    out: DescribeAssetCompositeModelRequest = {}  # type: ignore[typeddict-item]
    return out
