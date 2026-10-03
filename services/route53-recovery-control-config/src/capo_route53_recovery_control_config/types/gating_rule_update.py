"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#GatingRuleUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__integer
    import capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09


class GatingRuleUpdate(TypedDict, closed=True):
    name: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name for the gating rule. You can use any non-white space character in the name.</p>"""
    safety_rule_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the gating rule.</p>"""
    wait_period_ms: NotRequired[
        "capo_route53_recovery_control_config.types.__integer.__integer"
    ]
    """<p>An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatingRuleUpdate) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "safety_rule_arn" in value:
        out["SafetyRuleArn"] = value["safety_rule_arn"]
    if "wait_period_ms" in value:
        out["WaitPeriodMs"] = value["wait_period_ms"]
    return out


def deserialize_json(data: dict) -> GatingRuleUpdate:
    out: GatingRuleUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SafetyRuleArn") is not None:
        out["safety_rule_arn"] = data["SafetyRuleArn"]
    if data.get("WaitPeriodMs") is not None:
        out["wait_period_ms"] = data["WaitPeriodMs"]
    return out
