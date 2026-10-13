"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ConditionBasedSignalFetchConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.fetch_config_event_expression
    import capo_iotfleetwise.types.trigger_mode


class ConditionBasedSignalFetchConfig(TypedDict, closed=True):
    condition_expression: "capo_iotfleetwise.types.fetch_config_event_expression.fetchConfigEventExpression"
    """<p>The condition that must be satisfied to trigger a signal fetch.</p>"""
    trigger_mode: "capo_iotfleetwise.types.trigger_mode.TriggerMode"
    """<p>Indicates the mode in which the signal fetch is triggered.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionBasedSignalFetchConfig) -> dict:
    out: dict = {}
    out["conditionExpression"] = value["condition_expression"]
    import capo_iotfleetwise.types.trigger_mode

    out["triggerMode"] = capo_iotfleetwise.types.trigger_mode.serialize_aws_json_1_0(
        value["trigger_mode"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionBasedSignalFetchConfig:
    out: ConditionBasedSignalFetchConfig = {}  # type: ignore[typeddict-item]
    if data.get("conditionExpression") is not None:
        out["condition_expression"] = data["conditionExpression"]
    else:
        raise DeserializationError(
            "ConditionBasedSignalFetchConfig.condition_expression required"
        )
    if data.get("triggerMode") is not None:
        import capo_iotfleetwise.types.trigger_mode

        out["trigger_mode"] = (
            capo_iotfleetwise.types.trigger_mode.deserialize_aws_json_1_0(
                data["triggerMode"]
            )
        )
    else:
        raise DeserializationError(
            "ConditionBasedSignalFetchConfig.trigger_mode required"
        )
    return out


def redact_sensitive(value: ConditionBasedSignalFetchConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "condition_expression" in value:
        out["condition_expression"] = "*** Sensitive Data Redacted ***"
    return out
