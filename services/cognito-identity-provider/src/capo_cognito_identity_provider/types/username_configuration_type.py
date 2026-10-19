"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UsernameConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.wrapped_boolean_type


class UsernameConfigurationType(TypedDict, closed=True):
    case_sensitive: (
        "capo_cognito_identity_provider.types.wrapped_boolean_type.WrappedBooleanType"
    )
    """<p>Specifies whether user name case sensitivity will be applied for all users in the user pool through Amazon Cognito APIs. For most use cases, set case sensitivity to <code>False</code> (case insensitive) as a best practice. When usernames and email addresses are case insensitive, users can sign in as the same user when they enter a different capitalization of their user name.</p> <p>Valid values include:</p> <dl> <dt>true</dt> <dd> <p>Enables case sensitivity for all username input. When this option is set to <code>true</code>, users must sign in using the exact capitalization of their given username, such as “UserName”. This is the default value.</p> </dd> <dt>false</dt> <dd> <p>Enables case insensitivity for all username input. For example, when this option is set to <code>false</code>, users can sign in using <code>username</code>, <code>USERNAME</code>, or <code>UserName</code>. This option also enables both <code>preferred_username</code> and <code>email</code> alias to be case insensitive, in addition to the <code>username</code> attribute.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsernameConfigurationType) -> dict:
    out: dict = {}
    out["CaseSensitive"] = value["case_sensitive"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UsernameConfigurationType:
    out: UsernameConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("CaseSensitive") is not None:
        out["case_sensitive"] = data["CaseSensitive"]
    else:
        out["case_sensitive"] = False
    return out
