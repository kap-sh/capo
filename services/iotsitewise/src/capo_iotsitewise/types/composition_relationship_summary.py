"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositionRelationshipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class CompositionRelationshipSummary(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_model_composite_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of a composite model on this asset model.</p>"""
    asset_model_composite_model_type: "capo_iotsitewise.types.name.Name"
    """<p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositionRelationshipSummary) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["assetModelCompositeModelId"] = value["asset_model_composite_model_id"]
    out["assetModelCompositeModelType"] = value["asset_model_composite_model_type"]
    return out


def deserialize_json(data: dict) -> CompositionRelationshipSummary:
    out: CompositionRelationshipSummary = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        out["asset_model_id"] = ""
    if data.get("assetModelCompositeModelId") is not None:
        out["asset_model_composite_model_id"] = data["assetModelCompositeModelId"]
    else:
        out["asset_model_composite_model_id"] = ""
    if data.get("assetModelCompositeModelType") is not None:
        out["asset_model_composite_model_type"] = data["assetModelCompositeModelType"]
    else:
        out["asset_model_composite_model_type"] = ""
    return out
