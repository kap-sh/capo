"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StartWebAuthnRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.document


class StartWebAuthnRegistrationResponse(TypedDict, closed=True):
    credential_creation_options: (
        "capo_cognito_identity_provider.types.document.Document"
    )
    """<p>The information that a user can provide in their request to register with their passkey provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWebAuthnRegistrationResponse) -> dict:
    out: dict = {}
    out["CredentialCreationOptions"] = value["credential_creation_options"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWebAuthnRegistrationResponse:
    out: StartWebAuthnRegistrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("CredentialCreationOptions") is not None:
        out["credential_creation_options"] = data["CredentialCreationOptions"]
    else:
        out["credential_creation_options"] = None
    return out
