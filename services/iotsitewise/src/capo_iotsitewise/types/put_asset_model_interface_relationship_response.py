"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutAssetModelInterfaceRelationshipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.asset_model_status
    import capo_iotsitewise.types.id


class PutAssetModelInterfaceRelationshipResponse(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model.</p>"""
    interface_asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the interface asset model.</p>"""
    asset_model_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the asset model, which has the following format. <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}</code> </p>"""
    asset_model_status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"


# --- restJson1 ser/de ---
def serialize_json(value: PutAssetModelInterfaceRelationshipResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["interfaceAssetModelId"] = value["interface_asset_model_id"]
    out["assetModelArn"] = value["asset_model_arn"]
    import capo_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["asset_model_status"]
    )
    return out


def deserialize_json(data: dict) -> PutAssetModelInterfaceRelationshipResponse:
    out: PutAssetModelInterfaceRelationshipResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        out["asset_model_id"] = ""
    if data.get("interfaceAssetModelId") is not None:
        out["interface_asset_model_id"] = data["interfaceAssetModelId"]
    else:
        out["interface_asset_model_id"] = ""
    if data.get("assetModelArn") is not None:
        out["asset_model_arn"] = data["assetModelArn"]
    else:
        out["asset_model_arn"] = ""
    if data.get("assetModelStatus") is not None:
        import capo_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            capo_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "PutAssetModelInterfaceRelationshipResponse.asset_model_status required"
        )
    return out
