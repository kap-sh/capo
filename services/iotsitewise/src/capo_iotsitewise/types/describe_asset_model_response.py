"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.asset_model_composite_model_summaries
    import capo_iotsitewise.types.asset_model_composite_models
    import capo_iotsitewise.types.asset_model_hierarchies
    import capo_iotsitewise.types.asset_model_properties
    import capo_iotsitewise.types.asset_model_status
    import capo_iotsitewise.types.asset_model_type
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.e_tag
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.interface_details
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class DescribeAssetModelResponse(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_model_external_id: NotRequired[
        "capo_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>The external ID of the asset model, if any.</p>"""
    asset_model_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the asset model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}</code> </p>"""
    asset_model_name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the asset model.</p>"""
    asset_model_type: NotRequired[
        "capo_iotsitewise.types.asset_model_type.AssetModelType"
    ]
    """<p>The type of asset model.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> </ul>"""
    asset_model_description: "capo_iotsitewise.types.description.Description"
    """<p>The asset model's description.</p>"""
    asset_model_properties: (
        "capo_iotsitewise.types.asset_model_properties.AssetModelProperties"
    )
    """<p>The list of asset properties for the asset model.</p> <p>This object doesn't include properties that you define in composite models. You can find composite model properties in the <code>assetModelCompositeModels</code> object.</p>"""
    asset_model_hierarchies: (
        "capo_iotsitewise.types.asset_model_hierarchies.AssetModelHierarchies"
    )
    """<p>A list of asset model hierarchies that each contain a <code>childAssetModelId</code> and a <code>hierarchyId</code> (named <code>id</code>). A hierarchy specifies allowed parent/child asset relationships for an asset model.</p>"""
    asset_model_composite_models: NotRequired[
        "capo_iotsitewise.types.asset_model_composite_models.AssetModelCompositeModels"
    ]
    """<p>The list of built-in composite models for the asset model, such as those with those of type <code>AWS/ALARMS</code>.</p>"""
    asset_model_composite_model_summaries: NotRequired[
        "capo_iotsitewise.types.asset_model_composite_model_summaries.AssetModelCompositeModelSummaries"
    ]
    """<p>The list of the immediate child custom composite model summaries for the asset model.</p>"""
    asset_model_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset model was created, in Unix epoch time.</p>"""
    asset_model_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset model was last updated, in Unix epoch time.</p>"""
    asset_model_status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"
    """<p>The current status of the asset model, which contains a state and any error message.</p>"""
    asset_model_version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>The version of the asset model. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    interface_details: NotRequired[
        "capo_iotsitewise.types.interface_details.InterfaceDetails"
    ]
    """<p>A list of interface details that describe the interfaces implemented by this asset model, including interface asset model IDs and property mappings.</p>"""
    e_tag: NotRequired["capo_iotsitewise.types.e_tag.ETag"]
    """<p>The entity tag (ETag) is a hash of the retrieved version of the asset model. It's used to make concurrent updates safely to the resource. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>. </p> <p>See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html"> Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetModelResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    if "asset_model_external_id" in value:
        out["assetModelExternalId"] = value["asset_model_external_id"]
    out["assetModelArn"] = value["asset_model_arn"]
    out["assetModelName"] = value["asset_model_name"]
    if "asset_model_type" in value:
        import capo_iotsitewise.types.asset_model_type

        out["assetModelType"] = capo_iotsitewise.types.asset_model_type.serialize_json(
            value["asset_model_type"]
        )
    out["assetModelDescription"] = value["asset_model_description"]
    import capo_iotsitewise.types.asset_model_properties

    out["assetModelProperties"] = (
        capo_iotsitewise.types.asset_model_properties.serialize_json(
            value["asset_model_properties"]
        )
    )
    import capo_iotsitewise.types.asset_model_hierarchies

    out["assetModelHierarchies"] = (
        capo_iotsitewise.types.asset_model_hierarchies.serialize_json(
            value["asset_model_hierarchies"]
        )
    )
    if "asset_model_composite_models" in value:
        import capo_iotsitewise.types.asset_model_composite_models

        out["assetModelCompositeModels"] = (
            capo_iotsitewise.types.asset_model_composite_models.serialize_json(
                value["asset_model_composite_models"]
            )
        )
    if "asset_model_composite_model_summaries" in value:
        import capo_iotsitewise.types.asset_model_composite_model_summaries

        out["assetModelCompositeModelSummaries"] = (
            capo_iotsitewise.types.asset_model_composite_model_summaries.serialize_json(
                value["asset_model_composite_model_summaries"]
            )
        )
    import capo_iotsitewise.types.timestamp

    out["assetModelCreationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["asset_model_creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["assetModelLastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["asset_model_last_update_date"]
    )
    import capo_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["asset_model_status"]
    )
    if "asset_model_version" in value:
        out["assetModelVersion"] = value["asset_model_version"]
    if "interface_details" in value:
        import capo_iotsitewise.types.interface_details

        out["interfaceDetails"] = (
            capo_iotsitewise.types.interface_details.serialize_json(
                value["interface_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetModelResponse:
    out: DescribeAssetModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("DescribeAssetModelResponse.asset_model_id required")
    if data.get("assetModelExternalId") is not None:
        out["asset_model_external_id"] = data["assetModelExternalId"]
    if data.get("assetModelArn") is not None:
        out["asset_model_arn"] = data["assetModelArn"]
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_arn required"
        )
    if data.get("assetModelName") is not None:
        out["asset_model_name"] = data["assetModelName"]
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_name required"
        )
    if data.get("assetModelType") is not None:
        import capo_iotsitewise.types.asset_model_type

        out["asset_model_type"] = (
            capo_iotsitewise.types.asset_model_type.deserialize_json(
                data["assetModelType"]
            )
        )
    if data.get("assetModelDescription") is not None:
        out["asset_model_description"] = data["assetModelDescription"]
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_description required"
        )
    if data.get("assetModelProperties") is not None:
        import capo_iotsitewise.types.asset_model_properties

        out["asset_model_properties"] = (
            capo_iotsitewise.types.asset_model_properties.deserialize_json(
                data["assetModelProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_properties required"
        )
    if data.get("assetModelHierarchies") is not None:
        import capo_iotsitewise.types.asset_model_hierarchies

        out["asset_model_hierarchies"] = (
            capo_iotsitewise.types.asset_model_hierarchies.deserialize_json(
                data["assetModelHierarchies"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_hierarchies required"
        )
    if data.get("assetModelCompositeModels") is not None:
        import capo_iotsitewise.types.asset_model_composite_models

        out["asset_model_composite_models"] = (
            capo_iotsitewise.types.asset_model_composite_models.deserialize_json(
                data["assetModelCompositeModels"]
            )
        )
    if data.get("assetModelCompositeModelSummaries") is not None:
        import capo_iotsitewise.types.asset_model_composite_model_summaries

        out["asset_model_composite_model_summaries"] = (
            capo_iotsitewise.types.asset_model_composite_model_summaries.deserialize_json(
                data["assetModelCompositeModelSummaries"]
            )
        )
    if data.get("assetModelCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["asset_model_creation_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["assetModelCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_creation_date required"
        )
    if data.get("assetModelLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["asset_model_last_update_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["assetModelLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_last_update_date required"
        )
    if data.get("assetModelStatus") is not None:
        import capo_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            capo_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_status required"
        )
    if data.get("assetModelVersion") is not None:
        out["asset_model_version"] = data["assetModelVersion"]
    if data.get("interfaceDetails") is not None:
        import capo_iotsitewise.types.interface_details

        out["interface_details"] = (
            capo_iotsitewise.types.interface_details.deserialize_json(
                data["interfaceDetails"]
            )
        )
    return out
