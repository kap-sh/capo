"""Generated from Smithy shape ``com.amazonaws.workspacesweb#InlineRedactionUrls``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.inline_redaction_url

InlineRedactionUrls: TypeAlias = list[
    "capo_workspaces_web.types.inline_redaction_url.InlineRedactionUrl"
]


# --- restJson1 ser/de ---
def serialize_json(value: InlineRedactionUrls) -> list:
    return list(value)


def deserialize_json(data: list) -> InlineRedactionUrls:
    return [item for item in data if item is not None]


def redact_sensitive(value: InlineRedactionUrls) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
