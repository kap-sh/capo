"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashDvbMetricsReporting``."""

from typing_extensions import NotRequired, TypedDict


class DashDvbMetricsReporting(TypedDict, closed=True):
    reporting_url: "str"
    """<p>The URL where playback devices send error reports.</p>"""
    probability: NotRequired["int"]
    """<p>The number of playback devices per 1000 that will send error reports to the reporting URL. This represents the probability that a playback device will be a reporting player for this session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashDvbMetricsReporting) -> dict:
    out: dict = {}
    out["ReportingUrl"] = value["reporting_url"]
    if "probability" in value:
        out["Probability"] = value["probability"]
    return out


def deserialize_json(data: dict) -> DashDvbMetricsReporting:
    out: DashDvbMetricsReporting = {}  # type: ignore[typeddict-item]
    if data.get("ReportingUrl") is not None:
        out["reporting_url"] = data["ReportingUrl"]
    else:
        out["reporting_url"] = ""
    if data.get("Probability") is not None:
        out["probability"] = data["Probability"]
    return out
