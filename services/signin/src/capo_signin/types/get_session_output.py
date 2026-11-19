"""Generated from Smithy shape ``com.amazonaws.signin#GetSessionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.client_type
    import capo_signin.types.principal_arn
    import capo_signin.types.session_arn
    import capo_signin.types.session_status


class GetSessionOutput(TypedDict, closed=True):
    session_arn: "capo_signin.types.session_arn.SessionArn"
    """The session ARN"""
    principal_arn: "capo_signin.types.principal_arn.PrincipalArn"
    """The IAM identity that owns the session"""
    role: NotRequired["capo_signin.types.principal_arn.PrincipalArn"]
    """The IAM role for the session, when the owner is a role"""
    status: NotRequired["capo_signin.types.session_status.SessionStatus"]
    """The session status"""
    client_id: NotRequired["str"]
    """The OAuth client that created the session"""
    client_type: NotRequired["capo_signin.types.client_type.ClientType"]
    """The type of OAuth client that created the session"""
    resource: NotRequired["str"]
    """The resource that the session's tokens are bound to"""
    issued_at: "int"
    """The time the session was created, in Unix epoch seconds"""
    expires_at: "int"
    """The time the session expires, in Unix epoch seconds"""
    last_used_at: NotRequired["int"]
    """The time the session was last refreshed, in Unix epoch seconds"""
    issued_in_region: NotRequired["str"]
    """The AWS Region where the session was created"""
    origin_session_arn: NotRequired["capo_signin.types.session_arn.SessionArn"]
    """The ARN of the session this session originated from"""
    user_agent: NotRequired["str"]
    """The user agent captured when the session was created or last refreshed"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionOutput) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    out["principalArn"] = value["principal_arn"]
    if "role" in value:
        out["role"] = value["role"]
    if "status" in value:
        import capo_signin.types.session_status

        out["status"] = capo_signin.types.session_status.serialize_json(value["status"])
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "client_type" in value:
        import capo_signin.types.client_type

        out["clientType"] = capo_signin.types.client_type.serialize_json(
            value["client_type"]
        )
    if "resource" in value:
        out["resource"] = value["resource"]
    out["issuedAt"] = value["issued_at"]
    out["expiresAt"] = value["expires_at"]
    if "last_used_at" in value:
        out["lastUsedAt"] = value["last_used_at"]
    if "issued_in_region" in value:
        out["issuedInRegion"] = value["issued_in_region"]
    if "origin_session_arn" in value:
        out["originSessionArn"] = value["origin_session_arn"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    return out


def deserialize_json(data: dict) -> GetSessionOutput:
    out: GetSessionOutput = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    else:
        out["principal_arn"] = ""
    if data.get("role") is not None:
        out["role"] = data["role"]
    if data.get("status") is not None:
        import capo_signin.types.session_status

        out["status"] = capo_signin.types.session_status.deserialize_json(
            data["status"]
        )
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("clientType") is not None:
        import capo_signin.types.client_type

        out["client_type"] = capo_signin.types.client_type.deserialize_json(
            data["clientType"]
        )
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    if data.get("issuedAt") is not None:
        out["issued_at"] = data["issuedAt"]
    else:
        out["issued_at"] = 0
    if data.get("expiresAt") is not None:
        out["expires_at"] = data["expiresAt"]
    else:
        out["expires_at"] = 0
    if data.get("lastUsedAt") is not None:
        out["last_used_at"] = data["lastUsedAt"]
    if data.get("issuedInRegion") is not None:
        out["issued_in_region"] = data["issuedInRegion"]
    if data.get("originSessionArn") is not None:
        out["origin_session_arn"] = data["originSessionArn"]
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    return out
