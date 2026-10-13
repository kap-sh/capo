"""Generated from Smithy shape ``com.amazonaws.workspacesweb#TagKeyList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.tag_key

TagKeyList: TypeAlias = list["capo_workspaces_web.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyList:
    return [item for item in data if item is not None]


def redact_sensitive(value: TagKeyList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
