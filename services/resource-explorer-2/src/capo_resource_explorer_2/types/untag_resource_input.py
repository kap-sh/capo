"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#UntagResourceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.string_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the view or index that you want to remove tags from.</p>"""
    tag_keys: "capo_resource_explorer_2.types.string_list.StringList"
    """<p>A list of the keys for the tags that you want to remove from the specified view or index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: UntagResourceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_keys" in value:
        out["tag_keys"] = "*** Sensitive Data Redacted ***"
    return out
