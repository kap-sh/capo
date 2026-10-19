"""Generated from Smithy shape ``com.amazonaws.appflow#ZendeskDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.error_handling_config
    import capo_appflow.types.id_field_name_list
    import capo_appflow.types.object
    import capo_appflow.types.write_operation_type


class ZendeskDestinationProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p>The object specified in the Zendesk flow destination.</p>"""
    id_field_names: NotRequired["capo_appflow.types.id_field_name_list.IdFieldNameList"]
    error_handling_config: NotRequired[
        "capo_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]
    write_operation_type: NotRequired[
        "capo_appflow.types.write_operation_type.WriteOperationType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ZendeskDestinationProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
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


def deserialize_json(data: dict) -> ZendeskDestinationProperties:
    out: ZendeskDestinationProperties = {}  # type: ignore[typeddict-item]
    if data.get("object") is not None:
        out["object"] = data["object"]
    else:
        out["object"] = ""
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
