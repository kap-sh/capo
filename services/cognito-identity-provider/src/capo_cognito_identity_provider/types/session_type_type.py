"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SessionTypeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a user session. <code>TOKEN</code> identifies a token session, which represents an app's authenticated session for a user and is tied to a refresh token. <code>SSO</code> identifies an SSO session, which is a single sign-on (SSO) session that records an authentication through managed login and can let the user sign in to other apps without re-authenticating.</p>"""
SessionTypeType: TypeAlias = Literal[
    "TOKEN",
    "SSO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionTypeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionTypeType:
    return cast(SessionTypeType, data)
