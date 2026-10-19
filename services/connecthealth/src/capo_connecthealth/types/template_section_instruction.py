"""Generated from Smithy shape ``com.amazonaws.connecthealth#TemplateSectionInstruction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.sensitive_markdown_string
    import capo_connecthealth.types.sensitive_section_header_string


class TemplateSectionInstruction(TypedDict, closed=True):
    section_header: "capo_connecthealth.types.sensitive_section_header_string.SensitiveSectionHeaderString"
    """<p>The header for this section of the template</p>"""
    section_instruction: (
        "capo_connecthealth.types.sensitive_markdown_string.SensitiveMarkdownString"
    )
    """<p>The instruction for generating this section</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSectionInstruction) -> dict:
    out: dict = {}
    out["sectionHeader"] = value["section_header"]
    out["sectionInstruction"] = value["section_instruction"]
    return out


def deserialize_json(data: dict) -> TemplateSectionInstruction:
    out: TemplateSectionInstruction = {}  # type: ignore[typeddict-item]
    if data.get("sectionHeader") is not None:
        out["section_header"] = data["sectionHeader"]
    else:
        out["section_header"] = ""
    if data.get("sectionInstruction") is not None:
        out["section_instruction"] = data["sectionInstruction"]
    else:
        out["section_instruction"] = ""
    return out


def redact_sensitive(value: TemplateSectionInstruction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "section_header" in value:
        out["section_header"] = "*** Sensitive Data Redacted ***"
    if "section_instruction" in value:
        out["section_instruction"] = "*** Sensitive Data Redacted ***"
    return out
