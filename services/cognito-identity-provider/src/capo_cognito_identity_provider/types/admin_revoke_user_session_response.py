"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminRevokeUserSessionResponse``."""

from typing_extensions import TypedDict


class AdminRevokeUserSessionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminRevokeUserSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminRevokeUserSessionResponse:
    out: AdminRevokeUserSessionResponse = {}  # type: ignore[typeddict-item]
    return out
