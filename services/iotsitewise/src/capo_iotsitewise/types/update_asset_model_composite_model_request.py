"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAssetModelCompositeModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_properties
    import capo_iotsitewise.types.asset_model_version_type
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.e_tag
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.select_all


class UpdateAssetModelCompositeModelRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_model_composite_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of a composite model on this asset model.</p>"""
    asset_model_composite_model_external_id: NotRequired[
        "capo_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>An external ID to assign to the asset model. You can only set the external ID of the asset model if it wasn't set when it was created, or you're setting it to the exact same thing as when it was created.</p>"""
    asset_model_composite_model_description: NotRequired[
        "capo_iotsitewise.types.description.Description"
    ]
    """<p>A description for the composite model.</p>"""
    asset_model_composite_model_name: "capo_iotsitewise.types.name.Name"
    """<p>A unique name for the composite model.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    asset_model_composite_model_properties: NotRequired[
        "capo_iotsitewise.types.asset_model_properties.AssetModelProperties"
    ]
    """<p>The property definitions of the composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html#inline-composite-models"> Inline custom composite models</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    if_match: NotRequired["capo_iotsitewise.types.e_tag.ETag"]
    """<p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The update request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    if_none_match: NotRequired["capo_iotsitewise.types.select_all.SelectAll"]
    """<p>Accepts <b>*</b> to reject the update request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>"""
    match_for_version_type: NotRequired[
        "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
    ]
    """<p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the update operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetModelCompositeModelRequest) -> dict:
    out: dict = {}
    if "asset_model_composite_model_external_id" in value:
        out["assetModelCompositeModelExternalId"] = value[
            "asset_model_composite_model_external_id"
        ]
    if "asset_model_composite_model_description" in value:
        out["assetModelCompositeModelDescription"] = value[
            "asset_model_composite_model_description"
        ]
    out["assetModelCompositeModelName"] = value["asset_model_composite_model_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "asset_model_composite_model_properties" in value:
        import capo_iotsitewise.types.asset_model_properties

        out["assetModelCompositeModelProperties"] = (
            capo_iotsitewise.types.asset_model_properties.serialize_json(
                value["asset_model_composite_model_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAssetModelCompositeModelRequest:
    out: UpdateAssetModelCompositeModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("assetModelCompositeModelExternalId") is not None:
        out["asset_model_composite_model_external_id"] = data[
            "assetModelCompositeModelExternalId"
        ]
    if data.get("assetModelCompositeModelDescription") is not None:
        out["asset_model_composite_model_description"] = data[
            "assetModelCompositeModelDescription"
        ]
    if data.get("assetModelCompositeModelName") is not None:
        out["asset_model_composite_model_name"] = data["assetModelCompositeModelName"]
    else:
        raise DeserializationError(
            "UpdateAssetModelCompositeModelRequest.asset_model_composite_model_name required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("assetModelCompositeModelProperties") is not None:
        import capo_iotsitewise.types.asset_model_properties

        out["asset_model_composite_model_properties"] = (
            capo_iotsitewise.types.asset_model_properties.deserialize_json(
                data["assetModelCompositeModelProperties"]
            )
        )
    return out
