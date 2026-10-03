"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositeModelProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.property


class CompositeModelProperty(TypedDict, closed=True):
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the property.</p>"""
    type: "capo_iotsitewise.types.name.Name"
    """<p>The type of the composite model that defines this property.</p>"""
    asset_property: "capo_iotsitewise.types.property.Property"
    id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p> The ID of the composite model that contains the property. </p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the composite model that contains the property. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeModelProperty) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    import capo_iotsitewise.types.property

    out["assetProperty"] = capo_iotsitewise.types.property.serialize_json(
        value["asset_property"]
    )
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> CompositeModelProperty:
    out: CompositeModelProperty = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CompositeModelProperty.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CompositeModelProperty.type required")
    if data.get("assetProperty") is not None:
        import capo_iotsitewise.types.property

        out["asset_property"] = capo_iotsitewise.types.property.deserialize_json(
            data["assetProperty"]
        )
    else:
        raise DeserializationError("CompositeModelProperty.asset_property required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    return out
