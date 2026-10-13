"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_chime_sdk_voice.types.arn.Arn"
    """<p>The resource ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListTagsForResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_arn" in value:
        out["resource_arn"] = "*** Sensitive Data Redacted ***"
    return out
