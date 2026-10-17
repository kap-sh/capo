"""Generated from Smithy shape ``com.amazonaws.lambdaweb#AuthType``."""

from typing import Literal, TypeAlias, cast

"""<p>The authorization type for a web function endpoint.</p> <p>Valid values:</p> <ul> <li> <p> <code>ApplicationManaged</code> – Your application handles authorization.</p> </li> <li> <p> <code>IamAuth</code> – Lambda uses IAM to authorize requests, which must be signed with Signature Version 4 (SigV4).</p> </li> </ul>"""
AuthType: TypeAlias = Literal[
    "ApplicationManaged",
    "IamAuth",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    return cast(AuthType, data)
