"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_property_path
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.property_data_type
    import capo_iotsitewise.types.property_type
    import capo_iotsitewise.types.property_unit


class AssetModelProperty(TypedDict, closed=True):
    id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of the asset model property.</p> <ul> <li> <p>If you are callling <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a> to create a <i>new</i> property: You can specify its ID here, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p> </li> <li> <p>If you are calling UpdateAssetModel to modify an <i>existing</i> property: This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p> </li> </ul>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID (if any) provided in the <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html">CreateAssetModel</a> or <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a> operation. You can assign an external ID by specifying this value as part of a call to <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a>. However, you can't change the external ID if one is already assigned. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the asset model property.</p>"""
    data_type: "capo_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the asset model property.</p> <p>The <code>VIDEO</code>, <code>ANNOTATION</code>, and <code>JSON</code> data types aren't supported for asset model properties. These types are used only by time series that store data for datasets in a workspace.</p> <p>If you specify <code>STRUCT</code>, you must also specify <code>dataTypeSpec</code> to identify the type of the structure for this property.</p>"""
    data_type_spec: NotRequired["capo_iotsitewise.types.name.Name"]
    """<p>The data type of the structure for this property. This parameter exists on properties that have the <code>STRUCT</code> data type.</p>"""
    unit: NotRequired["capo_iotsitewise.types.property_unit.PropertyUnit"]
    """<p>The unit of the asset model property, such as <code>Newtons</code> or <code>RPM</code>.</p>"""
    type: "capo_iotsitewise.types.property_type.PropertyType"
    """<p>The property type (see <code>PropertyType</code>).</p>"""
    path: NotRequired[
        "capo_iotsitewise.types.asset_model_property_path.AssetModelPropertyPath"
    ]
    """<p>The structured path to the property from the root of the asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelProperty) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    import capo_iotsitewise.types.property_data_type

    out["dataType"] = capo_iotsitewise.types.property_data_type.serialize_json(
        value["data_type"]
    )
    if "data_type_spec" in value:
        out["dataTypeSpec"] = value["data_type_spec"]
    if "unit" in value:
        out["unit"] = value["unit"]
    import capo_iotsitewise.types.property_type

    out["type"] = capo_iotsitewise.types.property_type.serialize_json(value["type"])
    if "path" in value:
        import capo_iotsitewise.types.asset_model_property_path

        out["path"] = capo_iotsitewise.types.asset_model_property_path.serialize_json(
            value["path"]
        )
    return out


def deserialize_json(data: dict) -> AssetModelProperty:
    out: AssetModelProperty = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelProperty.name required")
    if data.get("dataType") is not None:
        import capo_iotsitewise.types.property_data_type

        out["data_type"] = capo_iotsitewise.types.property_data_type.deserialize_json(
            data["dataType"]
        )
    else:
        raise DeserializationError("AssetModelProperty.data_type required")
    if data.get("dataTypeSpec") is not None:
        out["data_type_spec"] = data["dataTypeSpec"]
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    if data.get("type") is not None:
        import capo_iotsitewise.types.property_type

        out["type"] = capo_iotsitewise.types.property_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("AssetModelProperty.type required")
    if data.get("path") is not None:
        import capo_iotsitewise.types.asset_model_property_path

        out["path"] = capo_iotsitewise.types.asset_model_property_path.deserialize_json(
            data["path"]
        )
    return out
