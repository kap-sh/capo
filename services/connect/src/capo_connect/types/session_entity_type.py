"""Generated from Smithy shape ``com.amazonaws.connect#SessionEntityType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the type of entity whose sessions you delete when you call <code>DeleteAllEntitySessions</code>. The only valid value is <code>USER</code>, which targets a user in your Connect Customer instance.</p>"""
SessionEntityType: TypeAlias = Literal["USER",]


# --- restJson1 ser/de ---
def serialize_json(value: SessionEntityType) -> str:
    return value


def deserialize_json(data: str) -> SessionEntityType:
    return cast(SessionEntityType, data)
