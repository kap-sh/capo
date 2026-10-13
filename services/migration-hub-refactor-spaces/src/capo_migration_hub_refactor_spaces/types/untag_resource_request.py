"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.string
    import capo_migration_hub_refactor_spaces.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_migration_hub_refactor_spaces.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource. </p>"""
    tag_keys: "capo_migration_hub_refactor_spaces.types.tag_keys.TagKeys"
    """<p>The list of keys of the tags to be removed from the resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: UntagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_keys" in value:
        out["tag_keys"] = "*** Sensitive Data Redacted ***"
    return out
