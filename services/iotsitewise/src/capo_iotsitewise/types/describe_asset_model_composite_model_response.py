"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetModelCompositeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.action_definitions
    import capo_iotsitewise.types.asset_model_composite_model_path
    import capo_iotsitewise.types.asset_model_composite_model_summaries
    import capo_iotsitewise.types.asset_model_properties
    import capo_iotsitewise.types.composition_details
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class DescribeAssetModelCompositeModelResponse(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_model_composite_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of a composite model on this asset model.</p>"""
    asset_model_composite_model_external_id: NotRequired[
        "capo_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>The external ID of a composite model on this asset model.</p>"""
    asset_model_composite_model_path: "capo_iotsitewise.types.asset_model_composite_model_path.AssetModelCompositeModelPath"
    """<p>The path to the composite model listing the parent composite models.</p>"""
    asset_model_composite_model_name: "capo_iotsitewise.types.name.Name"
    """<p>The unique, friendly name for the composite model.</p>"""
    asset_model_composite_model_description: (
        "capo_iotsitewise.types.description.Description"
    )
    """<p>The description for the composite model.</p>"""
    asset_model_composite_model_type: "capo_iotsitewise.types.name.Name"
    """<p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>"""
    asset_model_composite_model_properties: (
        "capo_iotsitewise.types.asset_model_properties.AssetModelProperties"
    )
    """<p>The property definitions of the composite model.</p>"""
    composition_details: NotRequired[
        "capo_iotsitewise.types.composition_details.CompositionDetails"
    ]
    """<p>Metadata for the composition relationship established by using <code>composedAssetModelId</code> in <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html"> <code>CreateAssetModelCompositeModel</code> </a>. For instance, an array detailing the path of the composition relationship for this composite model.</p>"""
    asset_model_composite_model_summaries: "capo_iotsitewise.types.asset_model_composite_model_summaries.AssetModelCompositeModelSummaries"
    """<p>The list of composite model summaries for the composite model.</p>"""
    action_definitions: NotRequired[
        "capo_iotsitewise.types.action_definitions.ActionDefinitions"
    ]
    """<p>The available actions for a composite model on this asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetModelCompositeModelResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["assetModelCompositeModelId"] = value["asset_model_composite_model_id"]
    if "asset_model_composite_model_external_id" in value:
        out["assetModelCompositeModelExternalId"] = value[
            "asset_model_composite_model_external_id"
        ]
    import capo_iotsitewise.types.asset_model_composite_model_path

    out["assetModelCompositeModelPath"] = (
        capo_iotsitewise.types.asset_model_composite_model_path.serialize_json(
            value["asset_model_composite_model_path"]
        )
    )
    out["assetModelCompositeModelName"] = value["asset_model_composite_model_name"]
    out["assetModelCompositeModelDescription"] = value[
        "asset_model_composite_model_description"
    ]
    out["assetModelCompositeModelType"] = value["asset_model_composite_model_type"]
    import capo_iotsitewise.types.asset_model_properties

    out["assetModelCompositeModelProperties"] = (
        capo_iotsitewise.types.asset_model_properties.serialize_json(
            value["asset_model_composite_model_properties"]
        )
    )
    if "composition_details" in value:
        import capo_iotsitewise.types.composition_details

        out["compositionDetails"] = (
            capo_iotsitewise.types.composition_details.serialize_json(
                value["composition_details"]
            )
        )
    import capo_iotsitewise.types.asset_model_composite_model_summaries

    out["assetModelCompositeModelSummaries"] = (
        capo_iotsitewise.types.asset_model_composite_model_summaries.serialize_json(
            value["asset_model_composite_model_summaries"]
        )
    )
    if "action_definitions" in value:
        import capo_iotsitewise.types.action_definitions

        out["actionDefinitions"] = (
            capo_iotsitewise.types.action_definitions.serialize_json(
                value["action_definitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetModelCompositeModelResponse:
    out: DescribeAssetModelCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_id required"
        )
    if data.get("assetModelCompositeModelId") is not None:
        out["asset_model_composite_model_id"] = data["assetModelCompositeModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_id required"
        )
    if data.get("assetModelCompositeModelExternalId") is not None:
        out["asset_model_composite_model_external_id"] = data[
            "assetModelCompositeModelExternalId"
        ]
    if data.get("assetModelCompositeModelPath") is not None:
        import capo_iotsitewise.types.asset_model_composite_model_path

        out["asset_model_composite_model_path"] = (
            capo_iotsitewise.types.asset_model_composite_model_path.deserialize_json(
                data["assetModelCompositeModelPath"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_path required"
        )
    if data.get("assetModelCompositeModelName") is not None:
        out["asset_model_composite_model_name"] = data["assetModelCompositeModelName"]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_name required"
        )
    if data.get("assetModelCompositeModelDescription") is not None:
        out["asset_model_composite_model_description"] = data[
            "assetModelCompositeModelDescription"
        ]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_description required"
        )
    if data.get("assetModelCompositeModelType") is not None:
        out["asset_model_composite_model_type"] = data["assetModelCompositeModelType"]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_type required"
        )
    if data.get("assetModelCompositeModelProperties") is not None:
        import capo_iotsitewise.types.asset_model_properties

        out["asset_model_composite_model_properties"] = (
            capo_iotsitewise.types.asset_model_properties.deserialize_json(
                data["assetModelCompositeModelProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_properties required"
        )
    if data.get("compositionDetails") is not None:
        import capo_iotsitewise.types.composition_details

        out["composition_details"] = (
            capo_iotsitewise.types.composition_details.deserialize_json(
                data["compositionDetails"]
            )
        )
    if data.get("assetModelCompositeModelSummaries") is not None:
        import capo_iotsitewise.types.asset_model_composite_model_summaries

        out["asset_model_composite_model_summaries"] = (
            capo_iotsitewise.types.asset_model_composite_model_summaries.deserialize_json(
                data["assetModelCompositeModelSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_summaries required"
        )
    if data.get("actionDefinitions") is not None:
        import capo_iotsitewise.types.action_definitions

        out["action_definitions"] = (
            capo_iotsitewise.types.action_definitions.deserialize_json(
                data["actionDefinitions"]
            )
        )
    return out
