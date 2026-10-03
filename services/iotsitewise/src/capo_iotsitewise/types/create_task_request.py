"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.tag_map
    import capo_iotsitewise.types.task_configuration
    import capo_iotsitewise.types.workspace_name


class CreateTaskRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    task_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the task to create. Must be unique within the workspace.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A description of the task.</p>"""
    task_configuration: "capo_iotsitewise.types.task_configuration.TaskConfiguration"
    """<p>The task execution configuration. Specify a <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html">containerTaskConfiguration</a> for custom container workloads.</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the task. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your AWS IoT SiteWise resources</a> in the AWS IoT SiteWise User Guide.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTaskRequest) -> dict:
    out: dict = {}
    out["taskName"] = value["task_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_iotsitewise.types.task_configuration

    out["taskConfiguration"] = capo_iotsitewise.types.task_configuration.serialize_json(
        value["task_configuration"]
    )
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTaskRequest:
    out: CreateTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskName") is not None:
        out["task_name"] = data["taskName"]
    else:
        raise DeserializationError("CreateTaskRequest.task_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("taskConfiguration") is not None:
        import capo_iotsitewise.types.task_configuration

        out["task_configuration"] = (
            capo_iotsitewise.types.task_configuration.deserialize_json(
                data["taskConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateTaskRequest.task_configuration required")
    if data.get("tags") is not None:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
