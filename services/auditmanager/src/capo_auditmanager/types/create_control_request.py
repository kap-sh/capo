"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateControlRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.action_plan_instructions
    import capo_auditmanager.types.action_plan_title
    import capo_auditmanager.types.control_description
    import capo_auditmanager.types.control_name
    import capo_auditmanager.types.create_control_mapping_sources
    import capo_auditmanager.types.tag_map
    import capo_auditmanager.types.testing_information


class CreateControlRequest(TypedDict, closed=True):
    name: "capo_auditmanager.types.control_name.ControlName"
    """<p> The name of the control. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.control_description.ControlDescription"
    ]
    """<p> The description of the control. </p>"""
    testing_information: NotRequired[
        "capo_auditmanager.types.testing_information.TestingInformation"
    ]
    """<p> The steps to follow to determine if the control is satisfied. </p>"""
    action_plan_title: NotRequired[
        "capo_auditmanager.types.action_plan_title.ActionPlanTitle"
    ]
    """<p> The title of the action plan for remediating the control. </p>"""
    action_plan_instructions: NotRequired[
        "capo_auditmanager.types.action_plan_instructions.ActionPlanInstructions"
    ]
    """<p> The recommended actions to carry out if the control isn't fulfilled. </p>"""
    control_mapping_sources: "capo_auditmanager.types.create_control_mapping_sources.CreateControlMappingSources"
    """<p> The data mapping sources for the control. </p>"""
    tags: NotRequired["capo_auditmanager.types.tag_map.TagMap"]
    """<p> The tags that are associated with the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateControlRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "testing_information" in value:
        out["testingInformation"] = value["testing_information"]
    if "action_plan_title" in value:
        out["actionPlanTitle"] = value["action_plan_title"]
    if "action_plan_instructions" in value:
        out["actionPlanInstructions"] = value["action_plan_instructions"]
    import capo_auditmanager.types.create_control_mapping_sources

    out["controlMappingSources"] = (
        capo_auditmanager.types.create_control_mapping_sources.serialize_json(
            value["control_mapping_sources"]
        )
    )
    if "tags" in value:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateControlRequest:
    out: CreateControlRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("testingInformation") is not None:
        out["testing_information"] = data["testingInformation"]
    if data.get("actionPlanTitle") is not None:
        out["action_plan_title"] = data["actionPlanTitle"]
    if data.get("actionPlanInstructions") is not None:
        out["action_plan_instructions"] = data["actionPlanInstructions"]
    if data.get("controlMappingSources") is not None:
        import capo_auditmanager.types.create_control_mapping_sources

        out["control_mapping_sources"] = (
            capo_auditmanager.types.create_control_mapping_sources.deserialize_json(
                data["controlMappingSources"]
            )
        )
    else:
        out["control_mapping_sources"] = []
    if data.get("tags") is not None:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateControlRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "testing_information" in value:
        out["testing_information"] = "*** Sensitive Data Redacted ***"
    if "action_plan_title" in value:
        out["action_plan_title"] = "*** Sensitive Data Redacted ***"
    if "action_plan_instructions" in value:
        out["action_plan_instructions"] = "*** Sensitive Data Redacted ***"
    if "control_mapping_sources" in value:
        import capo_auditmanager.types.create_control_mapping_sources

        out["control_mapping_sources"] = (
            capo_auditmanager.types.create_control_mapping_sources.redact_sensitive(
                value["control_mapping_sources"]
            )
        )
    return out
