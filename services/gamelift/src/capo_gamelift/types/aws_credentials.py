"""Generated from Smithy shape ``com.amazonaws.gamelift#AwsCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string


class AwsCredentials(TypedDict, closed=True):
    access_key_id: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>The access key ID that identifies the temporary security credentials. </p>"""
    secret_access_key: NotRequired[
        "capo_gamelift.types.non_empty_string.NonEmptyString"
    ]
    """<p>The secret access key that can be used to sign requests.</p>"""
    session_token: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>The token that users must pass to the service API to use the temporary credentials. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsCredentials) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["AccessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["SecretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["SessionToken"] = value["session_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AwsCredentials:
    out: AwsCredentials = {}  # type: ignore[typeddict-item]
    if data.get("AccessKeyId") is not None:
        out["access_key_id"] = data["AccessKeyId"]
    if data.get("SecretAccessKey") is not None:
        out["secret_access_key"] = data["SecretAccessKey"]
    if data.get("SessionToken") is not None:
        out["session_token"] = data["SessionToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AwsCredentials) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["AccessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["SecretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["SessionToken"] = value["session_token"]
    return out


def deserialize_cbor(data: dict) -> AwsCredentials:
    out: AwsCredentials = {}  # type: ignore[typeddict-item]
    if data.get("AccessKeyId") is not None:
        out["access_key_id"] = data["AccessKeyId"]
    if data.get("SecretAccessKey") is not None:
        out["secret_access_key"] = data["SecretAccessKey"]
    if data.get("SessionToken") is not None:
        out["session_token"] = data["SessionToken"]
    return out
