"""Generated from Smithy shape ``com.amazonaws.glue#Trigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.action_list
    import capo_glue.types.description_string
    import capo_glue.types.event_batching_condition
    import capo_glue.types.generic_string
    import capo_glue.types.id_string
    import capo_glue.types.name_string
    import capo_glue.types.predicate
    import capo_glue.types.trigger_state
    import capo_glue.types.trigger_type


class Trigger(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the trigger.</p>"""
    workflow_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the workflow associated with the trigger.</p>"""
    id: NotRequired["capo_glue.types.id_string.IdString"]
    """<p>Reserved for future use.</p>"""
    type: NotRequired["capo_glue.types.trigger_type.TriggerType"]
    """<p>The type of trigger that this is.</p>"""
    state: NotRequired["capo_glue.types.trigger_state.TriggerState"]
    """<p>The current state of the trigger.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of this trigger.</p>"""
    schedule: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A <code>cron</code> expression used to specify the schedule (see <a href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p>"""
    actions: NotRequired["capo_glue.types.action_list.ActionList"]
    """<p>The actions initiated by this trigger.</p>"""
    predicate: NotRequired["capo_glue.types.predicate.Predicate"]
    """<p>The predicate of this trigger, which defines when it will fire.</p>"""
    event_batching_condition: NotRequired[
        "capo_glue.types.event_batching_condition.EventBatchingCondition"
    ]
    """<p>Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trigger) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "workflow_name" in value:
        out["WorkflowName"] = value["workflow_name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_glue.types.trigger_type

        out["Type"] = capo_glue.types.trigger_type.serialize_aws_json_1_1(value["type"])
    if "state" in value:
        import capo_glue.types.trigger_state

        out["State"] = capo_glue.types.trigger_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "actions" in value:
        import capo_glue.types.action_list

        out["Actions"] = capo_glue.types.action_list.serialize_aws_json_1_1(
            value["actions"]
        )
    if "predicate" in value:
        import capo_glue.types.predicate

        out["Predicate"] = capo_glue.types.predicate.serialize_aws_json_1_1(
            value["predicate"]
        )
    if "event_batching_condition" in value:
        import capo_glue.types.event_batching_condition

        out["EventBatchingCondition"] = (
            capo_glue.types.event_batching_condition.serialize_aws_json_1_1(
                value["event_batching_condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Trigger:
    out: Trigger = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("WorkflowName") is not None:
        out["workflow_name"] = data["WorkflowName"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_glue.types.trigger_type

        out["type"] = capo_glue.types.trigger_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("State") is not None:
        import capo_glue.types.trigger_state

        out["state"] = capo_glue.types.trigger_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Schedule") is not None:
        out["schedule"] = data["Schedule"]
    if data.get("Actions") is not None:
        import capo_glue.types.action_list

        out["actions"] = capo_glue.types.action_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    if data.get("Predicate") is not None:
        import capo_glue.types.predicate

        out["predicate"] = capo_glue.types.predicate.deserialize_aws_json_1_1(
            data["Predicate"]
        )
    if data.get("EventBatchingCondition") is not None:
        import capo_glue.types.event_batching_condition

        out["event_batching_condition"] = (
            capo_glue.types.event_batching_condition.deserialize_aws_json_1_1(
                data["EventBatchingCondition"]
            )
        )
    return out
