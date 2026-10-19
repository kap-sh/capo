"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.configuration
    import capo_iottwinmaker.types.data_type
    import capo_iottwinmaker.types.data_value
    import capo_iottwinmaker.types.property_display_name


class PropertyDefinitionResponse(TypedDict, closed=True):
    data_type: "capo_iottwinmaker.types.data_type.DataType"
    """<p>An object that contains information about the data type.</p>"""
    is_time_series: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property consists of time series data.</p>"""
    is_required_in_entity: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property is required in an entity.</p>"""
    is_external_id: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property ID comes from an external data store.</p>"""
    is_stored_externally: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property is stored externally.</p>"""
    is_imported: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property definition is imported from an external data store.</p>"""
    is_final: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property definition can be updated.</p>"""
    is_inherited: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property definition is inherited from a parent entity.</p>"""
    default_value: NotRequired["capo_iottwinmaker.types.data_value.DataValue"]
    """<p>An object that contains the default value.</p>"""
    configuration: NotRequired["capo_iottwinmaker.types.configuration.Configuration"]
    """<p>A mapping that specifies configuration information about the property.</p>"""
    display_name: NotRequired[
        "capo_iottwinmaker.types.property_display_name.PropertyDisplayName"
    ]
    """<p>A friendly name for the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyDefinitionResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.data_type

    out["dataType"] = capo_iottwinmaker.types.data_type.serialize_json(
        value["data_type"]
    )
    out["isTimeSeries"] = value["is_time_series"]
    out["isRequiredInEntity"] = value["is_required_in_entity"]
    out["isExternalId"] = value["is_external_id"]
    out["isStoredExternally"] = value["is_stored_externally"]
    out["isImported"] = value["is_imported"]
    out["isFinal"] = value["is_final"]
    out["isInherited"] = value["is_inherited"]
    if "default_value" in value:
        import capo_iottwinmaker.types.data_value

        out["defaultValue"] = capo_iottwinmaker.types.data_value.serialize_json(
            value["default_value"]
        )
    if "configuration" in value:
        import capo_iottwinmaker.types.configuration

        out["configuration"] = capo_iottwinmaker.types.configuration.serialize_json(
            value["configuration"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> PropertyDefinitionResponse:
    out: PropertyDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataType") is not None:
        import capo_iottwinmaker.types.data_type

        out["data_type"] = capo_iottwinmaker.types.data_type.deserialize_json(
            data["dataType"]
        )
    else:
        raise DeserializationError("PropertyDefinitionResponse.data_type required")
    if data.get("isTimeSeries") is not None:
        out["is_time_series"] = data["isTimeSeries"]
    else:
        out["is_time_series"] = False
    if data.get("isRequiredInEntity") is not None:
        out["is_required_in_entity"] = data["isRequiredInEntity"]
    else:
        out["is_required_in_entity"] = False
    if data.get("isExternalId") is not None:
        out["is_external_id"] = data["isExternalId"]
    else:
        out["is_external_id"] = False
    if data.get("isStoredExternally") is not None:
        out["is_stored_externally"] = data["isStoredExternally"]
    else:
        out["is_stored_externally"] = False
    if data.get("isImported") is not None:
        out["is_imported"] = data["isImported"]
    else:
        out["is_imported"] = False
    if data.get("isFinal") is not None:
        out["is_final"] = data["isFinal"]
    else:
        out["is_final"] = False
    if data.get("isInherited") is not None:
        out["is_inherited"] = data["isInherited"]
    else:
        out["is_inherited"] = False
    if data.get("defaultValue") is not None:
        import capo_iottwinmaker.types.data_value

        out["default_value"] = capo_iottwinmaker.types.data_value.deserialize_json(
            data["defaultValue"]
        )
    if data.get("configuration") is not None:
        import capo_iottwinmaker.types.configuration

        out["configuration"] = capo_iottwinmaker.types.configuration.deserialize_json(
            data["configuration"]
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    return out
