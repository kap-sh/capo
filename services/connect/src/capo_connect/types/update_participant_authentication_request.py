"""Generated from Smithy shape ``com.amazonaws.connect#UpdateParticipantAuthenticationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.authentication_error
    import capo_connect.types.authentication_error_description
    import capo_connect.types.authorization_code
    import capo_connect.types.instance_id
    import capo_connect.types.participant_token


class UpdateParticipantAuthenticationRequest(TypedDict, closed=True):
    state: "capo_connect.types.participant_token.ParticipantToken"
    """<p>The <code>state</code> query parameter that was provided by Cognito in the <code>redirectUri</code>. This will also match the <code>state</code> parameter provided in the <code>AuthenticationUrl</code> from the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_GetAuthenticationUrl.html">GetAuthenticationUrl</a> response.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    code: NotRequired["capo_connect.types.authorization_code.AuthorizationCode"]
    """<p>The <code>code</code> query parameter provided by Cognito in the <code>redirectUri</code>.</p>"""
    error: NotRequired["capo_connect.types.authentication_error.AuthenticationError"]
    """<p>The <code>error</code> query parameter provided by Cognito in the <code>redirectUri</code>.</p>"""
    error_description: NotRequired[
        "capo_connect.types.authentication_error_description.AuthenticationErrorDescription"
    ]
    """<p>The <code>error_description</code> parameter provided by Cognito in the <code>redirectUri</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateParticipantAuthenticationRequest) -> dict:
    out: dict = {}
    out["State"] = value["state"]
    out["InstanceId"] = value["instance_id"]
    if "code" in value:
        out["Code"] = value["code"]
    if "error" in value:
        out["Error"] = value["error"]
    if "error_description" in value:
        out["ErrorDescription"] = value["error_description"]
    return out


def deserialize_json(data: dict) -> UpdateParticipantAuthenticationRequest:
    out: UpdateParticipantAuthenticationRequest = {}  # type: ignore[typeddict-item]
    if data.get("State") is not None:
        out["state"] = data["State"]
    else:
        raise DeserializationError(
            "UpdateParticipantAuthenticationRequest.state required"
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "UpdateParticipantAuthenticationRequest.instance_id required"
        )
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Error") is not None:
        out["error"] = data["Error"]
    if data.get("ErrorDescription") is not None:
        out["error_description"] = data["ErrorDescription"]
    return out
