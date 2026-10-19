"""Generated from Smithy shape ``com.amazonaws.wafv2#ActionCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.action_value


class ActionCondition(TypedDict, closed=True):
    action: "capo_wafv2.types.action_value.ActionValue"
    """<p>The action setting that a log record must contain in order to meet the condition. This is the action that WAF applied to the web request. </p> <p>For rule groups, this is either the configured rule action setting, or if you've applied a rule action override to the rule, it's the override action. The value <code>EXCLUDED_AS_COUNT</code> matches on excluded rules and also on rules that have a rule action override of Count. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionCondition) -> dict:
    out: dict = {}
    import capo_wafv2.types.action_value

    out["Action"] = capo_wafv2.types.action_value.serialize_aws_json_1_1(
        value["action"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionCondition:
    out: ActionCondition = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_wafv2.types.action_value

        out["action"] = capo_wafv2.types.action_value.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast("capo_wafv2.types.action_value.ActionValue", "")
    return out
