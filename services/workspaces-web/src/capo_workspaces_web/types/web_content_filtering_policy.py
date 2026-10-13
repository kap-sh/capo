"""Generated from Smithy shape ``com.amazonaws.workspacesweb#WebContentFilteringPolicy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.blocked_categories
    import capo_workspaces_web.types.url_pattern_list


class WebContentFilteringPolicy(TypedDict, closed=True):
    blocked_categories: NotRequired[
        "capo_workspaces_web.types.blocked_categories.BlockedCategories"
    ]
    """<p>Categories of websites that are blocked on the end user’s browsers.</p>"""
    allowed_urls: NotRequired[
        "capo_workspaces_web.types.url_pattern_list.UrlPatternList"
    ]
    """<p>URLs and domains that are always accessible to end users.</p>"""
    blocked_urls: NotRequired[
        "capo_workspaces_web.types.url_pattern_list.UrlPatternList"
    ]
    """<p>URLs and domains that end users cannot access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebContentFilteringPolicy) -> dict:
    out: dict = {}
    if "blocked_categories" in value:
        import capo_workspaces_web.types.blocked_categories

        out["blockedCategories"] = (
            capo_workspaces_web.types.blocked_categories.serialize_json(
                value["blocked_categories"]
            )
        )
    if "allowed_urls" in value:
        import capo_workspaces_web.types.url_pattern_list

        out["allowedUrls"] = capo_workspaces_web.types.url_pattern_list.serialize_json(
            value["allowed_urls"]
        )
    if "blocked_urls" in value:
        import capo_workspaces_web.types.url_pattern_list

        out["blockedUrls"] = capo_workspaces_web.types.url_pattern_list.serialize_json(
            value["blocked_urls"]
        )
    return out


def deserialize_json(data: dict) -> WebContentFilteringPolicy:
    out: WebContentFilteringPolicy = {}  # type: ignore[typeddict-item]
    if data.get("blockedCategories") is not None:
        import capo_workspaces_web.types.blocked_categories

        out["blocked_categories"] = (
            capo_workspaces_web.types.blocked_categories.deserialize_json(
                data["blockedCategories"]
            )
        )
    if data.get("allowedUrls") is not None:
        import capo_workspaces_web.types.url_pattern_list

        out["allowed_urls"] = (
            capo_workspaces_web.types.url_pattern_list.deserialize_json(
                data["allowedUrls"]
            )
        )
    if data.get("blockedUrls") is not None:
        import capo_workspaces_web.types.url_pattern_list

        out["blocked_urls"] = (
            capo_workspaces_web.types.url_pattern_list.deserialize_json(
                data["blockedUrls"]
            )
        )
    return out


def redact_sensitive(value: WebContentFilteringPolicy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "allowed_urls" in value:
        import capo_workspaces_web.types.url_pattern_list

        out["allowed_urls"] = (
            capo_workspaces_web.types.url_pattern_list.redact_sensitive(
                value["allowed_urls"]
            )
        )
    if "blocked_urls" in value:
        import capo_workspaces_web.types.url_pattern_list

        out["blocked_urls"] = (
            capo_workspaces_web.types.url_pattern_list.redact_sensitive(
                value["blocked_urls"]
            )
        )
    return out
