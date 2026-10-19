"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#CreateTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.command
    import capo_snow_device_management.types.idempotency_token
    import capo_snow_device_management.types.tag_map
    import capo_snow_device_management.types.target_list
    import capo_snow_device_management.types.task_description_string


class CreateTaskInput(TypedDict, closed=True):
    targets: "capo_snow_device_management.types.target_list.TargetList"
    """<p>A list of managed device IDs.</p>"""
    command: "capo_snow_device_management.types.command.Command"
    """<p>The task to be performed. Only one task is executed on a device at a time.</p>"""
    description: NotRequired[
        "capo_snow_device_management.types.task_description_string.TaskDescriptionString"
    ]
    """<p>A description of the task and its targets.</p>"""
    tags: NotRequired["capo_snow_device_management.types.tag_map.TagMap"]
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment. </p>"""
    client_token: NotRequired[
        "capo_snow_device_management.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token ensuring that the action is called only once with the specified details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTaskInput) -> dict:
    out: dict = {}
    import capo_snow_device_management.types.target_list

    out["targets"] = capo_snow_device_management.types.target_list.serialize_json(
        value["targets"]
    )
    import capo_snow_device_management.types.command

    out["command"] = capo_snow_device_management.types.command.serialize_json(
        value["command"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_snow_device_management.types.tag_map

        out["tags"] = capo_snow_device_management.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTaskInput:
    out: CreateTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("targets") is not None:
        import capo_snow_device_management.types.target_list

        out["targets"] = capo_snow_device_management.types.target_list.deserialize_json(
            data["targets"]
        )
    else:
        out["targets"] = []
    if data.get("command") is not None:
        import capo_snow_device_management.types.command

        out["command"] = capo_snow_device_management.types.command.deserialize_json(
            data["command"]
        )
    else:
        import capo_snow_device_management.types._unknown

        out["command"] = capo_snow_device_management.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_snow_device_management.types.tag_map

        out["tags"] = capo_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
