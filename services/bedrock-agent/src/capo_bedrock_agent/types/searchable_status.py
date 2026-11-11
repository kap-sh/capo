"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SearchableStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether a custom metadata field is searchable. The knowledge base matches query text against the values of searchable fields.</p>"""
SearchableStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableStatus) -> str:
    return value


def deserialize_json(data: str) -> SearchableStatus:
    return cast(SearchableStatus, data)
