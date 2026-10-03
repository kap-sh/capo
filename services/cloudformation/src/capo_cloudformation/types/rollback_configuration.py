"""Generated from Smithy shape ``com.amazonaws.cloudformation#RollbackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.monitoring_time_in_minutes
    import capo_cloudformation.types.rollback_triggers


class RollbackConfiguration(TypedDict, closed=True):
    rollback_triggers: NotRequired[
        "capo_cloudformation.types.rollback_triggers.RollbackTriggers"
    ]
    """<p>The triggers to monitor during stack creation or update actions.</p> <p>By default, CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:</p> <ul> <li> <p>To use the rollback triggers previously specified for this stack, if any, don't specify this parameter.</p> </li> <li> <p>To specify new or updated rollback triggers, you must specify <i>all</i> the triggers that you want used for this stack, even triggers you've specified before (for example, when creating the stack or during a previous stack update). Any triggers that you don't include in the updated list of triggers are no longer applied to the stack.</p> </li> <li> <p>To remove all currently specified triggers, specify an empty list for this parameter.</p> </li> </ul> <p>If a specified trigger is missing, the entire stack operation fails and is rolled back.</p>"""
    monitoring_time_in_minutes: NotRequired[
        "capo_cloudformation.types.monitoring_time_in_minutes.MonitoringTimeInMinutes"
    ]
    """<p>The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.</p> <p>The default is 0 minutes.</p> <p>If you specify a monitoring period but don't specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html">CancelUpdateStack</a>, for example) as necessary.</p> <p>If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RollbackConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rollback_triggers" in value:
        import capo_cloudformation.types.rollback_triggers

        capo_cloudformation.types.rollback_triggers.serialize_query(
            value["rollback_triggers"], pairs, f"{key_prefix}RollbackTriggers"
        )
    if "monitoring_time_in_minutes" in value:
        pairs.append(
            (
                f"{key_prefix}MonitoringTimeInMinutes",
                str(value["monitoring_time_in_minutes"]),
            )
        )


def deserialize_query(el: Element) -> RollbackConfiguration:
    out: RollbackConfiguration = {}  # type: ignore[typeddict-item]
    child_rollback_triggers = el.find("RollbackTriggers")
    if child_rollback_triggers is not None:
        import capo_cloudformation.types.rollback_triggers

        out["rollback_triggers"] = (
            capo_cloudformation.types.rollback_triggers.deserialize_query(
                child_rollback_triggers
            )
        )
    child_monitoring_time_in_minutes = el.find("MonitoringTimeInMinutes")
    if child_monitoring_time_in_minutes is not None:
        out["monitoring_time_in_minutes"] = int(
            child_monitoring_time_in_minutes.text or ""
        )
    return out
