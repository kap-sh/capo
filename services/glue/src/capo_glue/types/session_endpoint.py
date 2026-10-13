"""Generated from Smithy shape ``com.amazonaws.glue#SessionEndpoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.sensitive_string
    import capo_glue.types.spark_connect_endpoint_url
    import capo_glue.types.timestamp_value


class SessionEndpoint(TypedDict, closed=True):
    url: "capo_glue.types.spark_connect_endpoint_url.SparkConnectEndpointUrl"
    """<p>The Spark Connect endpoint URL for the session.</p>"""
    auth_token: "capo_glue.types.sensitive_string.SensitiveString"
    """<p>The authentication token to include in requests to the Spark Connect endpoint.</p>"""
    auth_token_expiration_time: "capo_glue.types.timestamp_value.TimestampValue"
    """<p>The time at which the authentication token expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionEndpoint) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    out["AuthToken"] = value["auth_token"]
    import capo_glue.types.timestamp_value

    out["AuthTokenExpirationTime"] = (
        capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["auth_token_expiration_time"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionEndpoint:
    out: SessionEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("SessionEndpoint.url required")
    if data.get("AuthToken") is not None:
        out["auth_token"] = data["AuthToken"]
    else:
        raise DeserializationError("SessionEndpoint.auth_token required")
    if data.get("AuthTokenExpirationTime") is not None:
        import capo_glue.types.timestamp_value

        out["auth_token_expiration_time"] = (
            capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["AuthTokenExpirationTime"]
            )
        )
    else:
        raise DeserializationError(
            "SessionEndpoint.auth_token_expiration_time required"
        )
    return out


def redact_sensitive(value: SessionEndpoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_token" in value:
        out["auth_token"] = "*** Sensitive Data Redacted ***"
    return out
