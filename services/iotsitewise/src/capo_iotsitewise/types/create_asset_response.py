"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.asset_status
    import capo_iotsitewise.types.id


class CreateAssetResponse(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format. This ID uniquely identifies the asset within IoT SiteWise and can be used with other IoT SiteWise API operations.</p>"""
    asset_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the asset, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}</code> </p>"""
    asset_status: "capo_iotsitewise.types.asset_status.AssetStatus"
    """<p>The status of the asset, which contains a state (<code>CREATING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetResponse) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["assetArn"] = value["asset_arn"]
    import capo_iotsitewise.types.asset_status

    out["assetStatus"] = capo_iotsitewise.types.asset_status.serialize_json(
        value["asset_status"]
    )
    return out


def deserialize_json(data: dict) -> CreateAssetResponse:
    out: CreateAssetResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("CreateAssetResponse.asset_id required")
    if data.get("assetArn") is not None:
        out["asset_arn"] = data["assetArn"]
    else:
        raise DeserializationError("CreateAssetResponse.asset_arn required")
    if data.get("assetStatus") is not None:
        import capo_iotsitewise.types.asset_status

        out["asset_status"] = capo_iotsitewise.types.asset_status.deserialize_json(
            data["assetStatus"]
        )
    else:
        raise DeserializationError("CreateAssetResponse.asset_status required")
    return out
