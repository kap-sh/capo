"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#GatingRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__integer
    import capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09
    import capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import capo_route53_recovery_control_config.types.__string_min12_max12_pattern_d12
    import capo_route53_recovery_control_config.types.rule_config
    import capo_route53_recovery_control_config.types.status


class GatingRule(TypedDict, closed=True):
    control_panel_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the control panel.</p>"""
    gating_controls: NotRequired[
        "capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.__listOf__stringMin1Max256PatternAZaZ09"
    ]
    """<p>An array of gating routing control Amazon Resource Names (ARNs). For a simple "on/off" switch, specify the ARN for one routing control. The gating routing controls are evaluated by the rule configuration that you specify to determine if the target routing control states can be changed.</p>"""
    name: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name for the gating rule. You can use any non-white space character in the name.</p>"""
    rule_config: NotRequired[
        "capo_route53_recovery_control_config.types.rule_config.RuleConfig"
    ]
    """<p>The criteria that you set for gating routing controls that designate how many of the routing control states must be ON to allow you to update target routing control states.</p>"""
    safety_rule_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the gating rule.</p>"""
    status: NotRequired["capo_route53_recovery_control_config.types.status.Status"]
    """<p>The deployment status of a gating rule. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</p>"""
    target_controls: NotRequired[
        "capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.__listOf__stringMin1Max256PatternAZaZ09"
    ]
    """<p>An array of target routing control Amazon Resource Names (ARNs) for which the states can only be updated if the rule configuration that you specify evaluates to true for the gating routing control. As a simple example, if you have a single gating control, it acts as an overall "on/off" switch for a set of target routing controls. You can use this to manually override automated failover, for example.</p>"""
    wait_period_ms: NotRequired[
        "capo_route53_recovery_control_config.types.__integer.__integer"
    ]
    """<p>An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.</p>"""
    owner: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min12_max12_pattern_d12.__stringMin12Max12PatternD12"
    ]
    """<p>The Amazon Web Services account ID of the gating rule owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatingRule) -> dict:
    out: dict = {}
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "gating_controls" in value:
        import capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["GatingControls"] = (
            capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.serialize_json(
                value["gating_controls"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "rule_config" in value:
        import capo_route53_recovery_control_config.types.rule_config

        out["RuleConfig"] = (
            capo_route53_recovery_control_config.types.rule_config.serialize_json(
                value["rule_config"]
            )
        )
    if "safety_rule_arn" in value:
        out["SafetyRuleArn"] = value["safety_rule_arn"]
    if "status" in value:
        import capo_route53_recovery_control_config.types.status

        out["Status"] = (
            capo_route53_recovery_control_config.types.status.serialize_json(
                value["status"]
            )
        )
    if "target_controls" in value:
        import capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["TargetControls"] = (
            capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.serialize_json(
                value["target_controls"]
            )
        )
    if "wait_period_ms" in value:
        out["WaitPeriodMs"] = value["wait_period_ms"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_json(data: dict) -> GatingRule:
    out: GatingRule = {}  # type: ignore[typeddict-item]
    if data.get("ControlPanelArn") is not None:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if data.get("GatingControls") is not None:
        import capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["gating_controls"] = (
            capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.deserialize_json(
                data["GatingControls"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RuleConfig") is not None:
        import capo_route53_recovery_control_config.types.rule_config

        out["rule_config"] = (
            capo_route53_recovery_control_config.types.rule_config.deserialize_json(
                data["RuleConfig"]
            )
        )
    if data.get("SafetyRuleArn") is not None:
        out["safety_rule_arn"] = data["SafetyRuleArn"]
    if data.get("Status") is not None:
        import capo_route53_recovery_control_config.types.status

        out["status"] = (
            capo_route53_recovery_control_config.types.status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("TargetControls") is not None:
        import capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["target_controls"] = (
            capo_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.deserialize_json(
                data["TargetControls"]
            )
        )
    if data.get("WaitPeriodMs") is not None:
        out["wait_period_ms"] = data["WaitPeriodMs"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    return out
