"""Generated from Smithy shape ``com.amazonaws.lambdaweb#AuthType``."""

from typing import Literal, TypeAlias, cast

"""<p>The authorization type for a web function endpoint. Possible values: <code>ApplicationManaged</code> (the function handles authorization), <code>IamAuth</code> (Lambda authorizes requests with AWS SigV4 and IAM).</p>"""
AuthType: TypeAlias = Literal[
    "ApplicationManaged",
    "IamAuth",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    return cast(AuthType, data)
