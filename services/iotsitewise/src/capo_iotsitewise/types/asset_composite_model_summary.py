"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetCompositeModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_composite_model_path
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class AssetCompositeModelSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the composite model that this summary describes.</p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>An external ID to assign to the asset model.</p> <p>If the composite model is a derived composite model, or one nested inside a component model, you can only set the external ID using <code>UpdateAssetModelCompositeModel</code> and specifying the derived ID of the model or property from the created model it's a part of.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the composite model that this summary describes.</p>"""
    type: "capo_iotsitewise.types.name.Name"
    """<p>The type of asset model.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> </ul>"""
    description: "capo_iotsitewise.types.description.Description"
    """<p>A description of the composite model that this summary describes.</p>"""
    path: "capo_iotsitewise.types.asset_composite_model_path.AssetCompositeModelPath"
    """<p>The path that includes all the components of the asset model for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetCompositeModelSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["description"] = value["description"]
    import capo_iotsitewise.types.asset_composite_model_path

    out["path"] = capo_iotsitewise.types.asset_composite_model_path.serialize_json(
        value["path"]
    )
    return out


def deserialize_json(data: dict) -> AssetCompositeModelSummary:
    out: AssetCompositeModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("path") is not None:
        import capo_iotsitewise.types.asset_composite_model_path

        out["path"] = (
            capo_iotsitewise.types.asset_composite_model_path.deserialize_json(
                data["path"]
            )
        )
    else:
        out["path"] = []
    return out
