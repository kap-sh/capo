"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.channel_arn
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_configuration_status
    import capo_notifications.types.notification_configuration_subtype
    import capo_notifications.types.source


class ListNotificationConfigurationsRequest(TypedDict, closed=True):
    event_rule_source: NotRequired["capo_notifications.types.source.Source"]
    """<p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    channel_arn: NotRequired["capo_notifications.types.channel_arn.ChannelArn"]
    """<p>The Amazon Resource Name (ARN) of the Channel to match.</p>"""
    status: NotRequired[
        "capo_notifications.types.notification_configuration_status.NotificationConfigurationStatus"
    ]
    """<p>The <code>NotificationConfiguration</code> status to match.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ACTIVE</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>ACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>PARTIALLY_ACTIVE</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> <li> <p>Any call can be run.</p> </li> </ul> </li> <li> <p> <code>INACTIVE</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>INACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>DELETING</code> </p> <ul> <li> <p>This <code>NotificationConfiguration</code> is being deleted.</p> </li> <li> <p>Only <code>GET</code> and <code>LIST</code> calls can be run.</p> </li> </ul> </li> </ul> </li> </ul>"""
    subtype: NotRequired[
        "capo_notifications.types.notification_configuration_subtype.NotificationConfigurationSubtype"
    ]
    """<p>The subtype used to filter the notification configurations in the request.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in this call. Defaults to 20.</p>"""
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNotificationConfigurationsRequest:
    out: ListNotificationConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
