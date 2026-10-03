"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_property_definitions
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class AssetModelCompositeModelDefinition(TypedDict, closed=True):
    id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID to assign to the composite model, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>An external ID to assign to the composite model. The external ID must be unique among composite models within this asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the composite model.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The description of the composite model.</p>"""
    type: "capo_iotsitewise.types.name.Name"
    """<p>The type of the composite model. For alarm composite models, this type is <code>AWS/ALARM</code>.</p>"""
    properties: NotRequired[
        "capo_iotsitewise.types.asset_model_property_definitions.AssetModelPropertyDefinitions"
    ]
    """<p>The asset property definitions for this composite model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModelDefinition) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["type"] = value["type"]
    if "properties" in value:
        import capo_iotsitewise.types.asset_model_property_definitions

        out["properties"] = (
            capo_iotsitewise.types.asset_model_property_definitions.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetModelCompositeModelDefinition:
    out: AssetModelCompositeModelDefinition = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelCompositeModelDefinition.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssetModelCompositeModelDefinition.type required")
    if data.get("properties") is not None:
        import capo_iotsitewise.types.asset_model_property_definitions

        out["properties"] = (
            capo_iotsitewise.types.asset_model_property_definitions.deserialize_json(
                data["properties"]
            )
        )
    return out
