"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAssetModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_model_definitions
    import capo_iotsitewise.types.asset_model_hierarchy_definitions
    import capo_iotsitewise.types.asset_model_property_definitions
    import capo_iotsitewise.types.asset_model_type
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.tag_map


class CreateAssetModelRequest(TypedDict, closed=True):
    asset_model_name: "capo_iotsitewise.types.name.Name"
    """<p>A unique name for the asset model.</p>"""
    asset_model_type: NotRequired[
        "capo_iotsitewise.types.asset_model_type.AssetModelType"
    ]
    """<p>The type of asset model.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> </ul>"""
    asset_model_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID to assign to the asset model, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    asset_model_external_id: NotRequired[
        "capo_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>An external ID to assign to the asset model. The external ID must be unique within your Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_model_description: NotRequired[
        "capo_iotsitewise.types.description.Description"
    ]
    """<p>A description for the asset model.</p>"""
    asset_model_properties: NotRequired[
        "capo_iotsitewise.types.asset_model_property_definitions.AssetModelPropertyDefinitions"
    ]
    """<p>The property definitions of the asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html">Asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_model_hierarchies: NotRequired[
        "capo_iotsitewise.types.asset_model_hierarchy_definitions.AssetModelHierarchyDefinitions"
    ]
    """<p>The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 10 hierarchies per asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_model_composite_models: NotRequired[
        "capo_iotsitewise.types.asset_model_composite_model_definitions.AssetModelCompositeModelDefinitions"
    ]
    """<p>The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.</p> <note> <p>When creating custom composite models, you need to use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html">CreateAssetModelCompositeModel</a>. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html">Creating custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p> </note>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetModelRequest) -> dict:
    out: dict = {}
    out["assetModelName"] = value["asset_model_name"]
    if "asset_model_type" in value:
        import capo_iotsitewise.types.asset_model_type

        out["assetModelType"] = capo_iotsitewise.types.asset_model_type.serialize_json(
            value["asset_model_type"]
        )
    if "asset_model_id" in value:
        out["assetModelId"] = value["asset_model_id"]
    if "asset_model_external_id" in value:
        out["assetModelExternalId"] = value["asset_model_external_id"]
    if "asset_model_description" in value:
        out["assetModelDescription"] = value["asset_model_description"]
    if "asset_model_properties" in value:
        import capo_iotsitewise.types.asset_model_property_definitions

        out["assetModelProperties"] = (
            capo_iotsitewise.types.asset_model_property_definitions.serialize_json(
                value["asset_model_properties"]
            )
        )
    if "asset_model_hierarchies" in value:
        import capo_iotsitewise.types.asset_model_hierarchy_definitions

        out["assetModelHierarchies"] = (
            capo_iotsitewise.types.asset_model_hierarchy_definitions.serialize_json(
                value["asset_model_hierarchies"]
            )
        )
    if "asset_model_composite_models" in value:
        import capo_iotsitewise.types.asset_model_composite_model_definitions

        out["assetModelCompositeModels"] = (
            capo_iotsitewise.types.asset_model_composite_model_definitions.serialize_json(
                value["asset_model_composite_models"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAssetModelRequest:
    out: CreateAssetModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("assetModelName") is not None:
        out["asset_model_name"] = data["assetModelName"]
    else:
        raise DeserializationError("CreateAssetModelRequest.asset_model_name required")
    if data.get("assetModelType") is not None:
        import capo_iotsitewise.types.asset_model_type

        out["asset_model_type"] = (
            capo_iotsitewise.types.asset_model_type.deserialize_json(
                data["assetModelType"]
            )
        )
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    if data.get("assetModelExternalId") is not None:
        out["asset_model_external_id"] = data["assetModelExternalId"]
    if data.get("assetModelDescription") is not None:
        out["asset_model_description"] = data["assetModelDescription"]
    if data.get("assetModelProperties") is not None:
        import capo_iotsitewise.types.asset_model_property_definitions

        out["asset_model_properties"] = (
            capo_iotsitewise.types.asset_model_property_definitions.deserialize_json(
                data["assetModelProperties"]
            )
        )
    if data.get("assetModelHierarchies") is not None:
        import capo_iotsitewise.types.asset_model_hierarchy_definitions

        out["asset_model_hierarchies"] = (
            capo_iotsitewise.types.asset_model_hierarchy_definitions.deserialize_json(
                data["assetModelHierarchies"]
            )
        )
    if data.get("assetModelCompositeModels") is not None:
        import capo_iotsitewise.types.asset_model_composite_model_definitions

        out["asset_model_composite_models"] = (
            capo_iotsitewise.types.asset_model_composite_model_definitions.deserialize_json(
                data["assetModelCompositeModels"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    return out
