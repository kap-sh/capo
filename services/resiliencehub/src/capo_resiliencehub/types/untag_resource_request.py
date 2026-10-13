"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the resource. </p>"""
    tag_keys: "capo_resiliencehub.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags you want to remove.</p>"""


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
