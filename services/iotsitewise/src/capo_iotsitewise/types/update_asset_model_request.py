"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAssetModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_models
    import capo_iotsitewise.types.asset_model_hierarchies
    import capo_iotsitewise.types.asset_model_properties
    import capo_iotsitewise.types.asset_model_version_type
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.e_tag
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.select_all


class UpdateAssetModelRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model to update. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_model_external_id: NotRequired[
        "capo_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>An external ID to assign to the asset model. The asset model must not already have an external ID. The external ID must be unique within your Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_model_name: "capo_iotsitewise.types.name.Name"
    """<p>A unique name for the asset model.</p>"""
    asset_model_description: NotRequired[
        "capo_iotsitewise.types.description.Description"
    ]
    """<p>A description for the asset model.</p>"""
    asset_model_properties: NotRequired[
        "capo_iotsitewise.types.asset_model_properties.AssetModelProperties"
    ]
    """<p>The updated property definitions of the asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html">Asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_model_hierarchies: NotRequired[
        "capo_iotsitewise.types.asset_model_hierarchies.AssetModelHierarchies"
    ]
    """<p>The updated hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 10 hierarchies per asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_model_composite_models: NotRequired[
        "capo_iotsitewise.types.asset_model_composite_models.AssetModelCompositeModels"
    ]
    """<p>The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.</p> <note> <p>When creating custom composite models, you need to use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html">CreateAssetModelCompositeModel</a>. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html">Creating custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p> </note>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    if_match: NotRequired["capo_iotsitewise.types.e_tag.ETag"]
    """<p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The update request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    if_none_match: NotRequired["capo_iotsitewise.types.select_all.SelectAll"]
    """<p>Accepts <b>*</b> to reject the update request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>"""
    match_for_version_type: NotRequired[
        "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
    ]
    """<p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the update operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetModelRequest) -> dict:
    out: dict = {}
    if "asset_model_external_id" in value:
        out["assetModelExternalId"] = value["asset_model_external_id"]
    out["assetModelName"] = value["asset_model_name"]
    if "asset_model_description" in value:
        out["assetModelDescription"] = value["asset_model_description"]
    if "asset_model_properties" in value:
        import capo_iotsitewise.types.asset_model_properties

        out["assetModelProperties"] = (
            capo_iotsitewise.types.asset_model_properties.serialize_json(
                value["asset_model_properties"]
            )
        )
    if "asset_model_hierarchies" in value:
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateAssetModelRequest:
    out: UpdateAssetModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("assetModelExternalId") is not None:
        out["asset_model_external_id"] = data["assetModelExternalId"]
    if data.get("assetModelName") is not None:
        out["asset_model_name"] = data["assetModelName"]
    else:
        raise DeserializationError("UpdateAssetModelRequest.asset_model_name required")
    if data.get("assetModelDescription") is not None:
        out["asset_model_description"] = data["assetModelDescription"]
    if data.get("assetModelProperties") is not None:
        import capo_iotsitewise.types.asset_model_properties

        out["asset_model_properties"] = (
            capo_iotsitewise.types.asset_model_properties.deserialize_json(
                data["assetModelProperties"]
            )
        )
    if data.get("assetModelHierarchies") is not None:
        import capo_iotsitewise.types.asset_model_hierarchies

        out["asset_model_hierarchies"] = (
            capo_iotsitewise.types.asset_model_hierarchies.deserialize_json(
                data["assetModelHierarchies"]
            )
        )
    if data.get("assetModelCompositeModels") is not None:
        import capo_iotsitewise.types.asset_model_composite_models

        out["asset_model_composite_models"] = (
            capo_iotsitewise.types.asset_model_composite_models.deserialize_json(
                data["assetModelCompositeModels"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
