"""Generated from Smithy shape ``com.amazonaws.glue#GrokClassifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.classification
    import capo_glue.types.custom_patterns
    import capo_glue.types.grok_pattern
    import capo_glue.types.name_string
    import capo_glue.types.timestamp
    import capo_glue.types.version_id


class GrokClassifier(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    classification: "capo_glue.types.classification.Classification"
    """<p>An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.</p>"""
    creation_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was registered.</p>"""
    last_updated: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was last updated.</p>"""
    version: "capo_glue.types.version_id.VersionId"
    """<p>The version of this classifier.</p>"""
    grok_pattern: "capo_glue.types.grok_pattern.GrokPattern"
    """<p>The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in <a href="https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html">Writing Custom Classifiers</a>.</p>"""
    custom_patterns: NotRequired["capo_glue.types.custom_patterns.CustomPatterns"]
    """<p>Optional custom grok patterns defined by this classifier. For more information, see custom patterns in <a href="https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html">Writing Custom Classifiers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrokClassifier) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Classification"] = value["classification"]
    if "creation_time" in value:
        import capo_glue.types.timestamp

        out["CreationTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated" in value:
        import capo_glue.types.timestamp

        out["LastUpdated"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    out["Version"] = value.get("version", 0)
    out["GrokPattern"] = value["grok_pattern"]
    if "custom_patterns" in value:
        out["CustomPatterns"] = value["custom_patterns"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GrokClassifier:
    out: GrokClassifier = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GrokClassifier.name required")
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    else:
        raise DeserializationError("GrokClassifier.classification required")
    if data.get("CreationTime") is not None:
        import capo_glue.types.timestamp

        out["creation_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastUpdated") is not None:
        import capo_glue.types.timestamp

        out["last_updated"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastUpdated"]
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if data.get("GrokPattern") is not None:
        out["grok_pattern"] = data["GrokPattern"]
    else:
        raise DeserializationError("GrokClassifier.grok_pattern required")
    if data.get("CustomPatterns") is not None:
        out["custom_patterns"] = data["CustomPatterns"]
    return out
