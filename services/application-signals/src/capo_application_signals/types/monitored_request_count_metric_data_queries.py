"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MonitoredRequestCountMetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.metric_data_queries


class _MonitoredRequestCountMetricDataQueries_GoodCountMetric(TypedDict, closed=True):
    GoodCountMetric: (
        "capo_application_signals.types.metric_data_queries.MetricDataQueries"
    )


class _MonitoredRequestCountMetricDataQueries_BadCountMetric(TypedDict, closed=True):
    BadCountMetric: (
        "capo_application_signals.types.metric_data_queries.MetricDataQueries"
    )


MonitoredRequestCountMetricDataQueries: TypeAlias = (
    _MonitoredRequestCountMetricDataQueries_GoodCountMetric
    | _MonitoredRequestCountMetricDataQueries_BadCountMetric
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MonitoredRequestCountMetricDataQueries) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MonitoredRequestCountMetricDataQueries: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "GoodCountMetric" in value:
        import capo_application_signals.types.metric_data_queries

        return {
            "GoodCountMetric": capo_application_signals.types.metric_data_queries.serialize_json(
                value["GoodCountMetric"]
            )
        }
    elif "BadCountMetric" in value:
        import capo_application_signals.types.metric_data_queries

        return {
            "BadCountMetric": capo_application_signals.types.metric_data_queries.serialize_json(
                value["BadCountMetric"]
            )
        }
    else:
        raise SerializationError(
            "MonitoredRequestCountMetricDataQueries: no variant present"
        )


def deserialize_json(data: dict) -> MonitoredRequestCountMetricDataQueries:
    if data.get("GoodCountMetric") is not None:
        import capo_application_signals.types.metric_data_queries

        return {
            "GoodCountMetric": capo_application_signals.types.metric_data_queries.deserialize_json(
                data["GoodCountMetric"]
            )
        }
    elif data.get("BadCountMetric") is not None:
        import capo_application_signals.types.metric_data_queries

        return {
            "BadCountMetric": capo_application_signals.types.metric_data_queries.deserialize_json(
                data["BadCountMetric"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MonitoredRequestCountMetricDataQueries: no recognized variant key"
        )
