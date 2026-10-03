"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.analyzer_configuration
    import capo_accessanalyzer.types.analyzer_name
    import capo_accessanalyzer.types.analyzer_status
    import capo_accessanalyzer.types.status_reason
    import capo_accessanalyzer.types.tags_map
    import capo_accessanalyzer.types.timestamp
    import capo_accessanalyzer.types.type


class AnalyzerSummary(TypedDict, closed=True):
    arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The ARN of the analyzer.</p>"""
    name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer.</p>"""
    type: "capo_accessanalyzer.types.type.Type"
    """<p>The type represents the zone of trust or scope for the analyzer.</p>"""
    created_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>A timestamp for the time at which the analyzer was created.</p>"""
    last_resource_analyzed: NotRequired["str"]
    """<p>The resource that was most recently analyzed by the analyzer.</p>"""
    last_resource_analyzed_at: NotRequired[
        "capo_accessanalyzer.types.timestamp.Timestamp"
    ]
    """<p>The time at which the most recently analyzed resource was analyzed.</p>"""
    tags: NotRequired["capo_accessanalyzer.types.tags_map.TagsMap"]
    """<p>An array of key-value pairs applied to the analyzer. The key-value pairs consist of the set of Unicode letters, digits, whitespace, <code>_</code>, <code>.</code>, <code>/</code>, <code>=</code>, <code>+</code>, and <code>-</code>.</p> <p>The tag key is a value that is 1 to 128 characters in length and cannot be prefixed with <code>aws:</code>.</p> <p>The tag value is a value that is 0 to 256 characters in length.</p>"""
    status: "capo_accessanalyzer.types.analyzer_status.AnalyzerStatus"
    """<p>The status of the analyzer. An <code>Active</code> analyzer successfully monitors supported resources and generates new findings. The analyzer is <code>Disabled</code> when a user action, such as removing trusted access for Identity and Access Management Access Analyzer from Organizations, causes the analyzer to stop generating new findings. The status is <code>Creating</code> when the analyzer creation is in progress and <code>Failed</code> when the analyzer creation has failed. </p>"""
    status_reason: NotRequired["capo_accessanalyzer.types.status_reason.StatusReason"]
    """<p>The <code>statusReason</code> provides more details about the current status of the analyzer. For example, if the creation for the analyzer fails, a <code>Failed</code> status is returned. For an analyzer with organization as the type, this failure can be due to an issue with creating the service-linked roles required in the member accounts of the Amazon Web Services organization.</p>"""
    configuration: NotRequired[
        "capo_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
    ]
    """<p>Specifies if the analyzer is an external access, unused access, or internal access analyzer. The <a href="https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzer.html">GetAnalyzer</a> action includes this property in its response if a configuration is specified, while the <a href="https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzers.html">ListAnalyzers</a> action omits it.</p>"""
    managed_by: NotRequired["str"]
    """<p>The service principal that manages this analyzer (for example, <code>securityhubv2.amazonaws.com</code>). This field is only present for service-linked analyzers and is not included for customer-managed analyzers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzerSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    import capo_accessanalyzer.types.timestamp

    out["createdAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    if "last_resource_analyzed" in value:
        out["lastResourceAnalyzed"] = value["last_resource_analyzed"]
    if "last_resource_analyzed_at" in value:
        import capo_accessanalyzer.types.timestamp

        out["lastResourceAnalyzedAt"] = (
            capo_accessanalyzer.types.timestamp.serialize_json(
                value["last_resource_analyzed_at"]
            )
        )
    if "tags" in value:
        import capo_accessanalyzer.types.tags_map

        out["tags"] = capo_accessanalyzer.types.tags_map.serialize_json(value["tags"])
    out["status"] = value["status"]
    if "status_reason" in value:
        import capo_accessanalyzer.types.status_reason

        out["statusReason"] = capo_accessanalyzer.types.status_reason.serialize_json(
            value["status_reason"]
        )
    if "configuration" in value:
        import capo_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            capo_accessanalyzer.types.analyzer_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "managed_by" in value:
        out["managedBy"] = value["managed_by"]
    return out


def deserialize_json(data: dict) -> AnalyzerSummary:
    out: AnalyzerSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AnalyzerSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AnalyzerSummary.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AnalyzerSummary.type required")
    if data.get("createdAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["created_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AnalyzerSummary.created_at required")
    if data.get("lastResourceAnalyzed") is not None:
        out["last_resource_analyzed"] = data["lastResourceAnalyzed"]
    if data.get("lastResourceAnalyzedAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["last_resource_analyzed_at"] = (
            capo_accessanalyzer.types.timestamp.deserialize_json(
                data["lastResourceAnalyzedAt"]
            )
        )
    if data.get("tags") is not None:
        import capo_accessanalyzer.types.tags_map

        out["tags"] = capo_accessanalyzer.types.tags_map.deserialize_json(data["tags"])
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AnalyzerSummary.status required")
    if data.get("statusReason") is not None:
        import capo_accessanalyzer.types.status_reason

        out["status_reason"] = capo_accessanalyzer.types.status_reason.deserialize_json(
            data["statusReason"]
        )
    if data.get("configuration") is not None:
        import capo_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            capo_accessanalyzer.types.analyzer_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if data.get("managedBy") is not None:
        out["managed_by"] = data["managedBy"]
    return out
