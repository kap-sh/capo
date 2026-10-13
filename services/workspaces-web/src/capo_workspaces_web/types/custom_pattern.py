"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CustomPattern``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.description_safe
    import capo_workspaces_web.types.pattern_name
    import capo_workspaces_web.types.regex


class CustomPattern(TypedDict, closed=True):
    pattern_name: "capo_workspaces_web.types.pattern_name.PatternName"
    """<p>The pattern name for the custom pattern.</p>"""
    pattern_regex: "capo_workspaces_web.types.regex.Regex"
    """<p>The pattern regex for the customer pattern. The format must follow JavaScript regex format. The pattern must be enclosed between slashes, and can have flags behind the second slash. For example: “/ab+c/gi”.</p>"""
    pattern_description: NotRequired[
        "capo_workspaces_web.types.description_safe.DescriptionSafe"
    ]
    """<p>The pattern description for the customer pattern.</p>"""
    keyword_regex: NotRequired["capo_workspaces_web.types.regex.Regex"]
    """<p>The keyword regex for the customer pattern. After there is a match to the pattern regex, the keyword regex is used to search within the proximity of the match. If there is a keyword match, then the match is confirmed. If no keyword regex is provided, the pattern regex match will automatically be confirmed. The format must follow JavaScript regex format. The pattern must be enclosed between slashes, and can have flags behind the second slash. For example, “/ab+c/gi”</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPattern) -> dict:
    out: dict = {}
    out["patternName"] = value["pattern_name"]
    out["patternRegex"] = value["pattern_regex"]
    if "pattern_description" in value:
        out["patternDescription"] = value["pattern_description"]
    if "keyword_regex" in value:
        out["keywordRegex"] = value["keyword_regex"]
    return out


def deserialize_json(data: dict) -> CustomPattern:
    out: CustomPattern = {}  # type: ignore[typeddict-item]
    if data.get("patternName") is not None:
        out["pattern_name"] = data["patternName"]
    else:
        raise DeserializationError("CustomPattern.pattern_name required")
    if data.get("patternRegex") is not None:
        out["pattern_regex"] = data["patternRegex"]
    else:
        raise DeserializationError("CustomPattern.pattern_regex required")
    if data.get("patternDescription") is not None:
        out["pattern_description"] = data["patternDescription"]
    if data.get("keywordRegex") is not None:
        out["keyword_regex"] = data["keywordRegex"]
    return out


def redact_sensitive(value: CustomPattern) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pattern_name" in value:
        out["pattern_name"] = "*** Sensitive Data Redacted ***"
    if "pattern_regex" in value:
        out["pattern_regex"] = "*** Sensitive Data Redacted ***"
    if "pattern_description" in value:
        out["pattern_description"] = "*** Sensitive Data Redacted ***"
    if "keyword_regex" in value:
        out["keyword_regex"] = "*** Sensitive Data Redacted ***"
    return out
