"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_model_path
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class AssetModelCompositeModelSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the composite model that this summary describes..</p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of a composite model on this asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the composite model that this summary describes..</p>"""
    type: "capo_iotsitewise.types.name.Name"
    """<p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The description of the composite model that this summary describes..</p>"""
    path: NotRequired[
        "capo_iotsitewise.types.asset_model_composite_model_path.AssetModelCompositeModelPath"
    ]
    """<p>The path that includes all the pieces that make up the composite model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModelSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "path" in value:
        import capo_iotsitewise.types.asset_model_composite_model_path

        out["path"] = (
            capo_iotsitewise.types.asset_model_composite_model_path.serialize_json(
                value["path"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetModelCompositeModelSummary:
    out: AssetModelCompositeModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssetModelCompositeModelSummary.id required")
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelCompositeModelSummary.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssetModelCompositeModelSummary.type required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("path") is not None:
        import capo_iotsitewise.types.asset_model_composite_model_path

        out["path"] = (
            capo_iotsitewise.types.asset_model_composite_model_path.deserialize_json(
                data["path"]
            )
        )
    return out
