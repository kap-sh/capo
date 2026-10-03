"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Schedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.auto_disable_policy
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.pipeline_execution_start_condition
    import capo_imagebuilder.types.timezone


class Schedule(TypedDict, closed=True):
    schedule_expression: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The expression determines how often EC2 Image Builder evaluates your <code>pipelineExecutionStartCondition</code>. You can specify a cron expression, or a rate expression such as <code>rate(1 day)</code>.</p> <p>For information on how to format a cron expression in Image Builder, see <a href="https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-cron.html">Use cron expressions in EC2 Image Builder</a>.</p>"""
    timezone: NotRequired["capo_imagebuilder.types.timezone.Timezone"]
    """<p>The timezone that applies to the scheduling expression. Specify a value in <a href="https://www.joda.org/joda-time/timezones.html">IANA timezone format</a>, for example <code>Etc/UTC</code> or <code>America/Los_Angeles</code>. If not specified, this defaults to UTC.</p>"""
    pipeline_execution_start_condition: NotRequired[
        "capo_imagebuilder.types.pipeline_execution_start_condition.PipelineExecutionStartCondition"
    ]
    """<p>The start condition configures when the pipeline should trigger a new image build, as follows. If no value is set Image Builder defaults to <code>EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE</code>.</p> <ul> <li> <p> <code>EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE</code> (default) – When you use semantic version filters on the base image or components in your image recipe, EC2 Image Builder builds a new image only when there are new versions of the base image or components in your recipe that match the filter.</p> <note> <p>For semantic version syntax, see <a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html">CreateComponent</a>.</p> </note> </li> <li> <p> <code>EXPRESSION_MATCH_ONLY</code> – This condition builds a new image every time the CRON expression matches the current time.</p> </li> </ul> <note> <p>If the recipe references its base image through an Amazon Web Services Systems Manager Parameter Store parameter, a change in the parameter's value also counts as an available dependency update.</p> </note>"""
    auto_disable_policy: NotRequired[
        "capo_imagebuilder.types.auto_disable_policy.AutoDisablePolicy"
    ]
    """<p>The policy that configures when Image Builder should automatically disable a pipeline that is failing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["scheduleExpression"] = value["schedule_expression"]
    if "timezone" in value:
        out["timezone"] = value["timezone"]
    if "pipeline_execution_start_condition" in value:
        import capo_imagebuilder.types.pipeline_execution_start_condition

        out["pipelineExecutionStartCondition"] = (
            capo_imagebuilder.types.pipeline_execution_start_condition.serialize_json(
                value["pipeline_execution_start_condition"]
            )
        )
    if "auto_disable_policy" in value:
        import capo_imagebuilder.types.auto_disable_policy

        out["autoDisablePolicy"] = (
            capo_imagebuilder.types.auto_disable_policy.serialize_json(
                value["auto_disable_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("scheduleExpression") is not None:
        out["schedule_expression"] = data["scheduleExpression"]
    if data.get("timezone") is not None:
        out["timezone"] = data["timezone"]
    if data.get("pipelineExecutionStartCondition") is not None:
        import capo_imagebuilder.types.pipeline_execution_start_condition

        out["pipeline_execution_start_condition"] = (
            capo_imagebuilder.types.pipeline_execution_start_condition.deserialize_json(
                data["pipelineExecutionStartCondition"]
            )
        )
    if data.get("autoDisablePolicy") is not None:
        import capo_imagebuilder.types.auto_disable_policy

        out["auto_disable_policy"] = (
            capo_imagebuilder.types.auto_disable_policy.deserialize_json(
                data["autoDisablePolicy"]
            )
        )
    return out
