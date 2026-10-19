"""Generated from Smithy shape ``com.amazonaws.xray#SamplingBoostStatisticsDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.anomaly_count
    import capo_xray.types.rule_name
    import capo_xray.types.sampled_anomaly_count
    import capo_xray.types.service_name
    import capo_xray.types.timestamp
    import capo_xray.types.total_count


class SamplingBoostStatisticsDocument(TypedDict, closed=True):
    rule_name: "capo_xray.types.rule_name.RuleName"
    """<p>The name of the sampling rule.</p>"""
    service_name: "capo_xray.types.service_name.ServiceName"
    """<p>Matches the <code>name</code> that the service uses to identify itself in segments.</p>"""
    timestamp: "capo_xray.types.timestamp.Timestamp"
    """<p>The current time.</p>"""
    anomaly_count: "capo_xray.types.anomaly_count.AnomalyCount"
    """<p>The number of requests with anomaly.</p>"""
    total_count: "capo_xray.types.total_count.TotalCount"
    """<p>The number of requests that associated to the rule.</p>"""
    sampled_anomaly_count: "capo_xray.types.sampled_anomaly_count.SampledAnomalyCount"
    """<p>The number of requests with anomaly recorded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingBoostStatisticsDocument) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    out["ServiceName"] = value["service_name"]
    import capo_xray.types.timestamp

    out["Timestamp"] = capo_xray.types.timestamp.serialize_json(value["timestamp"])
    out["AnomalyCount"] = value.get("anomaly_count", 0)
    out["TotalCount"] = value.get("total_count", 0)
    out["SampledAnomalyCount"] = value.get("sampled_anomaly_count", 0)
    return out


def deserialize_json(data: dict) -> SamplingBoostStatisticsDocument:
    out: SamplingBoostStatisticsDocument = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    else:
        out["rule_name"] = ""
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    else:
        out["service_name"] = ""
    if data.get("Timestamp") is not None:
        import capo_xray.types.timestamp

        out["timestamp"] = capo_xray.types.timestamp.deserialize_json(data["Timestamp"])
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("AnomalyCount") is not None:
        out["anomaly_count"] = data["AnomalyCount"]
    else:
        out["anomaly_count"] = 0
    if data.get("TotalCount") is not None:
        out["total_count"] = data["TotalCount"]
    else:
        out["total_count"] = 0
    if data.get("SampledAnomalyCount") is not None:
        out["sampled_anomaly_count"] = data["SampledAnomalyCount"]
    else:
        out["sampled_anomaly_count"] = 0
    return out
