"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GlobalInlineRedactionUrls``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.inline_redaction_url

GlobalInlineRedactionUrls: TypeAlias = list[
    "capo_workspaces_web.types.inline_redaction_url.InlineRedactionUrl"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalInlineRedactionUrls) -> list:
    return list(value)


def deserialize_json(data: list) -> GlobalInlineRedactionUrls:
    return [item for item in data if item is not None]


def redact_sensitive(value: GlobalInlineRedactionUrls) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
