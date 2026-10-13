"""Generated from Smithy shape ``com.amazonaws.workspacesweb#InlineRedactionPatterns``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.inline_redaction_pattern

InlineRedactionPatterns: TypeAlias = list[
    "capo_workspaces_web.types.inline_redaction_pattern.InlineRedactionPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: InlineRedactionPatterns) -> list:
    import capo_workspaces_web.types.inline_redaction_pattern

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.inline_redaction_pattern.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InlineRedactionPatterns:
    import capo_workspaces_web.types.inline_redaction_pattern

    out: InlineRedactionPatterns = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_web.types.inline_redaction_pattern.deserialize_json(item)
        )
    return out


def redact_sensitive(value: InlineRedactionPatterns) -> list[Any]:
    import capo_workspaces_web.types.inline_redaction_pattern

    return [
        capo_workspaces_web.types.inline_redaction_pattern.redact_sensitive(item)
        for item in value
    ]
