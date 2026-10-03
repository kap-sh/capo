"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.asset_composite_model_summaries
    import capo_iotsitewise.types.asset_composite_models
    import capo_iotsitewise.types.asset_hierarchies
    import capo_iotsitewise.types.asset_properties
    import capo_iotsitewise.types.asset_status
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.timestamp


class DescribeAssetResponse(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format.</p>"""
    asset_external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the asset, if any.</p>"""
    asset_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the asset, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}</code> </p>"""
    asset_name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the asset.</p>"""
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model that was used to create the asset.</p>"""
    asset_properties: "capo_iotsitewise.types.asset_properties.AssetProperties"
    """<p>The list of asset properties for the asset.</p> <p>This object doesn't include properties that you define in composite models. You can find composite model properties in the <code>assetCompositeModels</code> object.</p>"""
    asset_hierarchies: "capo_iotsitewise.types.asset_hierarchies.AssetHierarchies"
    """<p>A list of asset hierarchies that each contain a <code>hierarchyId</code>. A hierarchy specifies allowed parent/child asset relationships.</p>"""
    asset_composite_models: NotRequired[
        "capo_iotsitewise.types.asset_composite_models.AssetCompositeModels"
    ]
    """<p>The composite models for the asset.</p>"""
    asset_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset was created, in Unix epoch time.</p>"""
    asset_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset was last updated, in Unix epoch time.</p>"""
    asset_status: "capo_iotsitewise.types.asset_status.AssetStatus"
    """<p>The current status of the asset, which contains a state and any error message.</p>"""
    asset_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A description for the asset.</p>"""
    asset_composite_model_summaries: NotRequired[
        "capo_iotsitewise.types.asset_composite_model_summaries.AssetCompositeModelSummaries"
    ]
    """<p>The list of the immediate child custom composite model summaries for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetResponse) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    if "asset_external_id" in value:
        out["assetExternalId"] = value["asset_external_id"]
    out["assetArn"] = value["asset_arn"]
    out["assetName"] = value["asset_name"]
    out["assetModelId"] = value["asset_model_id"]
    import capo_iotsitewise.types.asset_properties

    out["assetProperties"] = capo_iotsitewise.types.asset_properties.serialize_json(
        value["asset_properties"]
    )
    import capo_iotsitewise.types.asset_hierarchies

    out["assetHierarchies"] = capo_iotsitewise.types.asset_hierarchies.serialize_json(
        value["asset_hierarchies"]
    )
    if "asset_composite_models" in value:
        import capo_iotsitewise.types.asset_composite_models

        out["assetCompositeModels"] = (
            capo_iotsitewise.types.asset_composite_models.serialize_json(
                value["asset_composite_models"]
            )
        )
    import capo_iotsitewise.types.timestamp

    out["assetCreationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["asset_creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["assetLastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["asset_last_update_date"]
    )
    import capo_iotsitewise.types.asset_status

    out["assetStatus"] = capo_iotsitewise.types.asset_status.serialize_json(
        value["asset_status"]
    )
    if "asset_description" in value:
        out["assetDescription"] = value["asset_description"]
    if "asset_composite_model_summaries" in value:
        import capo_iotsitewise.types.asset_composite_model_summaries

        out["assetCompositeModelSummaries"] = (
            capo_iotsitewise.types.asset_composite_model_summaries.serialize_json(
                value["asset_composite_model_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetResponse:
    out: DescribeAssetResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("DescribeAssetResponse.asset_id required")
    if data.get("assetExternalId") is not None:
        out["asset_external_id"] = data["assetExternalId"]
    if data.get("assetArn") is not None:
        out["asset_arn"] = data["assetArn"]
    else:
        raise DeserializationError("DescribeAssetResponse.asset_arn required")
    if data.get("assetName") is not None:
        out["asset_name"] = data["assetName"]
    else:
        raise DeserializationError("DescribeAssetResponse.asset_name required")
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("DescribeAssetResponse.asset_model_id required")
    if data.get("assetProperties") is not None:
        import capo_iotsitewise.types.asset_properties

        out["asset_properties"] = (
            capo_iotsitewise.types.asset_properties.deserialize_json(
                data["assetProperties"]
            )
        )
    else:
        raise DeserializationError("DescribeAssetResponse.asset_properties required")
    if data.get("assetHierarchies") is not None:
        import capo_iotsitewise.types.asset_hierarchies

        out["asset_hierarchies"] = (
            capo_iotsitewise.types.asset_hierarchies.deserialize_json(
                data["assetHierarchies"]
            )
        )
    else:
        raise DeserializationError("DescribeAssetResponse.asset_hierarchies required")
    if data.get("assetCompositeModels") is not None:
        import capo_iotsitewise.types.asset_composite_models

        out["asset_composite_models"] = (
            capo_iotsitewise.types.asset_composite_models.deserialize_json(
                data["assetCompositeModels"]
            )
        )
    if data.get("assetCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["asset_creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["assetCreationDate"]
        )
    else:
        raise DeserializationError("DescribeAssetResponse.asset_creation_date required")
    if data.get("assetLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["asset_last_update_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["assetLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetResponse.asset_last_update_date required"
        )
    if data.get("assetStatus") is not None:
        import capo_iotsitewise.types.asset_status

        out["asset_status"] = capo_iotsitewise.types.asset_status.deserialize_json(
            data["assetStatus"]
        )
    else:
        raise DeserializationError("DescribeAssetResponse.asset_status required")
    if data.get("assetDescription") is not None:
        out["asset_description"] = data["assetDescription"]
    if data.get("assetCompositeModelSummaries") is not None:
        import capo_iotsitewise.types.asset_composite_model_summaries

        out["asset_composite_model_summaries"] = (
            capo_iotsitewise.types.asset_composite_model_summaries.deserialize_json(
                data["assetCompositeModelSummaries"]
            )
        )
    return out
