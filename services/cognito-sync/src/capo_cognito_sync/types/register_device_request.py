"""Generated from Smithy shape ``com.amazonaws.cognitosync#RegisterDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.identity_id
    import capo_cognito_sync.types.identity_pool_id
    import capo_cognito_sync.types.platform
    import capo_cognito_sync.types.push_token


class RegisterDeviceRequest(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """<p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.</p>"""
    identity_id: "capo_cognito_sync.types.identity_id.IdentityId"
    """<p>The unique ID for this identity.</p>"""
    platform: "capo_cognito_sync.types.platform.Platform"
    """<p>The SNS platform type (e.g. GCM, SDM, APNS, APNS_SANDBOX).</p>"""
    token: "capo_cognito_sync.types.push_token.PushToken"
    """<p>The push token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterDeviceRequest) -> dict:
    out: dict = {}
    import capo_cognito_sync.types.platform

    out["Platform"] = capo_cognito_sync.types.platform.serialize_json(value["platform"])
    out["Token"] = value["token"]
    return out


def deserialize_json(data: dict) -> RegisterDeviceRequest:
    out: RegisterDeviceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Platform") is not None:
        import capo_cognito_sync.types.platform

        out["platform"] = capo_cognito_sync.types.platform.deserialize_json(
            data["Platform"]
        )
    else:
        import typing

        out["platform"] = typing.cast("capo_cognito_sync.types.platform.Platform", "")
    if data.get("Token") is not None:
        out["token"] = data["Token"]
    else:
        out["token"] = ""
    return out
