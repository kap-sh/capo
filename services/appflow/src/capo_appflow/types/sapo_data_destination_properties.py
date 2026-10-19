"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.error_handling_config
    import capo_appflow.types.id_field_name_list
    import capo_appflow.types.object
    import capo_appflow.types.success_response_handling_config
    import capo_appflow.types.write_operation_type


class SAPODataDestinationProperties(TypedDict, closed=True):
    object_path: "capo_appflow.types.object.Object"
    """<p>The object path specified in the SAPOData flow destination.</p>"""
    success_response_handling_config: NotRequired[
        "capo_appflow.types.success_response_handling_config.SuccessResponseHandlingConfig"
    ]
    """<p>Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data.</p> <p>For example, this setting would determine where to write the response from a destination connector upon a successful insert operation.</p>"""
    id_field_names: NotRequired["capo_appflow.types.id_field_name_list.IdFieldNameList"]
    error_handling_config: NotRequired[
        "capo_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]
    write_operation_type: NotRequired[
        "capo_appflow.types.write_operation_type.WriteOperationType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataDestinationProperties) -> dict:
    out: dict = {}
    out["objectPath"] = value["object_path"]
    if "success_response_handling_config" in value:
        import capo_appflow.types.success_response_handling_config

        out["successResponseHandlingConfig"] = (
            capo_appflow.types.success_response_handling_config.serialize_json(
                value["success_response_handling_config"]
            )
        )
    if "id_field_names" in value:
        import capo_appflow.types.id_field_name_list

        out["idFieldNames"] = capo_appflow.types.id_field_name_list.serialize_json(
            value["id_field_names"]
        )
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
    return out


def deserialize_json(data: dict) -> SAPODataDestinationProperties:
    out: SAPODataDestinationProperties = {}  # type: ignore[typeddict-item]
    if data.get("objectPath") is not None:
        out["object_path"] = data["objectPath"]
    else:
        out["object_path"] = ""
    if data.get("successResponseHandlingConfig") is not None:
        import capo_appflow.types.success_response_handling_config

        out["success_response_handling_config"] = (
            capo_appflow.types.success_response_handling_config.deserialize_json(
                data["successResponseHandlingConfig"]
            )
        )
    if data.get("idFieldNames") is not None:
        import capo_appflow.types.id_field_name_list

        out["id_field_names"] = capo_appflow.types.id_field_name_list.deserialize_json(
            data["idFieldNames"]
        )
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
    return out
