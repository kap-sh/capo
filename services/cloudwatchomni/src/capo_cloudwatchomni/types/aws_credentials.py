"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AwsCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.access_key_id
    import capo_cloudwatchomni.types.secret_access_key
    import capo_cloudwatchomni.types.session_token


class AwsCredentials(TypedDict, closed=True):
    access_key_id: "capo_cloudwatchomni.types.access_key_id.AccessKeyId"
    """The AWS access key ID."""
    secret_access_key: "capo_cloudwatchomni.types.secret_access_key.SecretAccessKey"
    """The AWS secret access key."""
    session_token: "capo_cloudwatchomni.types.session_token.SessionToken"
    """The AWS session token."""
    expiration: "datetime.datetime"
    """The timestamp when the credentials expire."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AwsCredentials) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["sessionToken"] = value["session_token"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["expiration"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["expiration"]
    )
    return out


def deserialize_cbor(data: dict) -> AwsCredentials:
    out: AwsCredentials = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    else:
        out["access_key_id"] = ""
    if data.get("secretAccessKey") is not None:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        out["secret_access_key"] = ""
    if data.get("sessionToken") is not None:
        out["session_token"] = data["sessionToken"]
    else:
        out["session_token"] = ""
    if data.get("expiration") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["expiration"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["expiration"]
            )
        )
    else:
        import datetime

        out["expiration"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
