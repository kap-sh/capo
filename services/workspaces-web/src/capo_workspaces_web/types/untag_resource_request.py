"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "capo_workspaces_web.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


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
        import capo_workspaces_web.types.tag_key_list

        out["tag_keys"] = capo_workspaces_web.types.tag_key_list.redact_sensitive(
            value["tag_keys"]
        )
    return out
