"""Generated from Smithy shape ``com.amazonaws.personalize#AutoTrainingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.scheduling_expression


class AutoTrainingConfig(TypedDict, closed=True):
    scheduling_expression: NotRequired[
        "capo_personalize.types.scheduling_expression.SchedulingExpression"
    ]
    """<p>Specifies how often to automatically train new solution versions. Specify a rate expression in rate(<i>value</i> <i>unit</i>) format. For value, specify a number between 1 and 30. For unit, specify <code>day</code> or <code>days</code>. For example, to automatically create a new solution version every 5 days, specify <code>rate(5 days)</code>. The default is every 7 days.</p> <p>For more information about auto training, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html">Creating and configuring a solution</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoTrainingConfig) -> dict:
    out: dict = {}
    if "scheduling_expression" in value:
        out["schedulingExpression"] = value["scheduling_expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoTrainingConfig:
    out: AutoTrainingConfig = {}  # type: ignore[typeddict-item]
    if data.get("schedulingExpression") is not None:
        out["scheduling_expression"] = data["schedulingExpression"]
    return out
