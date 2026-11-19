"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ApplicationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of application described by an application context.</p>"""
ApplicationType: TypeAlias = Literal[
    "SAS",
    "DESKTOP_APPLICATION",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    return cast(ApplicationType, data)
