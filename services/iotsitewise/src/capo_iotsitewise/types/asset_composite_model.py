"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetCompositeModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_properties
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class AssetCompositeModel(TypedDict, closed=True):
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the composite model.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The description of the composite model.</p>"""
    type: "capo_iotsitewise.types.name.Name"
    """<p>The type of the composite model. For alarm composite models, this type is <code>AWS/ALARM</code>.</p>"""
    properties: "capo_iotsitewise.types.asset_properties.AssetProperties"
    """<p>The asset properties that this composite model defines.</p>"""
    id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p> The ID of the asset composite model. </p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the asset composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetCompositeModel) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["type"] = value["type"]
    import capo_iotsitewise.types.asset_properties

    out["properties"] = capo_iotsitewise.types.asset_properties.serialize_json(
        value["properties"]
    )
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> AssetCompositeModel:
    out: AssetCompositeModel = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetCompositeModel.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssetCompositeModel.type required")
    if data.get("properties") is not None:
        import capo_iotsitewise.types.asset_properties

        out["properties"] = capo_iotsitewise.types.asset_properties.deserialize_json(
            data["properties"]
        )
    else:
        raise DeserializationError("AssetCompositeModel.properties required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    return out
