"""Generated from Smithy shape ``com.amazonaws.sesv2#IdentityFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The filter key to use when listing email identities. This can be one of the following:</p> <ul> <li> <p> <code>IDENTITY_NAME_CONTAINS</code> – Filter by a substring of the identity name.</p> </li> <li> <p> <code>IDENTITY_TYPE</code> – Filter by identity type.</p> </li> <li> <p> <code>VERIFICATION_STATUS</code> – Filter by verification status.</p> </li> </ul>"""
IdentityFilterKey: TypeAlias = Literal[
    "IDENTITY_NAME_CONTAINS",
    "IDENTITY_TYPE",
    "VERIFICATION_STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityFilterKey) -> str:
    return value


def deserialize_json(data: str) -> IdentityFilterKey:
    return cast(IdentityFilterKey, data)
