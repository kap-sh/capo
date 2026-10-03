"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_property_path
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.interface_summaries
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.property_data_type
    import capo_iotsitewise.types.property_type
    import capo_iotsitewise.types.property_unit


class AssetModelPropertySummary(TypedDict, closed=True):
    id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the property.</p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the property. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the property.</p>"""
    data_type: "capo_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the property.</p>"""
    data_type_spec: NotRequired["capo_iotsitewise.types.name.Name"]
    """<p>The data type of the structure for this property. This parameter exists on properties that have the <code>STRUCT</code> data type.</p>"""
    unit: NotRequired["capo_iotsitewise.types.property_unit.PropertyUnit"]
    """<p>The unit (such as <code>Newtons</code> or <code>RPM</code>) of the property.</p>"""
    type: "capo_iotsitewise.types.property_type.PropertyType"
    asset_model_composite_model_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p> The ID of the composite model that contains the asset model property. </p>"""
    path: NotRequired[
        "capo_iotsitewise.types.asset_model_property_path.AssetModelPropertyPath"
    ]
    """<p>The structured path to the property from the root of the asset model.</p>"""
    interface_summaries: NotRequired[
        "capo_iotsitewise.types.interface_summaries.InterfaceSummaries"
    ]
    """<p>A list of interface summaries that describe which interfaces this property belongs to, including the interface asset model ID and the corresponding property ID in the interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertySummary) -> dict:
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
    if "asset_model_composite_model_id" in value:
        out["assetModelCompositeModelId"] = value["asset_model_composite_model_id"]
    if "path" in value:
        import capo_iotsitewise.types.asset_model_property_path

        out["path"] = capo_iotsitewise.types.asset_model_property_path.serialize_json(
            value["path"]
        )
    if "interface_summaries" in value:
        import capo_iotsitewise.types.interface_summaries

        out["interfaceSummaries"] = (
            capo_iotsitewise.types.interface_summaries.serialize_json(
                value["interface_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetModelPropertySummary:
    out: AssetModelPropertySummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelPropertySummary.name required")
    if data.get("dataType") is not None:
        import capo_iotsitewise.types.property_data_type

        out["data_type"] = capo_iotsitewise.types.property_data_type.deserialize_json(
            data["dataType"]
        )
    else:
        raise DeserializationError("AssetModelPropertySummary.data_type required")
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
        raise DeserializationError("AssetModelPropertySummary.type required")
    if data.get("assetModelCompositeModelId") is not None:
        out["asset_model_composite_model_id"] = data["assetModelCompositeModelId"]
    if data.get("path") is not None:
        import capo_iotsitewise.types.asset_model_property_path

        out["path"] = capo_iotsitewise.types.asset_model_property_path.deserialize_json(
            data["path"]
        )
    if data.get("interfaceSummaries") is not None:
        import capo_iotsitewise.types.interface_summaries

        out["interface_summaries"] = (
            capo_iotsitewise.types.interface_summaries.deserialize_json(
                data["interfaceSummaries"]
            )
        )
    return out
