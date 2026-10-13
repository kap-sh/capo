"""Generated from Smithy shape ``com.amazonaws.ssm#Credentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.access_key_id_type
    import capo_ssm.types.access_key_secret_type
    import capo_ssm.types.date_time
    import capo_ssm.types.session_token_type


class Credentials(TypedDict, closed=True):
    access_key_id: "capo_ssm.types.access_key_id_type.AccessKeyIdType"
    """<p>The access key ID that identifies the temporary security credentials.</p>"""
    secret_access_key: "capo_ssm.types.access_key_secret_type.AccessKeySecretType"
    """<p>The secret access key that can be used to sign requests.</p>"""
    session_token: "capo_ssm.types.session_token_type.SessionTokenType"
    """<p>The token that users must pass to the service API to use the temporary credentials.</p>"""
    expiration_time: "capo_ssm.types.date_time.DateTime"
    """<p>The datetime on which the current credentials expire.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Credentials) -> dict:
    out: dict = {}
    out["AccessKeyId"] = value["access_key_id"]
    out["SecretAccessKey"] = value["secret_access_key"]
    out["SessionToken"] = value["session_token"]
    import capo_ssm.types.date_time

    out["ExpirationTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
        value["expiration_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    if data.get("AccessKeyId") is not None:
        out["access_key_id"] = data["AccessKeyId"]
    else:
        raise DeserializationError("Credentials.access_key_id required")
    if data.get("SecretAccessKey") is not None:
        out["secret_access_key"] = data["SecretAccessKey"]
    else:
        raise DeserializationError("Credentials.secret_access_key required")
    if data.get("SessionToken") is not None:
        out["session_token"] = data["SessionToken"]
    else:
        raise DeserializationError("Credentials.session_token required")
    if data.get("ExpirationTime") is not None:
        import capo_ssm.types.date_time

        out["expiration_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExpirationTime"]
        )
    else:
        raise DeserializationError("Credentials.expiration_time required")
    return out


def redact_sensitive(value: Credentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_access_key" in value:
        out["secret_access_key"] = "*** Sensitive Data Redacted ***"
    if "session_token" in value:
        out["session_token"] = "*** Sensitive Data Redacted ***"
    return out
