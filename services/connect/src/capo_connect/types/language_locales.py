"""Generated from Smithy shape ``com.amazonaws.connect#LanguageLocales``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.language_locale

LanguageLocales: TypeAlias = list["capo_connect.types.language_locale.LanguageLocale"]


# --- restJson1 ser/de ---
def serialize_json(value: LanguageLocales) -> list:
    return list(value)


def deserialize_json(data: list) -> LanguageLocales:
    return [item for item in data if item is not None]
