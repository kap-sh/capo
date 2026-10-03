"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_version_filter
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.exclude_properties


class DescribeAssetModelRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    exclude_properties: "capo_iotsitewise.types.exclude_properties.ExcludeProperties"
    """<p> Whether or not to exclude asset model properties from the response. </p>"""
    asset_model_version: NotRequired[
        "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
    ]
    """<p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAssetModelRequest:
    out: DescribeAssetModelRequest = {}  # type: ignore[typeddict-item]
    return out
