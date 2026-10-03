"""Generated from Smithy shape ``com.amazonaws.notifications#UpdateEventRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.event_rule_arn
    import capo_notifications.types.event_rule_event_pattern
    import capo_notifications.types.regions


class UpdateEventRuleRequest(TypedDict, closed=True):
    arn: "capo_notifications.types.event_rule_arn.EventRuleArn"
    """<p>The Amazon Resource Name (ARN) to use to update the <code>EventRule</code>.</p>"""
    event_pattern: NotRequired[
        "capo_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
    ]
    """<p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>"""
    regions: NotRequired["capo_notifications.types.regions.Regions"]
    """<p>A list of Amazon Web Services Regions that sends events to this <code>EventRule</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventRuleRequest) -> dict:
    out: dict = {}
    if "event_pattern" in value:
        out["eventPattern"] = value["event_pattern"]
    if "regions" in value:
        import capo_notifications.types.regions

        out["regions"] = capo_notifications.types.regions.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEventRuleRequest:
    out: UpdateEventRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventPattern") is not None:
        out["event_pattern"] = data["eventPattern"]
    if data.get("regions") is not None:
        import capo_notifications.types.regions

        out["regions"] = capo_notifications.types.regions.deserialize_json(
            data["regions"]
        )
    return out
