"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PreferenceKey``."""

from typing import Literal, TypeAlias, cast

"""<p>Identifies one of the caller's Well-Architected Agent preferences. A new preference is introduced as a new enum value, which is a backward-compatible change. Existing values are never removed or renamed.</p>"""
PreferenceKey: TypeAlias = Literal["ORG_INTEGRATION",]


# --- restJson1 ser/de ---
def serialize_json(value: PreferenceKey) -> str:
    return value


def deserialize_json(data: str) -> PreferenceKey:
    return cast(PreferenceKey, data)
