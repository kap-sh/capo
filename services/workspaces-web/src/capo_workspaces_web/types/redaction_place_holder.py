"""Generated from Smithy shape ``com.amazonaws.workspacesweb#RedactionPlaceHolder``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.redaction_place_holder_text
    import capo_workspaces_web.types.redaction_place_holder_type


class RedactionPlaceHolder(TypedDict, closed=True):
    redaction_place_holder_type: (
        "capo_workspaces_web.types.redaction_place_holder_type.RedactionPlaceHolderType"
    )
    """<p>The redaction placeholder type that will replace the redacted text in session.</p>"""
    redaction_place_holder_text: NotRequired[
        "capo_workspaces_web.types.redaction_place_holder_text.RedactionPlaceHolderText"
    ]
    """<p>The redaction placeholder text that will replace the redacted text in session for the custom text redaction placeholder type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedactionPlaceHolder) -> dict:
    out: dict = {}
    out["redactionPlaceHolderType"] = value["redaction_place_holder_type"]
    if "redaction_place_holder_text" in value:
        out["redactionPlaceHolderText"] = value["redaction_place_holder_text"]
    return out


def deserialize_json(data: dict) -> RedactionPlaceHolder:
    out: RedactionPlaceHolder = {}  # type: ignore[typeddict-item]
    if data.get("redactionPlaceHolderType") is not None:
        out["redaction_place_holder_type"] = data["redactionPlaceHolderType"]
    else:
        raise DeserializationError(
            "RedactionPlaceHolder.redaction_place_holder_type required"
        )
    if data.get("redactionPlaceHolderText") is not None:
        out["redaction_place_holder_text"] = data["redactionPlaceHolderText"]
    return out


def redact_sensitive(value: RedactionPlaceHolder) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "redaction_place_holder_text" in value:
        out["redaction_place_holder_text"] = "*** Sensitive Data Redacted ***"
    return out
