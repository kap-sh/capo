"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleSetVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.capacity_unit
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.time_window_day
    import capo_wafv2.types.timestamp


class ManagedRuleSetVersion(TypedDict, closed=True):
    associated_rule_group_arn: NotRequired["capo_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the vendor rule group that's used to define the published version of your managed rule group. </p>"""
    capacity: NotRequired["capo_wafv2.types.capacity_unit.CapacityUnit"]
    """<p>The web ACL capacity units (WCUs) required for this rule group.</p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>"""
    forecasted_lifetime: NotRequired["capo_wafv2.types.time_window_day.TimeWindowDay"]
    """<p>The amount of time you expect this version of your managed rule group to last, in days. </p>"""
    publish_timestamp: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The time that you first published this version. </p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z". </p>"""
    last_update_timestamp: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The last time that you updated this version. </p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z". </p>"""
    expiry_timestamp: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The time that this version is set to expire.</p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z". </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleSetVersion) -> dict:
    out: dict = {}
    if "associated_rule_group_arn" in value:
        out["AssociatedRuleGroupArn"] = value["associated_rule_group_arn"]
    if "capacity" in value:
        out["Capacity"] = value["capacity"]
    if "forecasted_lifetime" in value:
        out["ForecastedLifetime"] = value["forecasted_lifetime"]
    if "publish_timestamp" in value:
        import capo_wafv2.types.timestamp

        out["PublishTimestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["publish_timestamp"]
        )
    if "last_update_timestamp" in value:
        import capo_wafv2.types.timestamp

        out["LastUpdateTimestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["last_update_timestamp"]
        )
    if "expiry_timestamp" in value:
        import capo_wafv2.types.timestamp

        out["ExpiryTimestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["expiry_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleSetVersion:
    out: ManagedRuleSetVersion = {}  # type: ignore[typeddict-item]
    if data.get("AssociatedRuleGroupArn") is not None:
        out["associated_rule_group_arn"] = data["AssociatedRuleGroupArn"]
    if data.get("Capacity") is not None:
        out["capacity"] = data["Capacity"]
    if data.get("ForecastedLifetime") is not None:
        out["forecasted_lifetime"] = data["ForecastedLifetime"]
    if data.get("PublishTimestamp") is not None:
        import capo_wafv2.types.timestamp

        out["publish_timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["PublishTimestamp"]
        )
    if data.get("LastUpdateTimestamp") is not None:
        import capo_wafv2.types.timestamp

        out["last_update_timestamp"] = (
            capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    if data.get("ExpiryTimestamp") is not None:
        import capo_wafv2.types.timestamp

        out["expiry_timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["ExpiryTimestamp"]
        )
    return out
