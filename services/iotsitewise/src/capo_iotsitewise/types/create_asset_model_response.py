"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAssetModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.asset_model_status
    import capo_iotsitewise.types.id


class CreateAssetModelResponse(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format. You can use this ID when you call other IoT SiteWise API operations.</p>"""
    asset_model_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the asset model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}</code> </p>"""
    asset_model_status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"
    """<p>The status of the asset model, which contains a state (<code>CREATING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetModelResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["assetModelArn"] = value["asset_model_arn"]
    import capo_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["asset_model_status"]
    )
    return out


def deserialize_json(data: dict) -> CreateAssetModelResponse:
    out: CreateAssetModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("CreateAssetModelResponse.asset_model_id required")
    if data.get("assetModelArn") is not None:
        out["asset_model_arn"] = data["assetModelArn"]
    else:
        raise DeserializationError("CreateAssetModelResponse.asset_model_arn required")
    if data.get("assetModelStatus") is not None:
        import capo_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            capo_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAssetModelResponse.asset_model_status required"
        )
    return out
