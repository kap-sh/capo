"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_notifications.types.locale_code
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_event_arn
    import capo_notifications.types.organizational_unit_id
    import capo_notifications.types.source


class ListNotificationEventsRequest(TypedDict, closed=True):
    start_time: NotRequired["datetime.datetime"]
    """<p>The earliest time of events to return from this call.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>Latest time of events to return from this call.</p>"""
    locale: NotRequired["capo_notifications.types.locale_code.LocaleCode"]
    """<p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>"""
    source: NotRequired["capo_notifications.types.source.Source"]
    """<p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    include_child_events: NotRequired["bool"]
    """<p>Include aggregated child events in the result.</p>"""
    aggregate_notification_event_arn: NotRequired[
        "capo_notifications.types.notification_event_arn.NotificationEventArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the <code>aggregatedNotificationEventArn</code> to match.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in this call. Defaults to 20.</p>"""
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>"""
    organizational_unit_id: NotRequired[
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The unique identifier of the organizational unit used to filter notification events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNotificationEventsRequest:
    out: ListNotificationEventsRequest = {}  # type: ignore[typeddict-item]
    return out
