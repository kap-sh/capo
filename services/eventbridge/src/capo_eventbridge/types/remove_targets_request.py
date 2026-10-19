"""Generated from Smithy shape ``com.amazonaws.eventbridge#RemoveTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.boolean
    import capo_eventbridge.types.event_bus_name_or_arn
    import capo_eventbridge.types.rule_name
    import capo_eventbridge.types.target_id_list


class RemoveTargetsRequest(TypedDict, closed=True):
    rule: "capo_eventbridge.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    event_bus_name: NotRequired[
        "capo_eventbridge.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""
    ids: "capo_eventbridge.types.target_id_list.TargetIdList"
    """<p>The IDs of the targets to remove from the rule.</p>"""
    force: NotRequired["capo_eventbridge.types.boolean.Boolean"]
    """<p>If this is a managed rule, created by an Amazon Web Services service on your behalf, you must specify <code>Force</code> as <code>True</code> to remove targets. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using <code>DescribeRule</code> or <code>ListRules</code> and checking the <code>ManagedBy</code> field of the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTargetsRequest) -> dict:
    out: dict = {}
    out["Rule"] = value["rule"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    import capo_eventbridge.types.target_id_list

    out["Ids"] = capo_eventbridge.types.target_id_list.serialize_aws_json_1_1(
        value["ids"]
    )
    if "force" in value:
        out["Force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTargetsRequest:
    out: RemoveTargetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Rule") is not None:
        out["rule"] = data["Rule"]
    else:
        out["rule"] = ""
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    if data.get("Ids") is not None:
        import capo_eventbridge.types.target_id_list

        out["ids"] = capo_eventbridge.types.target_id_list.deserialize_aws_json_1_1(
            data["Ids"]
        )
    else:
        out["ids"] = []
    if data.get("Force") is not None:
        out["force"] = data["Force"]
    return out
