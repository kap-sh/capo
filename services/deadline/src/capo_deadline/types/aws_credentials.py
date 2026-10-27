"""Generated from Smithy shape ``com.amazonaws.deadline#AwsCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.access_key_id
    import capo_deadline.types.secret_access_key
    import capo_deadline.types.session_token
    import capo_deadline.types.timestamp


class AwsCredentials(TypedDict, closed=True):
    access_key_id: "capo_deadline.types.access_key_id.AccessKeyId"
    """The IAM access key ID."""
    secret_access_key: "capo_deadline.types.secret_access_key.SecretAccessKey"
    """The IAM secret access key."""
    session_token: "capo_deadline.types.session_token.SessionToken"
    """The IAM session token"""
    expiration: "capo_deadline.types.timestamp.Timestamp"
    """The expiration date and time of the IAM credentials."""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCredentials) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["sessionToken"] = value["session_token"]
    import capo_deadline._protocol.serialize

    out["expiration"] = capo_deadline._protocol.serialize.fmt_date_time(
        value["expiration"]
    )
    return out


def deserialize_json(data: dict) -> AwsCredentials:
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
        import datetime

        out["expiration"] = datetime.datetime.fromisoformat(
            data["expiration"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["expiration"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
