"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#LoginsMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_provider_name
    import capo_cognito_identity.types.identity_provider_token

LoginsMap: TypeAlias = dict[
    "capo_cognito_identity.types.identity_provider_name.IdentityProviderName",
    "capo_cognito_identity.types.identity_provider_token.IdentityProviderToken",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LoginsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LoginsMap:
    out: LoginsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: LoginsMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
