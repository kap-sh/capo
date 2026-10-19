"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAssetModelCompositeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_model_path
    import capo_iotsitewise.types.asset_model_status
    import capo_iotsitewise.types.id


class UpdateAssetModelCompositeModelResponse(TypedDict, closed=True):
    asset_model_composite_model_path: "capo_iotsitewise.types.asset_model_composite_model_path.AssetModelCompositeModelPath"
    """<p>The path to the composite model listing the parent composite models.</p>"""
    asset_model_status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"
    asset_model_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetModelCompositeModelResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_model_composite_model_path

    out["assetModelCompositeModelPath"] = (
        capo_iotsitewise.types.asset_model_composite_model_path.serialize_json(
            value["asset_model_composite_model_path"]
        )
    )
    import capo_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["asset_model_status"]
    )
    if "asset_model_id" in value:
        out["assetModelId"] = value["asset_model_id"]
    return out


def deserialize_json(data: dict) -> UpdateAssetModelCompositeModelResponse:
    out: UpdateAssetModelCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelCompositeModelPath") is not None:
        import capo_iotsitewise.types.asset_model_composite_model_path

        out["asset_model_composite_model_path"] = (
            capo_iotsitewise.types.asset_model_composite_model_path.deserialize_json(
                data["assetModelCompositeModelPath"]
            )
        )
    else:
        out["asset_model_composite_model_path"] = []
    if data.get("assetModelStatus") is not None:
        import capo_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            capo_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssetModelCompositeModelResponse.asset_model_status required"
        )
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    return out
