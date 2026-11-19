"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a context, describing the kind of application or environment metadata it carries.</p>"""
ContextType: TypeAlias = Literal["APPLICATION",]


# --- restJson1 ser/de ---
def serialize_json(value: ContextType) -> str:
    return value


def deserialize_json(data: str) -> ContextType:
    return cast(ContextType, data)
