"""Generated from Smithy shape ``com.amazonaws.workspacesweb#InlineRedactionConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.confidence_level
    import capo_workspaces_web.types.global_inline_redaction_urls
    import capo_workspaces_web.types.inline_redaction_patterns


class InlineRedactionConfiguration(TypedDict, closed=True):
    inline_redaction_patterns: (
        "capo_workspaces_web.types.inline_redaction_patterns.InlineRedactionPatterns"
    )
    """<p>The inline redaction patterns to be enabled for the inline redaction configuration.</p>"""
    global_enforced_urls: NotRequired[
        "capo_workspaces_web.types.global_inline_redaction_urls.GlobalInlineRedactionUrls"
    ]
    """<p>The global enforced URL configuration for the inline redaction configuration. This is applied to patterns that do not have a pattern-level enforced URL list.</p>"""
    global_exempt_urls: NotRequired[
        "capo_workspaces_web.types.global_inline_redaction_urls.GlobalInlineRedactionUrls"
    ]
    """<p>The global exempt URL configuration for the inline redaction configuration. This is applied to patterns that do not have a pattern-level exempt URL list.</p>"""
    global_confidence_level: NotRequired[
        "capo_workspaces_web.types.confidence_level.ConfidenceLevel"
    ]
    """<p>The global confidence level for the inline redaction configuration. This indicates the certainty of data type matches in the redaction process. Confidence level 3 means high confidence, and requires a formatted text pattern match in order for content to be redacted. Confidence level 2 means medium confidence, and redaction considers both formatted and unformatted text, and adds keyword associate to the logic. Confidence level 1 means low confidence, and redaction is enforced for both formatted pattern + unformatted pattern without keyword. This is applied to patterns that do not have a pattern-level confidence level. Defaults to confidence level 2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineRedactionConfiguration) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.inline_redaction_patterns

    out["inlineRedactionPatterns"] = (
        capo_workspaces_web.types.inline_redaction_patterns.serialize_json(
            value["inline_redaction_patterns"]
        )
    )
    if "global_enforced_urls" in value:
        import capo_workspaces_web.types.global_inline_redaction_urls

        out["globalEnforcedUrls"] = (
            capo_workspaces_web.types.global_inline_redaction_urls.serialize_json(
                value["global_enforced_urls"]
            )
        )
    if "global_exempt_urls" in value:
        import capo_workspaces_web.types.global_inline_redaction_urls

        out["globalExemptUrls"] = (
            capo_workspaces_web.types.global_inline_redaction_urls.serialize_json(
                value["global_exempt_urls"]
            )
        )
    if "global_confidence_level" in value:
        out["globalConfidenceLevel"] = value["global_confidence_level"]
    return out


def deserialize_json(data: dict) -> InlineRedactionConfiguration:
    out: InlineRedactionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("inlineRedactionPatterns") is not None:
        import capo_workspaces_web.types.inline_redaction_patterns

        out["inline_redaction_patterns"] = (
            capo_workspaces_web.types.inline_redaction_patterns.deserialize_json(
                data["inlineRedactionPatterns"]
            )
        )
    else:
        raise DeserializationError(
            "InlineRedactionConfiguration.inline_redaction_patterns required"
        )
    if data.get("globalEnforcedUrls") is not None:
        import capo_workspaces_web.types.global_inline_redaction_urls

        out["global_enforced_urls"] = (
            capo_workspaces_web.types.global_inline_redaction_urls.deserialize_json(
                data["globalEnforcedUrls"]
            )
        )
    if data.get("globalExemptUrls") is not None:
        import capo_workspaces_web.types.global_inline_redaction_urls

        out["global_exempt_urls"] = (
            capo_workspaces_web.types.global_inline_redaction_urls.deserialize_json(
                data["globalExemptUrls"]
            )
        )
    if data.get("globalConfidenceLevel") is not None:
        out["global_confidence_level"] = data["globalConfidenceLevel"]
    return out


def redact_sensitive(value: InlineRedactionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inline_redaction_patterns" in value:
        import capo_workspaces_web.types.inline_redaction_patterns

        out["inline_redaction_patterns"] = (
            capo_workspaces_web.types.inline_redaction_patterns.redact_sensitive(
                value["inline_redaction_patterns"]
            )
        )
    if "global_enforced_urls" in value:
        import capo_workspaces_web.types.global_inline_redaction_urls

        out["global_enforced_urls"] = (
            capo_workspaces_web.types.global_inline_redaction_urls.redact_sensitive(
                value["global_enforced_urls"]
            )
        )
    if "global_exempt_urls" in value:
        import capo_workspaces_web.types.global_inline_redaction_urls

        out["global_exempt_urls"] = (
            capo_workspaces_web.types.global_inline_redaction_urls.redact_sensitive(
                value["global_exempt_urls"]
            )
        )
    return out
