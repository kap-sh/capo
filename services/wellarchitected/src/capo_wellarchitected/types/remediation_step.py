"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RemediationStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.sensitive_string


class RemediationStep(TypedDict, closed=True):
    title: NotRequired["capo_wellarchitected.types.sensitive_string.SensitiveString"]
    """<p>An optional short label for the step.</p>"""
    content: "capo_wellarchitected.types.sensitive_string.SensitiveString"
    """<p>The content describing the step, which can include code examples and verification checklists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationStep) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> RemediationStep:
    out: RemediationStep = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    return out


def redact_sensitive(value: RemediationStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
