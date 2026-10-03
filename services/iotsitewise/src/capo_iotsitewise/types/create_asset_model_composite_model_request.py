"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAssetModelCompositeModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_property_definitions
    import capo_iotsitewise.types.asset_model_version_type
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.e_tag
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.select_all


class CreateAssetModelCompositeModelRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model this composite model is a part of.</p>"""
    asset_model_composite_model_external_id: NotRequired[
        "capo_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>An external ID to assign to the composite model.</p> <p>If the composite model is a derived composite model, or one nested inside a component model, you can only set the external ID using <code>UpdateAssetModelCompositeModel</code> and specifying the derived ID of the model or property from the created model it's a part of.</p>"""
    parent_asset_model_composite_model_id: NotRequired[
        "capo_iotsitewise.types.custom_id.CustomID"
    ]
    """<p>The ID of the parent composite model in this asset model relationship.</p>"""
    asset_model_composite_model_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the composite model. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    asset_model_composite_model_description: NotRequired[
        "capo_iotsitewise.types.description.Description"
    ]
    """<p>A description for the composite model.</p>"""
    asset_model_composite_model_name: "capo_iotsitewise.types.name.Name"
    """<p>A unique name for the composite model.</p>"""
    asset_model_composite_model_type: "capo_iotsitewise.types.name.Name"
    """<p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    composed_asset_model_id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of a component model which is reused to create this composite model.</p>"""
    asset_model_composite_model_properties: NotRequired[
        "capo_iotsitewise.types.asset_model_property_definitions.AssetModelPropertyDefinitions"
    ]
    """<p>The property definitions of the composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html#inline-composite-models"> Inline custom composite models</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    if_match: NotRequired["capo_iotsitewise.types.e_tag.ETag"]
    """<p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The create request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    if_none_match: NotRequired["capo_iotsitewise.types.select_all.SelectAll"]
    """<p>Accepts <b>*</b> to reject the create request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>"""
    match_for_version_type: NotRequired[
        "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
    ]
    """<p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the create operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetModelCompositeModelRequest) -> dict:
    out: dict = {}
    if "asset_model_composite_model_external_id" in value:
        out["assetModelCompositeModelExternalId"] = value[
            "asset_model_composite_model_external_id"
        ]
    if "parent_asset_model_composite_model_id" in value:
        out["parentAssetModelCompositeModelId"] = value[
            "parent_asset_model_composite_model_id"
        ]
    if "asset_model_composite_model_id" in value:
        out["assetModelCompositeModelId"] = value["asset_model_composite_model_id"]
    if "asset_model_composite_model_description" in value:
        out["assetModelCompositeModelDescription"] = value[
            "asset_model_composite_model_description"
        ]
    out["assetModelCompositeModelName"] = value["asset_model_composite_model_name"]
    out["assetModelCompositeModelType"] = value["asset_model_composite_model_type"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "composed_asset_model_id" in value:
        out["composedAssetModelId"] = value["composed_asset_model_id"]
    if "asset_model_composite_model_properties" in value:
        import capo_iotsitewise.types.asset_model_property_definitions

        out["assetModelCompositeModelProperties"] = (
            capo_iotsitewise.types.asset_model_property_definitions.serialize_json(
                value["asset_model_composite_model_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAssetModelCompositeModelRequest:
    out: CreateAssetModelCompositeModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("assetModelCompositeModelExternalId") is not None:
        out["asset_model_composite_model_external_id"] = data[
            "assetModelCompositeModelExternalId"
        ]
    if data.get("parentAssetModelCompositeModelId") is not None:
        out["parent_asset_model_composite_model_id"] = data[
            "parentAssetModelCompositeModelId"
        ]
    if data.get("assetModelCompositeModelId") is not None:
        out["asset_model_composite_model_id"] = data["assetModelCompositeModelId"]
    if data.get("assetModelCompositeModelDescription") is not None:
        out["asset_model_composite_model_description"] = data[
            "assetModelCompositeModelDescription"
        ]
    if data.get("assetModelCompositeModelName") is not None:
        out["asset_model_composite_model_name"] = data["assetModelCompositeModelName"]
    else:
        raise DeserializationError(
            "CreateAssetModelCompositeModelRequest.asset_model_composite_model_name required"
        )
    if data.get("assetModelCompositeModelType") is not None:
        out["asset_model_composite_model_type"] = data["assetModelCompositeModelType"]
    else:
        raise DeserializationError(
            "CreateAssetModelCompositeModelRequest.asset_model_composite_model_type required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("composedAssetModelId") is not None:
        out["composed_asset_model_id"] = data["composedAssetModelId"]
    if data.get("assetModelCompositeModelProperties") is not None:
        import capo_iotsitewise.types.asset_model_property_definitions

        out["asset_model_composite_model_properties"] = (
            capo_iotsitewise.types.asset_model_property_definitions.deserialize_json(
                data["assetModelCompositeModelProperties"]
            )
        )
    return out
