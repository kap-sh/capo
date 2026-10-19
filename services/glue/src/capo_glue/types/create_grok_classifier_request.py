"""Generated from Smithy shape ``com.amazonaws.glue#CreateGrokClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.classification
    import capo_glue.types.custom_patterns
    import capo_glue.types.grok_pattern
    import capo_glue.types.name_string


class CreateGrokClassifierRequest(TypedDict, closed=True):
    classification: "capo_glue.types.classification.Classification"
    """<p>An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.</p>"""
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the new classifier.</p>"""
    grok_pattern: "capo_glue.types.grok_pattern.GrokPattern"
    """<p>The grok pattern used by this classifier.</p>"""
    custom_patterns: NotRequired["capo_glue.types.custom_patterns.CustomPatterns"]
    """<p>Optional custom grok patterns used by this classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGrokClassifierRequest) -> dict:
    out: dict = {}
    out["Classification"] = value["classification"]
    out["Name"] = value["name"]
    out["GrokPattern"] = value["grok_pattern"]
    if "custom_patterns" in value:
        out["CustomPatterns"] = value["custom_patterns"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGrokClassifierRequest:
    out: CreateGrokClassifierRequest = {}  # type: ignore[typeddict-item]
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    else:
        out["classification"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("GrokPattern") is not None:
        out["grok_pattern"] = data["GrokPattern"]
    else:
        out["grok_pattern"] = ""
    if data.get("CustomPatterns") is not None:
        out["custom_patterns"] = data["CustomPatterns"]
    return out
