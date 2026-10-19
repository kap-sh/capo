"""Generated from Smithy shape ``com.amazonaws.connect#RuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.action_summaries
    import capo_connect.types.arn
    import capo_connect.types.event_source_name
    import capo_connect.types.rule_capability_tiers
    import capo_connect.types.rule_id
    import capo_connect.types.rule_name
    import capo_connect.types.rule_publish_status
    import capo_connect.types.timestamp


class RuleSummary(TypedDict, closed=True):
    name: "capo_connect.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    rule_id: "capo_connect.types.rule_id.RuleId"
    """<p>A unique identifier for the rule.</p>"""
    rule_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    event_source_name: "capo_connect.types.event_source_name.EventSourceName"
    """<p>The name of the event source.</p>"""
    publish_status: "capo_connect.types.rule_publish_status.RulePublishStatus"
    """<p>The publish status of the rule.</p>"""
    rule_capability_tiers: NotRequired[
        "capo_connect.types.rule_capability_tiers.RuleCapabilityTiers"
    ]
    """<p>The list of capability tiers associated with the rule. Used for categorizing rules by capability (for example, <code>GenerativeAI</code>).</p>"""
    action_summaries: "capo_connect.types.action_summaries.ActionSummaries"
    """<p>A list of ActionTypes associated with a rule. </p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the rule was created. </p>"""
    last_updated_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RuleId"] = value["rule_id"]
    out["RuleArn"] = value["rule_arn"]
    import capo_connect.types.event_source_name

    out["EventSourceName"] = capo_connect.types.event_source_name.serialize_json(
        value["event_source_name"]
    )
    import capo_connect.types.rule_publish_status

    out["PublishStatus"] = capo_connect.types.rule_publish_status.serialize_json(
        value["publish_status"]
    )
    if "rule_capability_tiers" in value:
        import capo_connect.types.rule_capability_tiers

        out["RuleCapabilityTiers"] = (
            capo_connect.types.rule_capability_tiers.serialize_json(
                value["rule_capability_tiers"]
            )
        )
    import capo_connect.types.action_summaries

    out["ActionSummaries"] = capo_connect.types.action_summaries.serialize_json(
        value["action_summaries"]
    )
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_connect.types.timestamp

    out["LastUpdatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    return out


def deserialize_json(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        out["rule_id"] = ""
    if data.get("RuleArn") is not None:
        out["rule_arn"] = data["RuleArn"]
    else:
        out["rule_arn"] = ""
    if data.get("EventSourceName") is not None:
        import capo_connect.types.event_source_name

        out["event_source_name"] = (
            capo_connect.types.event_source_name.deserialize_json(
                data["EventSourceName"]
            )
        )
    else:
        import typing

        out["event_source_name"] = typing.cast(
            "capo_connect.types.event_source_name.EventSourceName", ""
        )
    if data.get("PublishStatus") is not None:
        import capo_connect.types.rule_publish_status

        out["publish_status"] = capo_connect.types.rule_publish_status.deserialize_json(
            data["PublishStatus"]
        )
    else:
        import typing

        out["publish_status"] = typing.cast(
            "capo_connect.types.rule_publish_status.RulePublishStatus", ""
        )
    if data.get("RuleCapabilityTiers") is not None:
        import capo_connect.types.rule_capability_tiers

        out["rule_capability_tiers"] = (
            capo_connect.types.rule_capability_tiers.deserialize_json(
                data["RuleCapabilityTiers"]
            )
        )
    if data.get("ActionSummaries") is not None:
        import capo_connect.types.action_summaries

        out["action_summaries"] = capo_connect.types.action_summaries.deserialize_json(
            data["ActionSummaries"]
        )
    else:
        out["action_summaries"] = []
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_connect.types.timestamp

        out["last_updated_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
