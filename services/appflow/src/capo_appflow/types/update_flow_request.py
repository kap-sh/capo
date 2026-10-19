"""Generated from Smithy shape ``com.amazonaws.appflow#UpdateFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.client_token
    import capo_appflow.types.destination_flow_config_list
    import capo_appflow.types.flow_description
    import capo_appflow.types.flow_name
    import capo_appflow.types.metadata_catalog_config
    import capo_appflow.types.source_flow_config
    import capo_appflow.types.tasks
    import capo_appflow.types.trigger_config


class UpdateFlowRequest(TypedDict, closed=True):
    flow_name: "capo_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    description: NotRequired["capo_appflow.types.flow_description.FlowDescription"]
    """<p> A description of the flow. </p>"""
    trigger_config: "capo_appflow.types.trigger_config.TriggerConfig"
    """<p> The trigger settings that determine how and when the flow runs. </p>"""
    source_flow_config: "capo_appflow.types.source_flow_config.SourceFlowConfig"
    destination_flow_config_list: (
        "capo_appflow.types.destination_flow_config_list.DestinationFlowConfigList"
    )
    """<p> The configuration that controls how Amazon AppFlow transfers data to the destination connector. </p>"""
    tasks: "capo_appflow.types.tasks.Tasks"
    """<p> A list of tasks that Amazon AppFlow performs while transferring the data in the flow run. </p>"""
    metadata_catalog_config: NotRequired[
        "capo_appflow.types.metadata_catalog_config.MetadataCatalogConfig"
    ]
    """<p>Specifies the configuration that Amazon AppFlow uses when it catalogs the data that's transferred by the associated flow. When Amazon AppFlow catalogs the data from a flow, it stores metadata in a data catalog.</p>"""
    client_token: NotRequired["capo_appflow.types.client_token.ClientToken"]
    """<p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>UpdateFlow</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>UpdateFlow</code>. The token is active for 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_appflow.types.trigger_config

    out["triggerConfig"] = capo_appflow.types.trigger_config.serialize_json(
        value["trigger_config"]
    )
    import capo_appflow.types.source_flow_config

    out["sourceFlowConfig"] = capo_appflow.types.source_flow_config.serialize_json(
        value["source_flow_config"]
    )
    import capo_appflow.types.destination_flow_config_list

    out["destinationFlowConfigList"] = (
        capo_appflow.types.destination_flow_config_list.serialize_json(
            value["destination_flow_config_list"]
        )
    )
    import capo_appflow.types.tasks

    out["tasks"] = capo_appflow.types.tasks.serialize_json(value["tasks"])
    if "metadata_catalog_config" in value:
        import capo_appflow.types.metadata_catalog_config

        out["metadataCatalogConfig"] = (
            capo_appflow.types.metadata_catalog_config.serialize_json(
                value["metadata_catalog_config"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateFlowRequest:
    out: UpdateFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("flowName") is not None:
        out["flow_name"] = data["flowName"]
    else:
        out["flow_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("triggerConfig") is not None:
        import capo_appflow.types.trigger_config

        out["trigger_config"] = capo_appflow.types.trigger_config.deserialize_json(
            data["triggerConfig"]
        )
    else:
        raise DeserializationError("UpdateFlowRequest.trigger_config required")
    if data.get("sourceFlowConfig") is not None:
        import capo_appflow.types.source_flow_config

        out["source_flow_config"] = (
            capo_appflow.types.source_flow_config.deserialize_json(
                data["sourceFlowConfig"]
            )
        )
    else:
        raise DeserializationError("UpdateFlowRequest.source_flow_config required")
    if data.get("destinationFlowConfigList") is not None:
        import capo_appflow.types.destination_flow_config_list

        out["destination_flow_config_list"] = (
            capo_appflow.types.destination_flow_config_list.deserialize_json(
                data["destinationFlowConfigList"]
            )
        )
    else:
        out["destination_flow_config_list"] = []
    if data.get("tasks") is not None:
        import capo_appflow.types.tasks

        out["tasks"] = capo_appflow.types.tasks.deserialize_json(data["tasks"])
    else:
        out["tasks"] = []
    if data.get("metadataCatalogConfig") is not None:
        import capo_appflow.types.metadata_catalog_config

        out["metadata_catalog_config"] = (
            capo_appflow.types.metadata_catalog_config.deserialize_json(
                data["metadataCatalogConfig"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
