"""Generated from Smithy shape ``com.amazonaws.shield#AttackDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.attack_id
    import capo_shield.types.attack_properties
    import capo_shield.types.attack_timestamp
    import capo_shield.types.mitigation_list
    import capo_shield.types.resource_arn
    import capo_shield.types.sub_resource_summary_list
    import capo_shield.types.summarized_counter_list


class AttackDetail(TypedDict, closed=True):
    attack_id: NotRequired["capo_shield.types.attack_id.AttackId"]
    """<p>The unique identifier (ID) of the attack.</p>"""
    resource_arn: NotRequired["capo_shield.types.resource_arn.ResourceArn"]
    """<p>The ARN (Amazon Resource Name) of the resource that was attacked.</p>"""
    sub_resources: NotRequired[
        "capo_shield.types.sub_resource_summary_list.SubResourceSummaryList"
    ]
    """<p>If applicable, additional detail about the resource being attacked, for example, IP address or URL.</p>"""
    start_time: NotRequired["capo_shield.types.attack_timestamp.AttackTimestamp"]
    """<p>The time the attack started, in Unix time in seconds. </p>"""
    end_time: NotRequired["capo_shield.types.attack_timestamp.AttackTimestamp"]
    """<p>The time the attack ended, in Unix time in seconds. </p>"""
    attack_counters: NotRequired[
        "capo_shield.types.summarized_counter_list.SummarizedCounterList"
    ]
    """<p>List of counters that describe the attack for the specified time period.</p>"""
    attack_properties: NotRequired[
        "capo_shield.types.attack_properties.AttackProperties"
    ]
    """<p>The array of objects that provide details of the Shield event. </p> <p>For infrastructure layer events (L3 and L4 events), you can view metrics for top contributors in Amazon CloudWatch metrics. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#set-ddos-alarms">Shield metrics and alarms</a> in the <i>WAF Developer Guide</i>. </p>"""
    mitigations: NotRequired["capo_shield.types.mitigation_list.MitigationList"]
    """<p>List of mitigation actions taken for the attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackDetail) -> dict:
    out: dict = {}
    if "attack_id" in value:
        out["AttackId"] = value["attack_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "sub_resources" in value:
        import capo_shield.types.sub_resource_summary_list

        out["SubResources"] = (
            capo_shield.types.sub_resource_summary_list.serialize_aws_json_1_1(
                value["sub_resources"]
            )
        )
    if "start_time" in value:
        import capo_shield.types.attack_timestamp

        out["StartTime"] = capo_shield.types.attack_timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_shield.types.attack_timestamp

        out["EndTime"] = capo_shield.types.attack_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "attack_counters" in value:
        import capo_shield.types.summarized_counter_list

        out["AttackCounters"] = (
            capo_shield.types.summarized_counter_list.serialize_aws_json_1_1(
                value["attack_counters"]
            )
        )
    if "attack_properties" in value:
        import capo_shield.types.attack_properties

        out["AttackProperties"] = (
            capo_shield.types.attack_properties.serialize_aws_json_1_1(
                value["attack_properties"]
            )
        )
    if "mitigations" in value:
        import capo_shield.types.mitigation_list

        out["Mitigations"] = capo_shield.types.mitigation_list.serialize_aws_json_1_1(
            value["mitigations"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackDetail:
    out: AttackDetail = {}  # type: ignore[typeddict-item]
    if data.get("AttackId") is not None:
        out["attack_id"] = data["AttackId"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("SubResources") is not None:
        import capo_shield.types.sub_resource_summary_list

        out["sub_resources"] = (
            capo_shield.types.sub_resource_summary_list.deserialize_aws_json_1_1(
                data["SubResources"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_shield.types.attack_timestamp

        out["start_time"] = capo_shield.types.attack_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_shield.types.attack_timestamp

        out["end_time"] = capo_shield.types.attack_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("AttackCounters") is not None:
        import capo_shield.types.summarized_counter_list

        out["attack_counters"] = (
            capo_shield.types.summarized_counter_list.deserialize_aws_json_1_1(
                data["AttackCounters"]
            )
        )
    if data.get("AttackProperties") is not None:
        import capo_shield.types.attack_properties

        out["attack_properties"] = (
            capo_shield.types.attack_properties.deserialize_aws_json_1_1(
                data["AttackProperties"]
            )
        )
    if data.get("Mitigations") is not None:
        import capo_shield.types.mitigation_list

        out["mitigations"] = capo_shield.types.mitigation_list.deserialize_aws_json_1_1(
            data["Mitigations"]
        )
    return out
