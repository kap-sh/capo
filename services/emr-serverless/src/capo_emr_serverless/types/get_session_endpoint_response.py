"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetSessionEndpointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.date
    import capo_emr_serverless.types.endpoint_url
    import capo_emr_serverless.types.session_auth_token
    import capo_emr_serverless.types.session_id


class GetSessionEndpointResponse(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The output contains the ID of the application.</p>"""
    session_id: "capo_emr_serverless.types.session_id.SessionId"
    """<p>The output contains the ID of the session.</p>"""
    endpoint: "capo_emr_serverless.types.endpoint_url.EndpointUrl"
    """<p>The endpoint URL for connecting to the session.</p>"""
    auth_token: "capo_emr_serverless.types.session_auth_token.SessionAuthToken"
    """<p>The authentication token for connecting to the session endpoint. Call <code>GetSessionEndpoint</code> again to obtain a new token before it expires.</p>"""
    auth_token_expires_at: "capo_emr_serverless.types.date.Date"
    """<p>The expiration time of the authentication token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionEndpointResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["sessionId"] = value["session_id"]
    out["endpoint"] = value["endpoint"]
    out["authToken"] = value["auth_token"]
    import capo_emr_serverless.types.date

    out["authTokenExpiresAt"] = capo_emr_serverless.types.date.serialize_json(
        value["auth_token_expires_at"]
    )
    return out


def deserialize_json(data: dict) -> GetSessionEndpointResponse:
    out: GetSessionEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("GetSessionEndpointResponse.application_id required")
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("GetSessionEndpointResponse.session_id required")
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("GetSessionEndpointResponse.endpoint required")
    if data.get("authToken") is not None:
        out["auth_token"] = data["authToken"]
    else:
        raise DeserializationError("GetSessionEndpointResponse.auth_token required")
    if data.get("authTokenExpiresAt") is not None:
        import capo_emr_serverless.types.date

        out["auth_token_expires_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["authTokenExpiresAt"]
        )
    else:
        raise DeserializationError(
            "GetSessionEndpointResponse.auth_token_expires_at required"
        )
    return out


def redact_sensitive(value: GetSessionEndpointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_token" in value:
        out["auth_token"] = "*** Sensitive Data Redacted ***"
    return out
