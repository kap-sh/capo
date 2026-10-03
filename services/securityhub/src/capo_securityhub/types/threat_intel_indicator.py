"""Generated from Smithy shape ``com.amazonaws.securityhub#ThreatIntelIndicator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.threat_intel_indicator_category
    import capo_securityhub.types.threat_intel_indicator_type


class ThreatIntelIndicator(TypedDict, closed=True):
    type: NotRequired[
        "capo_securityhub.types.threat_intel_indicator_type.ThreatIntelIndicatorType"
    ]
    """<p>The type of threat intelligence indicator.</p>"""
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of a threat intelligence indicator.</p> <p>Length Constraints: Minimum of 1 length. Maximum of 512 length.</p>"""
    category: NotRequired[
        "capo_securityhub.types.threat_intel_indicator_category.ThreatIntelIndicatorCategory"
    ]
    """<p>The category of a threat intelligence indicator.</p>"""
    last_observed_at: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the most recent instance of a threat intelligence indicator was observed.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    source: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source of the threat intelligence indicator.</p> <p>Length Constraints: Minimum of 1 length. Maximum of 64 length.</p>"""
    source_url: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The URL to the page or site where you can get more information about the threat intelligence indicator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelIndicator) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_securityhub.types.threat_intel_indicator_type

        out["Type"] = capo_securityhub.types.threat_intel_indicator_type.serialize_json(
            value["type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    if "category" in value:
        import capo_securityhub.types.threat_intel_indicator_category

        out["Category"] = (
            capo_securityhub.types.threat_intel_indicator_category.serialize_json(
                value["category"]
            )
        )
    if "last_observed_at" in value:
        out["LastObservedAt"] = value["last_observed_at"]
    if "source" in value:
        out["Source"] = value["source"]
    if "source_url" in value:
        out["SourceUrl"] = value["source_url"]
    return out


def deserialize_json(data: dict) -> ThreatIntelIndicator:
    out: ThreatIntelIndicator = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_securityhub.types.threat_intel_indicator_type

        out["type"] = (
            capo_securityhub.types.threat_intel_indicator_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Category") is not None:
        import capo_securityhub.types.threat_intel_indicator_category

        out["category"] = (
            capo_securityhub.types.threat_intel_indicator_category.deserialize_json(
                data["Category"]
            )
        )
    if data.get("LastObservedAt") is not None:
        out["last_observed_at"] = data["LastObservedAt"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("SourceUrl") is not None:
        out["source_url"] = data["SourceUrl"]
    return out
