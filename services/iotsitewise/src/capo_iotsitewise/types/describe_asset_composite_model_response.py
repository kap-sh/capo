"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetCompositeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.action_definitions
    import capo_iotsitewise.types.asset_composite_model_path
    import capo_iotsitewise.types.asset_composite_model_summaries
    import capo_iotsitewise.types.asset_properties
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class DescribeAssetCompositeModelResponse(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format. This ID uniquely identifies the asset within IoT SiteWise and can be used with other IoT SiteWise APIs.</p>"""
    asset_composite_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of a composite model on this asset.</p>"""
    asset_composite_model_external_id: NotRequired[
        "capo_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>An external ID to assign to the asset model.</p> <p>If the composite model is a component-based composite model, or one nested inside a component model, you can only set the external ID using <code>UpdateAssetModelCompositeModel</code> and specifying the derived ID of the model or property from the created model it's a part of.</p>"""
    asset_composite_model_path: (
        "capo_iotsitewise.types.asset_composite_model_path.AssetCompositeModelPath"
    )
    """<p>The path to the composite model listing the parent composite models.</p>"""
    asset_composite_model_name: "capo_iotsitewise.types.name.Name"
    """<p>The unique, friendly name for the composite model.</p>"""
    asset_composite_model_description: "capo_iotsitewise.types.description.Description"
    """<p>A description for the composite model.</p>"""
    asset_composite_model_type: "capo_iotsitewise.types.name.Name"
    """<p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>"""
    asset_composite_model_properties: (
        "capo_iotsitewise.types.asset_properties.AssetProperties"
    )
    """<p>The property definitions of the composite model that was used to create the asset.</p>"""
    asset_composite_model_summaries: "capo_iotsitewise.types.asset_composite_model_summaries.AssetCompositeModelSummaries"
    """<p>The list of composite model summaries.</p>"""
    action_definitions: NotRequired[
        "capo_iotsitewise.types.action_definitions.ActionDefinitions"
    ]
    """<p>The available actions for a composite model on this asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetCompositeModelResponse) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["assetCompositeModelId"] = value["asset_composite_model_id"]
    if "asset_composite_model_external_id" in value:
        out["assetCompositeModelExternalId"] = value[
            "asset_composite_model_external_id"
        ]
    import capo_iotsitewise.types.asset_composite_model_path

    out["assetCompositeModelPath"] = (
        capo_iotsitewise.types.asset_composite_model_path.serialize_json(
            value["asset_composite_model_path"]
        )
    )
    out["assetCompositeModelName"] = value["asset_composite_model_name"]
    out["assetCompositeModelDescription"] = value["asset_composite_model_description"]
    out["assetCompositeModelType"] = value["asset_composite_model_type"]
    import capo_iotsitewise.types.asset_properties

    out["assetCompositeModelProperties"] = (
        capo_iotsitewise.types.asset_properties.serialize_json(
            value["asset_composite_model_properties"]
        )
    )
    import capo_iotsitewise.types.asset_composite_model_summaries

    out["assetCompositeModelSummaries"] = (
        capo_iotsitewise.types.asset_composite_model_summaries.serialize_json(
            value["asset_composite_model_summaries"]
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


def deserialize_json(data: dict) -> DescribeAssetCompositeModelResponse:
    out: DescribeAssetCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("assetCompositeModelId") is not None:
        out["asset_composite_model_id"] = data["assetCompositeModelId"]
    else:
        out["asset_composite_model_id"] = ""
    if data.get("assetCompositeModelExternalId") is not None:
        out["asset_composite_model_external_id"] = data["assetCompositeModelExternalId"]
    if data.get("assetCompositeModelPath") is not None:
        import capo_iotsitewise.types.asset_composite_model_path

        out["asset_composite_model_path"] = (
            capo_iotsitewise.types.asset_composite_model_path.deserialize_json(
                data["assetCompositeModelPath"]
            )
        )
    else:
        out["asset_composite_model_path"] = []
    if data.get("assetCompositeModelName") is not None:
        out["asset_composite_model_name"] = data["assetCompositeModelName"]
    else:
        out["asset_composite_model_name"] = ""
    if data.get("assetCompositeModelDescription") is not None:
        out["asset_composite_model_description"] = data[
            "assetCompositeModelDescription"
        ]
    else:
        out["asset_composite_model_description"] = ""
    if data.get("assetCompositeModelType") is not None:
        out["asset_composite_model_type"] = data["assetCompositeModelType"]
    else:
        out["asset_composite_model_type"] = ""
    if data.get("assetCompositeModelProperties") is not None:
        import capo_iotsitewise.types.asset_properties

        out["asset_composite_model_properties"] = (
            capo_iotsitewise.types.asset_properties.deserialize_json(
                data["assetCompositeModelProperties"]
            )
        )
    else:
        out["asset_composite_model_properties"] = []
    if data.get("assetCompositeModelSummaries") is not None:
        import capo_iotsitewise.types.asset_composite_model_summaries

        out["asset_composite_model_summaries"] = (
            capo_iotsitewise.types.asset_composite_model_summaries.deserialize_json(
                data["assetCompositeModelSummaries"]
            )
        )
    else:
        out["asset_composite_model_summaries"] = []
    if data.get("actionDefinitions") is not None:
        import capo_iotsitewise.types.action_definitions

        out["action_definitions"] = (
            capo_iotsitewise.types.action_definitions.deserialize_json(
                data["actionDefinitions"]
            )
        )
    return out
