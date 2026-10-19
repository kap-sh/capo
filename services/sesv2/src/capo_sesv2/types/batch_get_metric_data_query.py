"""Generated from Smithy shape ``com.amazonaws.sesv2#BatchGetMetricDataQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.dimensions
    import capo_sesv2.types.metric
    import capo_sesv2.types.metric_namespace
    import capo_sesv2.types.query_identifier
    import capo_sesv2.types.timestamp


class BatchGetMetricDataQuery(TypedDict, closed=True):
    id: "capo_sesv2.types.query_identifier.QueryIdentifier"
    """<p>The query identifier.</p>"""
    namespace: "capo_sesv2.types.metric_namespace.MetricNamespace"
    """<p>The query namespace - e.g. <code>VDM</code> </p>"""
    metric: "capo_sesv2.types.metric.Metric"
    """<p>The queried metric. This can be one of the following:</p> <ul> <li> <p> <code>SEND</code> – Emails sent eligible for tracking in the VDM dashboard. This excludes emails sent to the mailbox simulator and emails addressed to more than one recipient.</p> </li> <li> <p> <code>COMPLAINT</code> – Complaints received for your account. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient</p> </li> <li> <p> <code>PERMANENT_BOUNCE</code> – Permanent bounces - i.e. feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient.</p> </li> <li> <p> <code>TRANSIENT_BOUNCE</code> – Transient bounces - i.e. feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those for emails addressed to more than one recipient.</p> </li> <li> <p> <code>OPEN</code> – Unique open events for emails including open trackers. Excludes opens for emails addressed to more than one recipient.</p> </li> <li> <p> <code>CLICK</code> – Unique click events for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.</p> </li> <li> <p> <code>DELIVERY</code> – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator and for emails addressed to more than one recipient.</p> </li> <li> <p> <code>DELIVERY_OPEN</code> – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without open trackers.</p> </li> <li> <p> <code>DELIVERY_CLICK</code> – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without click trackers.</p> </li> <li> <p> <code>DELIVERY_COMPLAINT</code> – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails addressed to recipients hosted by ISPs with which Amazon SES does not have a feedback loop agreement.</p> </li> </ul>"""
    dimensions: NotRequired["capo_sesv2.types.dimensions.Dimensions"]
    """<p>An object that contains mapping between <code>MetricDimensionName</code> and <code>MetricDimensionValue</code> to filter metrics by.</p>"""
    start_date: "capo_sesv2.types.timestamp.Timestamp"
    """<p>Represents the start date for the query interval.</p>"""
    end_date: "capo_sesv2.types.timestamp.Timestamp"
    """<p>Represents the end date for the query interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMetricDataQuery) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_sesv2.types.metric_namespace

    out["Namespace"] = capo_sesv2.types.metric_namespace.serialize_json(
        value["namespace"]
    )
    import capo_sesv2.types.metric

    out["Metric"] = capo_sesv2.types.metric.serialize_json(value["metric"])
    if "dimensions" in value:
        import capo_sesv2.types.dimensions

        out["Dimensions"] = capo_sesv2.types.dimensions.serialize_json(
            value["dimensions"]
        )
    import capo_sesv2.types.timestamp

    out["StartDate"] = capo_sesv2.types.timestamp.serialize_json(value["start_date"])
    import capo_sesv2.types.timestamp

    out["EndDate"] = capo_sesv2.types.timestamp.serialize_json(value["end_date"])
    return out


def deserialize_json(data: dict) -> BatchGetMetricDataQuery:
    out: BatchGetMetricDataQuery = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Namespace") is not None:
        import capo_sesv2.types.metric_namespace

        out["namespace"] = capo_sesv2.types.metric_namespace.deserialize_json(
            data["Namespace"]
        )
    else:
        import typing

        out["namespace"] = typing.cast(
            "capo_sesv2.types.metric_namespace.MetricNamespace", ""
        )
    if data.get("Metric") is not None:
        import capo_sesv2.types.metric

        out["metric"] = capo_sesv2.types.metric.deserialize_json(data["Metric"])
    else:
        import typing

        out["metric"] = typing.cast("capo_sesv2.types.metric.Metric", "")
    if data.get("Dimensions") is not None:
        import capo_sesv2.types.dimensions

        out["dimensions"] = capo_sesv2.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if data.get("StartDate") is not None:
        import capo_sesv2.types.timestamp

        out["start_date"] = capo_sesv2.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndDate") is not None:
        import capo_sesv2.types.timestamp

        out["end_date"] = capo_sesv2.types.timestamp.deserialize_json(data["EndDate"])
    else:
        import datetime

        out["end_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
