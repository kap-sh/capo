"""Generated from Smithy shape ``com.amazonaws.glue#CreateTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.action_list
    import capo_glue.types.boolean_value
    import capo_glue.types.description_string
    import capo_glue.types.event_batching_condition
    import capo_glue.types.generic_string
    import capo_glue.types.name_string
    import capo_glue.types.predicate
    import capo_glue.types.tags_map
    import capo_glue.types.trigger_type


class CreateTriggerRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the trigger.</p>"""
    workflow_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the workflow associated with the trigger.</p>"""
    type: "capo_glue.types.trigger_type.TriggerType"
    """<p>The type of the new trigger.</p>"""
    schedule: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A <code>cron</code> expression used to specify the schedule (see <a href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p> <p>This field is required when the trigger type is SCHEDULED.</p>"""
    predicate: NotRequired["capo_glue.types.predicate.Predicate"]
    """<p>A predicate to specify when the new trigger should fire.</p> <p>This field is required when the trigger type is <code>CONDITIONAL</code>.</p>"""
    actions: "capo_glue.types.action_list.ActionList"
    """<p>The actions initiated by this trigger when it fires.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the new trigger.</p>"""
    start_on_creation: "capo_glue.types.boolean_value.BooleanValue"
    """<p>Set to <code>true</code> to start <code>SCHEDULED</code> and <code>CONDITIONAL</code> triggers when created. True is not supported for <code>ON_DEMAND</code> triggers.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The tags to use with this trigger. You may use tags to limit access to the trigger. For more information about tags in Glue, see <a href="https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html">Amazon Web Services Tags in Glue</a> in the developer guide. </p>"""
    event_batching_condition: NotRequired[
        "capo_glue.types.event_batching_condition.EventBatchingCondition"
    ]
    """<p>Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTriggerRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "workflow_name" in value:
        out["WorkflowName"] = value["workflow_name"]
    import capo_glue.types.trigger_type

    out["Type"] = capo_glue.types.trigger_type.serialize_aws_json_1_1(value["type"])
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "predicate" in value:
        import capo_glue.types.predicate

        out["Predicate"] = capo_glue.types.predicate.serialize_aws_json_1_1(
            value["predicate"]
        )
    import capo_glue.types.action_list

    out["Actions"] = capo_glue.types.action_list.serialize_aws_json_1_1(
        value["actions"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    out["StartOnCreation"] = value.get("start_on_creation", False)
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "event_batching_condition" in value:
        import capo_glue.types.event_batching_condition

        out["EventBatchingCondition"] = (
            capo_glue.types.event_batching_condition.serialize_aws_json_1_1(
                value["event_batching_condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTriggerRequest:
    out: CreateTriggerRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateTriggerRequest.name required")
    if data.get("WorkflowName") is not None:
        out["workflow_name"] = data["WorkflowName"]
    if data.get("Type") is not None:
        import capo_glue.types.trigger_type

        out["type"] = capo_glue.types.trigger_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateTriggerRequest.type required")
    if data.get("Schedule") is not None:
        out["schedule"] = data["Schedule"]
    if data.get("Predicate") is not None:
        import capo_glue.types.predicate

        out["predicate"] = capo_glue.types.predicate.deserialize_aws_json_1_1(
            data["Predicate"]
        )
    if data.get("Actions") is not None:
        import capo_glue.types.action_list

        out["actions"] = capo_glue.types.action_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    else:
        raise DeserializationError("CreateTriggerRequest.actions required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("StartOnCreation") is not None:
        out["start_on_creation"] = data["StartOnCreation"]
    else:
        out["start_on_creation"] = False
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("EventBatchingCondition") is not None:
        import capo_glue.types.event_batching_condition

        out["event_batching_condition"] = (
            capo_glue.types.event_batching_condition.deserialize_aws_json_1_1(
                data["EventBatchingCondition"]
            )
        )
    return out
