"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UrlPatternList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.url_pattern

UrlPatternList: TypeAlias = list["capo_workspaces_web.types.url_pattern.UrlPattern"]


# --- restJson1 ser/de ---
def serialize_json(value: UrlPatternList) -> list:
    return list(value)


def deserialize_json(data: list) -> UrlPatternList:
    return [item for item in data if item is not None]


def redact_sensitive(value: UrlPatternList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
