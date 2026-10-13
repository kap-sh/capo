"""Generated from Smithy shape ``com.amazonaws.datazone#DetailedGlossaryTerms``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.detailed_glossary_term

DetailedGlossaryTerms: TypeAlias = list[
    "capo_datazone.types.detailed_glossary_term.DetailedGlossaryTerm"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetailedGlossaryTerms) -> list:
    import capo_datazone.types.detailed_glossary_term

    out: list = []
    for item in value:
        out.append(capo_datazone.types.detailed_glossary_term.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetailedGlossaryTerms:
    import capo_datazone.types.detailed_glossary_term

    out: DetailedGlossaryTerms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.detailed_glossary_term.deserialize_json(item))
    return out


def redact_sensitive(value: DetailedGlossaryTerms) -> list[Any]:
    import capo_datazone.types.detailed_glossary_term

    return [
        capo_datazone.types.detailed_glossary_term.redact_sensitive(item)
        for item in value
    ]
