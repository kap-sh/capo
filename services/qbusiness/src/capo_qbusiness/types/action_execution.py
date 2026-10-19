"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.action_execution_payload
    import capo_qbusiness.types.action_payload_field_name_separator
    import capo_qbusiness.types.plugin_id


class ActionExecution(TypedDict, closed=True):
    plugin_id: "capo_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the plugin the action is attached to.</p>"""
    payload: "capo_qbusiness.types.action_execution_payload.ActionExecutionPayload"
    """<p>A mapping of field names to the field values in input that an end user provides to Amazon Q Business requests to perform their plugin action. </p>"""
    payload_field_name_separator: "capo_qbusiness.types.action_payload_field_name_separator.ActionPayloadFieldNameSeparator"
    """<p>A string used to retain information about the hierarchical contexts within an action execution event payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionExecution) -> dict:
    out: dict = {}
    out["pluginId"] = value["plugin_id"]
    import capo_qbusiness.types.action_execution_payload

    out["payload"] = capo_qbusiness.types.action_execution_payload.serialize_json(
        value["payload"]
    )
    out["payloadFieldNameSeparator"] = value["payload_field_name_separator"]
    return out


def deserialize_json(data: dict) -> ActionExecution:
    out: ActionExecution = {}  # type: ignore[typeddict-item]
    if data.get("pluginId") is not None:
        out["plugin_id"] = data["pluginId"]
    else:
        out["plugin_id"] = ""
    if data.get("payload") is not None:
        import capo_qbusiness.types.action_execution_payload

        out["payload"] = capo_qbusiness.types.action_execution_payload.deserialize_json(
            data["payload"]
        )
    else:
        out["payload"] = {}
    if data.get("payloadFieldNameSeparator") is not None:
        out["payload_field_name_separator"] = data["payloadFieldNameSeparator"]
    else:
        out["payload_field_name_separator"] = ""
    return out
