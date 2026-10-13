"""Generated from Smithy shape ``com.amazonaws.drs#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_drs.types.arn.ARN"
    """<p>ARN of the resource for which tags are to be removed.</p>"""
    tag_keys: "capo_drs.types.tag_keys.TagKeys"
    """<p>Array of tags to be removed.</p>"""


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
