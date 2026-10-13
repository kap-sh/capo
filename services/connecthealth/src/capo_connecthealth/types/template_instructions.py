"""Generated from Smithy shape ``com.amazonaws.connecthealth#TemplateInstructions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.template_section_instruction

TemplateInstructions: TypeAlias = list[
    "capo_connecthealth.types.template_section_instruction.TemplateSectionInstruction"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateInstructions) -> list:
    import capo_connecthealth.types.template_section_instruction

    out: list = []
    for item in value:
        out.append(
            capo_connecthealth.types.template_section_instruction.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TemplateInstructions:
    import capo_connecthealth.types.template_section_instruction

    out: TemplateInstructions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connecthealth.types.template_section_instruction.deserialize_json(item)
        )
    return out


def redact_sensitive(value: TemplateInstructions) -> list[Any]:
    import capo_connecthealth.types.template_section_instruction

    return [
        capo_connecthealth.types.template_section_instruction.redact_sensitive(item)
        for item in value
    ]
