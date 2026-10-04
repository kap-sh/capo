"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationTrait``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class RemediationTrait(TypedDict, closed=True):
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The trait type.</p>"""
    title: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The trait title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationTrait) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "title" in value:
        out["Title"] = value["title"]
    return out


def deserialize_json(data: dict) -> RemediationTrait:
    out: RemediationTrait = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    return out
