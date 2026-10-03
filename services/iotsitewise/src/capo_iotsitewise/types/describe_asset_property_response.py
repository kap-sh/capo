"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetPropertyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.composite_model_property
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.property


class DescribeAssetPropertyResponse(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format.</p>"""
    asset_external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the asset. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the asset.</p>"""
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_property: NotRequired["capo_iotsitewise.types.property.Property"]
    """<p>The asset property's definition, alias, and notification state.</p> <p>This response includes this object for normal asset properties. If you describe an asset property in a composite model, this response includes the asset property information in <code>compositeModel</code>.</p>"""
    composite_model: NotRequired[
        "capo_iotsitewise.types.composite_model_property.CompositeModelProperty"
    ]
    """<p>The composite model that declares this asset property, if this asset property exists in a composite model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetPropertyResponse) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    if "asset_external_id" in value:
        out["assetExternalId"] = value["asset_external_id"]
    out["assetName"] = value["asset_name"]
    out["assetModelId"] = value["asset_model_id"]
    if "asset_property" in value:
        import capo_iotsitewise.types.property

        out["assetProperty"] = capo_iotsitewise.types.property.serialize_json(
            value["asset_property"]
        )
    if "composite_model" in value:
        import capo_iotsitewise.types.composite_model_property

        out["compositeModel"] = (
            capo_iotsitewise.types.composite_model_property.serialize_json(
                value["composite_model"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetPropertyResponse:
    out: DescribeAssetPropertyResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("DescribeAssetPropertyResponse.asset_id required")
    if data.get("assetExternalId") is not None:
        out["asset_external_id"] = data["assetExternalId"]
    if data.get("assetName") is not None:
        out["asset_name"] = data["assetName"]
    else:
        raise DeserializationError("DescribeAssetPropertyResponse.asset_name required")
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetPropertyResponse.asset_model_id required"
        )
    if data.get("assetProperty") is not None:
        import capo_iotsitewise.types.property

        out["asset_property"] = capo_iotsitewise.types.property.deserialize_json(
            data["assetProperty"]
        )
    if data.get("compositeModel") is not None:
        import capo_iotsitewise.types.composite_model_property

        out["composite_model"] = (
            capo_iotsitewise.types.composite_model_property.deserialize_json(
                data["compositeModel"]
            )
        )
    return out
