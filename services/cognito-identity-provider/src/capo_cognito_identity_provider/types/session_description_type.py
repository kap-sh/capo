"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SessionDescriptionType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.session_device_type
    import capo_cognito_identity_provider.types.session_id_type
    import capo_cognito_identity_provider.types.session_ip_address_type
    import capo_cognito_identity_provider.types.session_location_type
    import capo_cognito_identity_provider.types.session_type_type
    import capo_cognito_identity_provider.types.wrapped_boolean_type


class SessionDescriptionType(TypedDict, closed=True):
    session_id: NotRequired[
        "capo_cognito_identity_provider.types.session_id_type.SessionIdType"
    ]
    """<p>The unique identifier for the session. This is a 28-character string of lowercase letters and digits, prefixed with <code>tkn</code> for a token session or <code>sso</code> for an SSO session.</p>"""
    session_type: NotRequired[
        "capo_cognito_identity_provider.types.session_type_type.SessionTypeType"
    ]
    """<p>The type of the session. Valid values are <code>TOKEN</code> and <code>SSO</code>.</p>"""
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The ID of the app client that the session belongs to.</p>"""
    create_date: NotRequired["capo_cognito_identity_provider.types.date_type.DateType"]
    """<p>The date and time when the session was created.</p>"""
    last_active_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time of the most recent activity on the session. For a token session, this is the most recent token refresh or rotation; a new authentication creates a new token session rather than updating an existing one. For an SSO session, this is the most recent authentication, token grant, or token rotation.</p>"""
    device_type: NotRequired[
        "capo_cognito_identity_provider.types.session_device_type.SessionDeviceType"
    ]
    """<p>A description of the device associated with the most recent activity on the session, derived from the parsed user agent (operating system and browser or app). Amazon Cognito overwrites this value on each sign-in, refresh, and rotation. The value can be <code>unknown</code>. The maximum length is 1,024 characters.</p>"""
    last_ip_address: NotRequired[
        "capo_cognito_identity_provider.types.session_ip_address_type.SessionIpAddressType"
    ]
    """<p>The IP address associated with the most recent activity on the session. Amazon Cognito overwrites this value on each refresh and rotation. The maximum length is 128 characters.</p>"""
    last_location: NotRequired[
        "capo_cognito_identity_provider.types.session_location_type.SessionLocationType"
    ]
    """<p>The geographic location of the most recent activity on the session, derived from the IP address.</p>"""
    origin_session_id: NotRequired[
        "capo_cognito_identity_provider.types.session_id_type.SessionIdType"
    ]
    """<p>For a token session, the ID of the SSO session that the token session originated from. This value is null for sessions that were initiated through the API and didn't come through an SSO session. Amazon Cognito returns this value for token sessions only.</p>"""
    is_current_session: NotRequired[
        "capo_cognito_identity_provider.types.wrapped_boolean_type.WrappedBooleanType"
    ]
    """<p>Specifies whether this session matches the access token supplied in the request. This value is always <code>false</code> for the <code>AdminListUserSessions</code> operation, which doesn't take an access token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionDescriptionType) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "session_type" in value:
        import capo_cognito_identity_provider.types.session_type_type

        out["SessionType"] = (
            capo_cognito_identity_provider.types.session_type_type.serialize_aws_json_1_1(
                value["session_type"]
            )
        )
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "create_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreateDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["create_date"]
            )
        )
    if "last_active_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastActiveDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_active_date"]
            )
        )
    if "device_type" in value:
        out["DeviceType"] = value["device_type"]
    if "last_ip_address" in value:
        out["LastIPAddress"] = value["last_ip_address"]
    if "last_location" in value:
        import capo_cognito_identity_provider.types.session_location_type

        out["LastLocation"] = (
            capo_cognito_identity_provider.types.session_location_type.serialize_aws_json_1_1(
                value["last_location"]
            )
        )
    if "origin_session_id" in value:
        out["OriginSessionId"] = value["origin_session_id"]
    if "is_current_session" in value:
        out["IsCurrentSession"] = value["is_current_session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionDescriptionType:
    out: SessionDescriptionType = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    if data.get("SessionType") is not None:
        import capo_cognito_identity_provider.types.session_type_type

        out["session_type"] = (
            capo_cognito_identity_provider.types.session_type_type.deserialize_aws_json_1_1(
                data["SessionType"]
            )
        )
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("CreateDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["create_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreateDate"]
            )
        )
    if data.get("LastActiveDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["last_active_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastActiveDate"]
            )
        )
    if data.get("DeviceType") is not None:
        out["device_type"] = data["DeviceType"]
    if data.get("LastIPAddress") is not None:
        out["last_ip_address"] = data["LastIPAddress"]
    if data.get("LastLocation") is not None:
        import capo_cognito_identity_provider.types.session_location_type

        out["last_location"] = (
            capo_cognito_identity_provider.types.session_location_type.deserialize_aws_json_1_1(
                data["LastLocation"]
            )
        )
    if data.get("OriginSessionId") is not None:
        out["origin_session_id"] = data["OriginSessionId"]
    if data.get("IsCurrentSession") is not None:
        out["is_current_session"] = data["IsCurrentSession"]
    return out


def redact_sensitive(value: SessionDescriptionType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    if "last_ip_address" in value:
        out["last_ip_address"] = "*** Sensitive Data Redacted ***"
    return out
