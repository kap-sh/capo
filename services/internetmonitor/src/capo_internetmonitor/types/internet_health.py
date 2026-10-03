"""Generated from Smithy shape ``com.amazonaws.internetmonitor#InternetHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.availability_measurement
    import capo_internetmonitor.types.performance_measurement


class InternetHealth(TypedDict, closed=True):
    availability: NotRequired[
        "capo_internetmonitor.types.availability_measurement.AvailabilityMeasurement"
    ]
    """<p>Availability in Internet Monitor represents the estimated percentage of traffic that is not seeing an availability drop. For example, an availability score of 99% for an end user and service location pair is equivalent to 1% of the traffic experiencing an availability drop for that pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores">How Internet Monitor calculates performance and availability scores</a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    performance: NotRequired[
        "capo_internetmonitor.types.performance_measurement.PerformanceMeasurement"
    ]
    """<p>Performance in Internet Monitor represents the estimated percentage of traffic that is not seeing a performance drop. For example, a performance score of 99% for an end user and service location pair is equivalent to 1% of the traffic experiencing a performance drop for that pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores">How Internet Monitor calculates performance and availability scores</a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternetHealth) -> dict:
    out: dict = {}
    if "availability" in value:
        import capo_internetmonitor.types.availability_measurement

        out["Availability"] = (
            capo_internetmonitor.types.availability_measurement.serialize_json(
                value["availability"]
            )
        )
    if "performance" in value:
        import capo_internetmonitor.types.performance_measurement

        out["Performance"] = (
            capo_internetmonitor.types.performance_measurement.serialize_json(
                value["performance"]
            )
        )
    return out


def deserialize_json(data: dict) -> InternetHealth:
    out: InternetHealth = {}  # type: ignore[typeddict-item]
    if data.get("Availability") is not None:
        import capo_internetmonitor.types.availability_measurement

        out["availability"] = (
            capo_internetmonitor.types.availability_measurement.deserialize_json(
                data["Availability"]
            )
        )
    if data.get("Performance") is not None:
        import capo_internetmonitor.types.performance_measurement

        out["performance"] = (
            capo_internetmonitor.types.performance_measurement.deserialize_json(
                data["Performance"]
            )
        )
    return out
