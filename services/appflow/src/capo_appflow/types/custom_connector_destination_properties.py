"""Generated from Smithy shape ``com.amazonaws.appflow#CustomConnectorDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.custom_properties
    import capo_appflow.types.entity_name
    import capo_appflow.types.error_handling_config
    import capo_appflow.types.id_field_name_list
    import capo_appflow.types.write_operation_type


class CustomConnectorDestinationProperties(TypedDict, closed=True):
    entity_name: "capo_appflow.types.entity_name.EntityName"
    """<p>The entity specified in the custom connector as a destination in the flow.</p>"""
    error_handling_config: NotRequired[
        "capo_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]
    """<p>The settings that determine how Amazon AppFlow handles an error when placing data in the custom connector as destination.</p>"""
    write_operation_type: NotRequired[
        "capo_appflow.types.write_operation_type.WriteOperationType"
    ]
    """<p>Specifies the type of write operation to be performed in the custom connector when it's used as destination.</p>"""
    id_field_names: NotRequired["capo_appflow.types.id_field_name_list.IdFieldNameList"]
    """<p>The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update, delete, or upsert.</p>"""
    custom_properties: NotRequired[
        "capo_appflow.types.custom_properties.CustomProperties"
    ]
    """<p>The custom properties that are specific to the connector when it's used as a destination in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomConnectorDestinationProperties) -> dict:
    out: dict = {}
    out["entityName"] = value["entity_name"]
    if "error_handling_config" in value:
        import capo_appflow.types.error_handling_config

        out["errorHandlingConfig"] = (
            capo_appflow.types.error_handling_config.serialize_json(
                value["error_handling_config"]
            )
        )
    if "write_operation_type" in value:
        import capo_appflow.types.write_operation_type

        out["writeOperationType"] = (
            capo_appflow.types.write_operation_type.serialize_json(
                value["write_operation_type"]
            )
        )
    if "id_field_names" in value:
        import capo_appflow.types.id_field_name_list

        out["idFieldNames"] = capo_appflow.types.id_field_name_list.serialize_json(
            value["id_field_names"]
        )
    if "custom_properties" in value:
        import capo_appflow.types.custom_properties

        out["customProperties"] = capo_appflow.types.custom_properties.serialize_json(
            value["custom_properties"]
        )
    return out


def deserialize_json(data: dict) -> CustomConnectorDestinationProperties:
    out: CustomConnectorDestinationProperties = {}  # type: ignore[typeddict-item]
    if data.get("entityName") is not None:
        out["entity_name"] = data["entityName"]
    else:
        out["entity_name"] = ""
    if data.get("errorHandlingConfig") is not None:
        import capo_appflow.types.error_handling_config

        out["error_handling_config"] = (
            capo_appflow.types.error_handling_config.deserialize_json(
                data["errorHandlingConfig"]
            )
        )
    if data.get("writeOperationType") is not None:
        import capo_appflow.types.write_operation_type

        out["write_operation_type"] = (
            capo_appflow.types.write_operation_type.deserialize_json(
                data["writeOperationType"]
            )
        )
    if data.get("idFieldNames") is not None:
        import capo_appflow.types.id_field_name_list

        out["id_field_names"] = capo_appflow.types.id_field_name_list.deserialize_json(
            data["idFieldNames"]
        )
    if data.get("customProperties") is not None:
        import capo_appflow.types.custom_properties

        out["custom_properties"] = (
            capo_appflow.types.custom_properties.deserialize_json(
                data["customProperties"]
            )
        )
    return out
