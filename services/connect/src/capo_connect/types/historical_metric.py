"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.historical_metric_name
    import capo_connect.types.statistic
    import capo_connect.types.threshold
    import capo_connect.types.unit


class HistoricalMetric(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.historical_metric_name.HistoricalMetricName"]
    """<p>The name of the metric. Following is a list of each supported metric mapped to the UI name, linked to a detailed description in the <i>Connect Customer Administrator Guide</i>. </p> <dl> <dt>ABANDON_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-abandon-time">Average queue abandon time</a> </p> </dd> <dt>AFTER_CONTACT_WORK_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#after-contact-work-time">After contact work time</a> </p> </dd> <dt>API_CONTACTS_HANDLED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#api-contacts-handled">API contacts handled</a> </p> </dd> <dt>AVG_HOLD_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-hold-time">Average customer hold time</a> </p> </dd> <dt>CALLBACK_CONTACTS_HANDLED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#callback-contacts-handled">Callback contacts handled</a> </p> </dd> <dt>CONTACTS_ABANDONED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-abandoned">Contacts abandoned</a> </p> </dd> <dt>CONTACTS_AGENT_HUNG_UP_FIRST</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-agent-hung-up-first">Contacts agent hung up first</a> </p> </dd> <dt>CONTACTS_CONSULTED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-consulted">Contacts consulted</a> </p> </dd> <dt>CONTACTS_HANDLED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled">Contacts handled</a> </p> </dd> <dt>CONTACTS_HANDLED_INCOMING</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-incoming">Contacts handled incoming</a> </p> </dd> <dt>CONTACTS_HANDLED_OUTBOUND</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-outbound">Contacts handled outbound</a> </p> </dd> <dt>CONTACTS_HOLD_ABANDONS</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-disconnect">Contacts hold disconnect</a> </p> </dd> <dt>CONTACTS_MISSED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-response">AGENT_NON_RESPONSE</a> </p> </dd> <dt>CONTACTS_QUEUED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-queued">Contacts queued</a> </p> </dd> <dt>CONTACTS_TRANSFERRED_IN</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-in">Contacts transferred in</a> </p> </dd> <dt>CONTACTS_TRANSFERRED_IN_FROM_QUEUE</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue">Contacts transferred out queue</a> </p> </dd> <dt>CONTACTS_TRANSFERRED_OUT</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out">Contacts transferred out</a> </p> </dd> <dt>CONTACTS_TRANSFERRED_OUT_FROM_QUEUE</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue">Contacts transferred out queue</a> </p> </dd> <dt>HANDLE_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-handle-time">Average handle time</a> </p> </dd> <dt>INTERACTION_AND_HOLD_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interaction-and-customer-hold-time">Average agent interaction and customer hold time</a> </p> </dd> <dt>INTERACTION_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#aaverage-agent-interaction-time">Average agent interaction time</a> </p> </dd> <dt>OCCUPANCY</dt> <dd> <p>Unit: PERCENT</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#occupancy">Occupancy</a> </p> </dd> <dt>QUEUE_ANSWER_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html##average-queue-answer-time">Average queue answer time</a> </p> </dd> <dt>QUEUED_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: MAX</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#minimum-flow-time">Minimum flow time</a> </p> </dd> <dt>SERVICE_LEVEL</dt> <dd> <p>You can include up to 20 SERVICE_LEVEL metrics in a request.</p> <p>Unit: PERCENT</p> <p>Statistic: AVG</p> <p>Threshold: For <code>ThresholdValue</code>, enter any whole number from 1 to 604800 (inclusive), in seconds. For <code>Comparison</code>, you must enter <code>LT</code> (for "Less than"). </p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#service-level">Service level X</a> </p> </dd> </dl>"""
    threshold: NotRequired["capo_connect.types.threshold.Threshold"]
    """<p>The threshold for the metric, used with service level metrics.</p>"""
    statistic: NotRequired["capo_connect.types.statistic.Statistic"]
    """<p>The statistic for the metric.</p>"""
    unit: NotRequired["capo_connect.types.unit.Unit"]
    """<p>The unit for the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_connect.types.historical_metric_name

        out["Name"] = capo_connect.types.historical_metric_name.serialize_json(
            value["name"]
        )
    if "threshold" in value:
        import capo_connect.types.threshold

        out["Threshold"] = capo_connect.types.threshold.serialize_json(
            value["threshold"]
        )
    if "statistic" in value:
        import capo_connect.types.statistic

        out["Statistic"] = capo_connect.types.statistic.serialize_json(
            value["statistic"]
        )
    if "unit" in value:
        import capo_connect.types.unit

        out["Unit"] = capo_connect.types.unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> HistoricalMetric:
    out: HistoricalMetric = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_connect.types.historical_metric_name

        out["name"] = capo_connect.types.historical_metric_name.deserialize_json(
            data["Name"]
        )
    if data.get("Threshold") is not None:
        import capo_connect.types.threshold

        out["threshold"] = capo_connect.types.threshold.deserialize_json(
            data["Threshold"]
        )
    if data.get("Statistic") is not None:
        import capo_connect.types.statistic

        out["statistic"] = capo_connect.types.statistic.deserialize_json(
            data["Statistic"]
        )
    if data.get("Unit") is not None:
        import capo_connect.types.unit

        out["unit"] = capo_connect.types.unit.deserialize_json(data["Unit"])
    return out
