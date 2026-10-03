"""Generated from Smithy shape ``com.amazonaws.iotsitewise#VariableValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_property_path
    import capo_iotsitewise.types.macro


class VariableValue(TypedDict, closed=True):
    property_id: NotRequired["capo_iotsitewise.types.macro.Macro"]
    """<p>The ID of the property to use as the variable. You can use the property <code>name</code> if it's from the same asset model. If the property has an external ID, you can specify <code>externalId:</code> followed by the external ID. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    hierarchy_id: NotRequired["capo_iotsitewise.types.macro.Macro"]
    """<p>The ID of the hierarchy to query for the property ID. You can use the hierarchy's name instead of the hierarchy's ID. If the hierarchy has an external ID, you can specify <code>externalId:</code> followed by the external ID. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same <code>propertyId</code>. For example, you might have separately grouped assets that come from the same asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_path: NotRequired[
        "capo_iotsitewise.types.asset_model_property_path.AssetModelPropertyPath"
    ]
    """<p>The path of the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariableValue) -> dict:
    out: dict = {}
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "hierarchy_id" in value:
        out["hierarchyId"] = value["hierarchy_id"]
    if "property_path" in value:
        import capo_iotsitewise.types.asset_model_property_path

        out["propertyPath"] = (
            capo_iotsitewise.types.asset_model_property_path.serialize_json(
                value["property_path"]
            )
        )
    return out


def deserialize_json(data: dict) -> VariableValue:
    out: VariableValue = {}  # type: ignore[typeddict-item]
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    if data.get("hierarchyId") is not None:
        out["hierarchy_id"] = data["hierarchyId"]
    if data.get("propertyPath") is not None:
        import capo_iotsitewise.types.asset_model_property_path

        out["property_path"] = (
            capo_iotsitewise.types.asset_model_property_path.deserialize_json(
                data["propertyPath"]
            )
        )
    return out
