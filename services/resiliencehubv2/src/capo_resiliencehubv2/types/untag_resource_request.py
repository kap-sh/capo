"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_resiliencehubv2.types.arn.Arn"
    tag_keys: "capo_resiliencehubv2.types.tag_key_list.TagKeyList"
    """<p>The tag keys to remove from the resource.</p>"""


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
