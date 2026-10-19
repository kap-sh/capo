"""Generated from Smithy shape ``com.amazonaws.wafv2#SourceStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.filter_string
    import capo_wafv2.types.monetization_amount_value
    import capo_wafv2.types.percentage_value
    import capo_wafv2.types.request_count
    import capo_wafv2.types.verified_status


class SourceStatistics(TypedDict, closed=True):
    source_name: "capo_wafv2.types.filter_string.FilterString"
    """<p>The name of the AI bot.</p>"""
    percentage: "capo_wafv2.types.percentage_value.PercentageValue"
    """<p>The percentage of total revenue from this source.</p>"""
    amount: "capo_wafv2.types.monetization_amount_value.MonetizationAmountValue"
    """<p>The total revenue amount from this source in the specified currency.</p>"""
    request_count: "capo_wafv2.types.request_count.RequestCount"
    """<p>The number of monetized requests from this source.</p>"""
    source_category: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The category of this AI bot source.</p>"""
    intent: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The declared intent of the AI bot (for example, summarize, index, or train).</p>"""
    organization: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The organization associated with the AI bot.</p>"""
    verified: "capo_wafv2.types.verified_status.VerifiedStatus"
    """<p>Indicates whether the AI bot's identity was verified — for example, through a cryptographically signed request (Web Bot Auth) or another published verification method. This value is meaningful only when GroupBy is NAME, where each result represents a single, identifiable bot. For all other GroupBy values (CATEGORY, INTENT, ORGANIZATION, or WEBACL), a result aggregates multiple bots that may have different verification states, so Verified is always returned as false and should be ignored. Type and required-ness are unchanged (Boolean, optional).</p>"""
    group_by_value: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The value for the group-by dimension, when grouping is applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceStatistics) -> dict:
    out: dict = {}
    out["SourceName"] = value["source_name"]
    out["Percentage"] = (
        "NaN"
        if value.get("percentage", 0) != value.get("percentage", 0)
        else "Infinity"
        if value.get("percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("percentage", 0) == float("-inf")
        else value.get("percentage", 0)
    )
    out["Amount"] = value["amount"]
    out["RequestCount"] = value.get("request_count", 0)
    if "source_category" in value:
        out["SourceCategory"] = value["source_category"]
    if "intent" in value:
        out["Intent"] = value["intent"]
    if "organization" in value:
        out["Organization"] = value["organization"]
    out["Verified"] = value.get("verified", False)
    if "group_by_value" in value:
        out["GroupByValue"] = value["group_by_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceStatistics:
    out: SourceStatistics = {}  # type: ignore[typeddict-item]
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    else:
        out["source_name"] = ""
    if data.get("Percentage") is not None:
        out["percentage"] = float(data["Percentage"])
    else:
        out["percentage"] = 0
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    else:
        out["amount"] = ""
    if data.get("RequestCount") is not None:
        out["request_count"] = data["RequestCount"]
    else:
        out["request_count"] = 0
    if data.get("SourceCategory") is not None:
        out["source_category"] = data["SourceCategory"]
    if data.get("Intent") is not None:
        out["intent"] = data["Intent"]
    if data.get("Organization") is not None:
        out["organization"] = data["Organization"]
    if data.get("Verified") is not None:
        out["verified"] = data["Verified"]
    else:
        out["verified"] = False
    if data.get("GroupByValue") is not None:
        out["group_by_value"] = data["GroupByValue"]
    return out
