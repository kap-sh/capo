"""Generated from Smithy shape ``com.amazonaws.internetmonitor#PerformanceMeasurement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.round_trip_time


class PerformanceMeasurement(TypedDict, closed=True):
    experience_score: NotRequired["float"]
    """<p>Experience scores, or health scores, are calculated for different geographic and network provider combinations (that is, different granularities) and also totaled into global scores. If you view performance or availability scores without filtering for any specific geography or service provider, Amazon CloudWatch Internet Monitor provides global health scores.</p> <p>The Amazon CloudWatch Internet Monitor chapter in the CloudWatch User Guide includes detailed information about how Internet Monitor calculates health scores, including performance and availability scores, and when it creates and resolves health events. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores">How Amazon Web Services calculates performance and availability scores</a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    percent_of_total_traffic_impacted: NotRequired["float"]
    """<p>The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the Amazon Web Services location using this client network.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMHealthEventStartStop">When Amazon Web Services creates and resolves health events</a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    percent_of_client_location_impacted: NotRequired["float"]
    """<p>How much performance impact was caused by a health event at a client location. For performance, this is the percentage of how much latency increased during the event compared to typical performance for traffic, from this client location to an Amazon Web Services location, using a specific client network. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMHealthEventStartStop">When Amazon Web Services creates and resolves health events</a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    round_trip_time: NotRequired[
        "capo_internetmonitor.types.round_trip_time.RoundTripTime"
    ]
    """<p>This is the percentage of how much round-trip time increased during the event compared to typical round-trip time for your application for traffic. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMHealthEventStartStop">When Amazon Web Services creates and resolves health events</a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMeasurement) -> dict:
    out: dict = {}
    if "experience_score" in value:
        out["ExperienceScore"] = (
            "NaN"
            if value["experience_score"] != value["experience_score"]
            else "Infinity"
            if value["experience_score"] == float("inf")
            else "-Infinity"
            if value["experience_score"] == float("-inf")
            else value["experience_score"]
        )
    if "percent_of_total_traffic_impacted" in value:
        out["PercentOfTotalTrafficImpacted"] = (
            "NaN"
            if value["percent_of_total_traffic_impacted"]
            != value["percent_of_total_traffic_impacted"]
            else "Infinity"
            if value["percent_of_total_traffic_impacted"] == float("inf")
            else "-Infinity"
            if value["percent_of_total_traffic_impacted"] == float("-inf")
            else value["percent_of_total_traffic_impacted"]
        )
    if "percent_of_client_location_impacted" in value:
        out["PercentOfClientLocationImpacted"] = (
            "NaN"
            if value["percent_of_client_location_impacted"]
            != value["percent_of_client_location_impacted"]
            else "Infinity"
            if value["percent_of_client_location_impacted"] == float("inf")
            else "-Infinity"
            if value["percent_of_client_location_impacted"] == float("-inf")
            else value["percent_of_client_location_impacted"]
        )
    if "round_trip_time" in value:
        import capo_internetmonitor.types.round_trip_time

        out["RoundTripTime"] = (
            capo_internetmonitor.types.round_trip_time.serialize_json(
                value["round_trip_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerformanceMeasurement:
    out: PerformanceMeasurement = {}  # type: ignore[typeddict-item]
    if data.get("ExperienceScore") is not None:
        out["experience_score"] = float(data["ExperienceScore"])
    if data.get("PercentOfTotalTrafficImpacted") is not None:
        out["percent_of_total_traffic_impacted"] = float(
            data["PercentOfTotalTrafficImpacted"]
        )
    if data.get("PercentOfClientLocationImpacted") is not None:
        out["percent_of_client_location_impacted"] = float(
            data["PercentOfClientLocationImpacted"]
        )
    if data.get("RoundTripTime") is not None:
        import capo_internetmonitor.types.round_trip_time

        out["round_trip_time"] = (
            capo_internetmonitor.types.round_trip_time.deserialize_json(
                data["RoundTripTime"]
            )
        )
    return out
