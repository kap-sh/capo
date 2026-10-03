"""Generated from Smithy shape ``com.amazonaws.connect#RuleSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.action_summaries
    import capo_connect.types.arn
    import capo_connect.types.pre_evaluation_filters
    import capo_connect.types.rule_capability_tiers
    import capo_connect.types.rule_id
    import capo_connect.types.rule_name
    import capo_connect.types.rule_publish_status
    import capo_connect.types.rule_trigger_event_source
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class RuleSearchSummary(TypedDict, closed=True):
    name: "capo_connect.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    rule_id: "capo_connect.types.rule_id.RuleId"
    """<p>A unique identifier for the rule.</p>"""
    rule_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    trigger_event_source: (
        "capo_connect.types.rule_trigger_event_source.RuleTriggerEventSource"
    )
    """<p>The event source to trigger the rule.</p>"""
    action_summaries: "capo_connect.types.action_summaries.ActionSummaries"
    """<p>A list of <code>ActionTypes</code> associated with a rule.</p>"""
    rule_capability_tiers: NotRequired[
        "capo_connect.types.rule_capability_tiers.RuleCapabilityTiers"
    ]
    """<p>The list of capability tiers associated with the rule. Used for categorizing rules by capability (for example, <code>GenerativeAI</code>).</p>"""
    publish_status: "capo_connect.types.rule_publish_status.RulePublishStatus"
    """<p>The publish status of the rule.</p>"""
    pre_evaluation_filters: NotRequired[
        "capo_connect.types.pre_evaluation_filters.PreEvaluationFilters"
    ]
    """<p>The pre-evaluation filters for the rule, that restrict the rule to be applied to only certain resources based on the resource's attributes, such as tags assigned to a contact. The pre-evaluation filters are applied even before rule conditions are evaluated and are used to enforce tag-based-access-control while applying rules.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the rule was created.</p>"""
    last_updated_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the rule was last updated.</p>"""
    last_updated_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the rule.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleSearchSummary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RuleId"] = value["rule_id"]
    out["RuleArn"] = value["rule_arn"]
    import capo_connect.types.rule_trigger_event_source

    out["TriggerEventSource"] = (
        capo_connect.types.rule_trigger_event_source.serialize_json(
            value["trigger_event_source"]
        )
    )
    import capo_connect.types.action_summaries

    out["ActionSummaries"] = capo_connect.types.action_summaries.serialize_json(
        value["action_summaries"]
    )
    if "rule_capability_tiers" in value:
        import capo_connect.types.rule_capability_tiers

        out["RuleCapabilityTiers"] = (
            capo_connect.types.rule_capability_tiers.serialize_json(
                value["rule_capability_tiers"]
            )
        )
    import capo_connect.types.rule_publish_status

    out["PublishStatus"] = capo_connect.types.rule_publish_status.serialize_json(
        value["publish_status"]
    )
    if "pre_evaluation_filters" in value:
        import capo_connect.types.pre_evaluation_filters

        out["PreEvaluationFilters"] = (
            capo_connect.types.pre_evaluation_filters.serialize_json(
                value["pre_evaluation_filters"]
            )
        )
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_connect.types.timestamp

    out["LastUpdatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    out["LastUpdatedBy"] = value["last_updated_by"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RuleSearchSummary:
    out: RuleSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RuleSearchSummary.name required")
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("RuleSearchSummary.rule_id required")
    if data.get("RuleArn") is not None:
        out["rule_arn"] = data["RuleArn"]
    else:
        raise DeserializationError("RuleSearchSummary.rule_arn required")
    if data.get("TriggerEventSource") is not None:
        import capo_connect.types.rule_trigger_event_source

        out["trigger_event_source"] = (
            capo_connect.types.rule_trigger_event_source.deserialize_json(
                data["TriggerEventSource"]
            )
        )
    else:
        raise DeserializationError("RuleSearchSummary.trigger_event_source required")
    if data.get("ActionSummaries") is not None:
        import capo_connect.types.action_summaries

        out["action_summaries"] = capo_connect.types.action_summaries.deserialize_json(
            data["ActionSummaries"]
        )
    else:
        raise DeserializationError("RuleSearchSummary.action_summaries required")
    if data.get("RuleCapabilityTiers") is not None:
        import capo_connect.types.rule_capability_tiers

        out["rule_capability_tiers"] = (
            capo_connect.types.rule_capability_tiers.deserialize_json(
                data["RuleCapabilityTiers"]
            )
        )
    if data.get("PublishStatus") is not None:
        import capo_connect.types.rule_publish_status

        out["publish_status"] = capo_connect.types.rule_publish_status.deserialize_json(
            data["PublishStatus"]
        )
    else:
        raise DeserializationError("RuleSearchSummary.publish_status required")
    if data.get("PreEvaluationFilters") is not None:
        import capo_connect.types.pre_evaluation_filters

        out["pre_evaluation_filters"] = (
            capo_connect.types.pre_evaluation_filters.deserialize_json(
                data["PreEvaluationFilters"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("RuleSearchSummary.created_time required")
    if data.get("LastUpdatedTime") is not None:
        import capo_connect.types.timestamp

        out["last_updated_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        raise DeserializationError("RuleSearchSummary.last_updated_time required")
    if data.get("LastUpdatedBy") is not None:
        out["last_updated_by"] = data["LastUpdatedBy"]
    else:
        raise DeserializationError("RuleSearchSummary.last_updated_by required")
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
