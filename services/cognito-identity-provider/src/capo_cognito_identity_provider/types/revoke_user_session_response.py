"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RevokeUserSessionResponse``."""

from typing_extensions import TypedDict


class RevokeUserSessionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeUserSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeUserSessionResponse:
    out: RevokeUserSessionResponse = {}  # type: ignore[typeddict-item]
    return out
