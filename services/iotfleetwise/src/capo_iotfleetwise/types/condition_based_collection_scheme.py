"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ConditionBasedCollectionScheme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.event_expression
    import capo_iotfleetwise.types.language_version
    import capo_iotfleetwise.types.trigger_mode
    import capo_iotfleetwise.types.uint32


class ConditionBasedCollectionScheme(TypedDict, closed=True):
    expression: "capo_iotfleetwise.types.event_expression.eventExpression"
    """<p>The logical expression used to recognize what data to collect. For example, <code>$variable.`Vehicle.OutsideAirTemperature` &gt;= 105.0</code>.</p>"""
    minimum_trigger_interval_ms: NotRequired["capo_iotfleetwise.types.uint32.uint32"]
    """<p>The minimum duration of time between two triggering events to collect data, in milliseconds.</p> <note> <p>If a signal changes often, you might want to collect data at a slower rate.</p> </note>"""
    trigger_mode: NotRequired["capo_iotfleetwise.types.trigger_mode.TriggerMode"]
    """<p>Whether to collect data for all triggering events (<code>ALWAYS</code>). Specify (<code>RISING_EDGE</code>), or specify only when the condition first evaluates to false. For example, triggering on "AirbagDeployed"; Users aren't interested on triggering when the airbag is already exploded; they only care about the change from not deployed =&gt; deployed.</p>"""
    condition_language_version: NotRequired[
        "capo_iotfleetwise.types.language_version.languageVersion"
    ]
    """<p>Specifies the version of the conditional expression language.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionBasedCollectionScheme) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    if "minimum_trigger_interval_ms" in value:
        out["minimumTriggerIntervalMs"] = value["minimum_trigger_interval_ms"]
    if "trigger_mode" in value:
        import capo_iotfleetwise.types.trigger_mode

        out["triggerMode"] = (
            capo_iotfleetwise.types.trigger_mode.serialize_aws_json_1_0(
                value["trigger_mode"]
            )
        )
    if "condition_language_version" in value:
        out["conditionLanguageVersion"] = value["condition_language_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionBasedCollectionScheme:
    out: ConditionBasedCollectionScheme = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("ConditionBasedCollectionScheme.expression required")
    if data.get("minimumTriggerIntervalMs") is not None:
        out["minimum_trigger_interval_ms"] = data["minimumTriggerIntervalMs"]
    if data.get("triggerMode") is not None:
        import capo_iotfleetwise.types.trigger_mode

        out["trigger_mode"] = (
            capo_iotfleetwise.types.trigger_mode.deserialize_aws_json_1_0(
                data["triggerMode"]
            )
        )
    if data.get("conditionLanguageVersion") is not None:
        out["condition_language_version"] = data["conditionLanguageVersion"]
    return out
