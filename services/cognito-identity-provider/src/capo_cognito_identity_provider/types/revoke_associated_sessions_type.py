"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RevokeAssociatedSessionsType``."""

from typing import Literal, TypeAlias, cast

"""<p>Controls whether revoking a session also revokes the sessions that are linked to it. <code>NONE</code> revokes only the targeted session. <code>LINKED</code> also revokes the directly linked session or sessions, interpreted relative to the type of the targeted session: revoking a token session also revokes the parent SSO session it came through, and revoking an SSO session also revokes the token sessions that came through it. The set of linked sessions is eventually consistent, so associated sessions are typically revoked within a few seconds.</p>"""
RevokeAssociatedSessionsType: TypeAlias = Literal[
    "NONE",
    "LINKED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeAssociatedSessionsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RevokeAssociatedSessionsType:
    return cast(RevokeAssociatedSessionsType, data)
