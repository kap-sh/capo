"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateWirelessGatewayTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.auto_create_tasks
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.tag_list
    import capo_iot_wireless.types.update_wireless_gateway_task_create
    import capo_iot_wireless.types.wireless_gateway_task_name


class CreateWirelessGatewayTaskDefinitionRequest(TypedDict, closed=True):
    auto_create_tasks: "capo_iot_wireless.types.auto_create_tasks.AutoCreateTasks"
    """<p>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If <code>false</code>, the task must me created by calling <code>CreateWirelessGatewayTask</code>.</p>"""
    name: NotRequired[
        "capo_iot_wireless.types.wireless_gateway_task_name.WirelessGatewayTaskName"
    ]
    """<p>The name of the new resource.</p>"""
    update: NotRequired[
        "capo_iot_wireless.types.update_wireless_gateway_task_create.UpdateWirelessGatewayTaskCreate"
    ]
    """<p>Information about the gateways to update.</p>"""
    client_request_token: NotRequired[
        "capo_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    """<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWirelessGatewayTaskDefinitionRequest) -> dict:
    out: dict = {}
    out["AutoCreateTasks"] = value.get("auto_create_tasks", False)
    if "name" in value:
        out["Name"] = value["name"]
    if "update" in value:
        import capo_iot_wireless.types.update_wireless_gateway_task_create

        out["Update"] = (
            capo_iot_wireless.types.update_wireless_gateway_task_create.serialize_json(
                value["update"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_iot_wireless.types.tag_list

        out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWirelessGatewayTaskDefinitionRequest:
    out: CreateWirelessGatewayTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoCreateTasks") is not None:
        out["auto_create_tasks"] = data["AutoCreateTasks"]
    else:
        out["auto_create_tasks"] = False
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Update") is not None:
        import capo_iot_wireless.types.update_wireless_gateway_task_create

        out["update"] = (
            capo_iot_wireless.types.update_wireless_gateway_task_create.deserialize_json(
                data["Update"]
            )
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    return out
