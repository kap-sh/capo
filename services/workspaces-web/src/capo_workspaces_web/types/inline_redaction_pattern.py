"""Generated from Smithy shape ``com.amazonaws.workspacesweb#InlineRedactionPattern``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.built_in_pattern_id
    import capo_workspaces_web.types.confidence_level
    import capo_workspaces_web.types.custom_pattern
    import capo_workspaces_web.types.inline_redaction_urls
    import capo_workspaces_web.types.redaction_place_holder


class InlineRedactionPattern(TypedDict, closed=True):
    built_in_pattern_id: NotRequired[
        "capo_workspaces_web.types.built_in_pattern_id.BuiltInPatternId"
    ]
    """<p>The built-in pattern from the list of preconfigured patterns. Either a customPattern or builtInPatternId is required.</p>"""
    custom_pattern: NotRequired[
        "capo_workspaces_web.types.custom_pattern.CustomPattern"
    ]
    """<p>&gt;The configuration for a custom pattern. Either a customPattern or builtInPatternId is required.</p>"""
    redaction_place_holder: (
        "capo_workspaces_web.types.redaction_place_holder.RedactionPlaceHolder"
    )
    """<p>The redaction placeholder that will replace the redacted text in session for the inline redaction pattern.</p>"""
    enforced_urls: NotRequired[
        "capo_workspaces_web.types.inline_redaction_urls.InlineRedactionUrls"
    ]
    """<p>The enforced URL configuration for the inline redaction pattern. This will override the global enforced URL configuration.</p>"""
    exempt_urls: NotRequired[
        "capo_workspaces_web.types.inline_redaction_urls.InlineRedactionUrls"
    ]
    """<p>The exempt URL configuration for the inline redaction pattern. This will override the global exempt URL configuration for the inline redaction pattern.</p>"""
    confidence_level: NotRequired[
        "capo_workspaces_web.types.confidence_level.ConfidenceLevel"
    ]
    """<p>The confidence level for inline redaction pattern. This indicates the certainty of data type matches in the redaction process. Confidence level 3 means high confidence, and requires a formatted text pattern match in order for content to be redacted. Confidence level 2 means medium confidence, and redaction considers both formatted and unformatted text, and adds keyword associate to the logic. Confidence level 1 means low confidence, and redaction is enforced for both formatted pattern + unformatted pattern without keyword. This overrides the global confidence level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineRedactionPattern) -> dict:
    out: dict = {}
    if "built_in_pattern_id" in value:
        out["builtInPatternId"] = value["built_in_pattern_id"]
    if "custom_pattern" in value:
        import capo_workspaces_web.types.custom_pattern

        out["customPattern"] = capo_workspaces_web.types.custom_pattern.serialize_json(
            value["custom_pattern"]
        )
    import capo_workspaces_web.types.redaction_place_holder

    out["redactionPlaceHolder"] = (
        capo_workspaces_web.types.redaction_place_holder.serialize_json(
            value["redaction_place_holder"]
        )
    )
    if "enforced_urls" in value:
        import capo_workspaces_web.types.inline_redaction_urls

        out["enforcedUrls"] = (
            capo_workspaces_web.types.inline_redaction_urls.serialize_json(
                value["enforced_urls"]
            )
        )
    if "exempt_urls" in value:
        import capo_workspaces_web.types.inline_redaction_urls

        out["exemptUrls"] = (
            capo_workspaces_web.types.inline_redaction_urls.serialize_json(
                value["exempt_urls"]
            )
        )
    if "confidence_level" in value:
        out["confidenceLevel"] = value["confidence_level"]
    return out


def deserialize_json(data: dict) -> InlineRedactionPattern:
    out: InlineRedactionPattern = {}  # type: ignore[typeddict-item]
    if data.get("builtInPatternId") is not None:
        out["built_in_pattern_id"] = data["builtInPatternId"]
    if data.get("customPattern") is not None:
        import capo_workspaces_web.types.custom_pattern

        out["custom_pattern"] = (
            capo_workspaces_web.types.custom_pattern.deserialize_json(
                data["customPattern"]
            )
        )
    if data.get("redactionPlaceHolder") is not None:
        import capo_workspaces_web.types.redaction_place_holder

        out["redaction_place_holder"] = (
            capo_workspaces_web.types.redaction_place_holder.deserialize_json(
                data["redactionPlaceHolder"]
            )
        )
    else:
        raise DeserializationError(
            "InlineRedactionPattern.redaction_place_holder required"
        )
    if data.get("enforcedUrls") is not None:
        import capo_workspaces_web.types.inline_redaction_urls

        out["enforced_urls"] = (
            capo_workspaces_web.types.inline_redaction_urls.deserialize_json(
                data["enforcedUrls"]
            )
        )
    if data.get("exemptUrls") is not None:
        import capo_workspaces_web.types.inline_redaction_urls

        out["exempt_urls"] = (
            capo_workspaces_web.types.inline_redaction_urls.deserialize_json(
                data["exemptUrls"]
            )
        )
    if data.get("confidenceLevel") is not None:
        out["confidence_level"] = data["confidenceLevel"]
    return out


def redact_sensitive(value: InlineRedactionPattern) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "built_in_pattern_id" in value:
        out["built_in_pattern_id"] = "*** Sensitive Data Redacted ***"
    if "custom_pattern" in value:
        import capo_workspaces_web.types.custom_pattern

        out["custom_pattern"] = (
            capo_workspaces_web.types.custom_pattern.redact_sensitive(
                value["custom_pattern"]
            )
        )
    if "redaction_place_holder" in value:
        import capo_workspaces_web.types.redaction_place_holder

        out["redaction_place_holder"] = (
            capo_workspaces_web.types.redaction_place_holder.redact_sensitive(
                value["redaction_place_holder"]
            )
        )
    if "enforced_urls" in value:
        import capo_workspaces_web.types.inline_redaction_urls

        out["enforced_urls"] = (
            capo_workspaces_web.types.inline_redaction_urls.redact_sensitive(
                value["enforced_urls"]
            )
        )
    if "exempt_urls" in value:
        import capo_workspaces_web.types.inline_redaction_urls

        out["exempt_urls"] = (
            capo_workspaces_web.types.inline_redaction_urls.redact_sensitive(
                value["exempt_urls"]
            )
        )
    return out
