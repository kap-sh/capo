"""Generated from Smithy shape ``com.amazonaws.glue#UpdateGrokClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.classification
    import capo_glue.types.custom_patterns
    import capo_glue.types.grok_pattern
    import capo_glue.types.name_string


class UpdateGrokClassifierRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the <code>GrokClassifier</code>.</p>"""
    classification: NotRequired["capo_glue.types.classification.Classification"]
    """<p>An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.</p>"""
    grok_pattern: NotRequired["capo_glue.types.grok_pattern.GrokPattern"]
    """<p>The grok pattern used by this classifier.</p>"""
    custom_patterns: NotRequired["capo_glue.types.custom_patterns.CustomPatterns"]
    """<p>Optional custom grok patterns used by this classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGrokClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "grok_pattern" in value:
        out["GrokPattern"] = value["grok_pattern"]
    if "custom_patterns" in value:
        out["CustomPatterns"] = value["custom_patterns"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGrokClassifierRequest:
    out: UpdateGrokClassifierRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    if data.get("GrokPattern") is not None:
        out["grok_pattern"] = data["GrokPattern"]
    if data.get("CustomPatterns") is not None:
        out["custom_patterns"] = data["CustomPatterns"]
    return out
