"""Generated from Smithy shape ``com.amazonaws.quicksight#Synonyms``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.synonym_string

Synonyms: TypeAlias = list["capo_quicksight.types.synonym_string.SynonymString"]


# --- restJson1 ser/de ---
def serialize_json(value: Synonyms) -> list:
    return list(value)


def deserialize_json(data: list) -> Synonyms:
    return [item for item in data if item is not None]


def redact_sensitive(value: Synonyms) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
