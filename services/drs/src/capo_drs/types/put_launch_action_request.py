"""Generated from Smithy shape ``com.amazonaws.drs#PutLaunchActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_action_category
    import capo_drs.types.launch_action_description
    import capo_drs.types.launch_action_id
    import capo_drs.types.launch_action_name
    import capo_drs.types.launch_action_order
    import capo_drs.types.launch_action_parameters
    import capo_drs.types.launch_action_resource_id
    import capo_drs.types.launch_action_version
    import capo_drs.types.ssm_document_name


class PutLaunchActionRequest(TypedDict, closed=True):
    resource_id: "capo_drs.types.launch_action_resource_id.LaunchActionResourceId"
    action_code: "capo_drs.types.ssm_document_name.SsmDocumentName"
    """<p>Launch action code.</p>"""
    order: "capo_drs.types.launch_action_order.LaunchActionOrder"
    action_id: "capo_drs.types.launch_action_id.LaunchActionId"
    optional: "bool"
    """<p>Whether the launch will not be marked as failed if this action fails.</p>"""
    active: "bool"
    """<p>Whether the launch action is active.</p>"""
    name: "capo_drs.types.launch_action_name.LaunchActionName"
    action_version: "capo_drs.types.launch_action_version.LaunchActionVersion"
    category: "capo_drs.types.launch_action_category.LaunchActionCategory"
    parameters: NotRequired[
        "capo_drs.types.launch_action_parameters.LaunchActionParameters"
    ]
    description: "capo_drs.types.launch_action_description.LaunchActionDescription"


# --- restJson1 ser/de ---
def serialize_json(value: PutLaunchActionRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    out["actionCode"] = value["action_code"]
    out["order"] = value["order"]
    out["actionId"] = value["action_id"]
    out["optional"] = value["optional"]
    out["active"] = value["active"]
    out["name"] = value["name"]
    out["actionVersion"] = value["action_version"]
    out["category"] = value["category"]
    if "parameters" in value:
        import capo_drs.types.launch_action_parameters

        out["parameters"] = capo_drs.types.launch_action_parameters.serialize_json(
            value["parameters"]
        )
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PutLaunchActionRequest:
    out: PutLaunchActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("actionCode") is not None:
        out["action_code"] = data["actionCode"]
    else:
        out["action_code"] = ""
    if data.get("order") is not None:
        out["order"] = data["order"]
    else:
        out["order"] = 0
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        out["action_id"] = ""
    if data.get("optional") is not None:
        out["optional"] = data["optional"]
    else:
        out["optional"] = False
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        out["active"] = False
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("actionVersion") is not None:
        out["action_version"] = data["actionVersion"]
    else:
        out["action_version"] = ""
    if data.get("category") is not None:
        out["category"] = data["category"]
    else:
        out["category"] = ""
    if data.get("parameters") is not None:
        import capo_drs.types.launch_action_parameters

        out["parameters"] = capo_drs.types.launch_action_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
