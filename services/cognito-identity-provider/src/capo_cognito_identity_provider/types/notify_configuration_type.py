"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#NotifyConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.notify_email_type
    import capo_cognito_identity_provider.types.string_type

NotifyConfigurationType = TypedDict(
    "NotifyConfigurationType",
    {
        "from": NotRequired[
            "capo_cognito_identity_provider.types.string_type.StringType"
        ],
        "reply_to": NotRequired[
            "capo_cognito_identity_provider.types.string_type.StringType"
        ],
        "source_arn": "capo_cognito_identity_provider.types.arn_type.ArnType",
        "block_email": NotRequired[
            "capo_cognito_identity_provider.types.notify_email_type.NotifyEmailType"
        ],
        "no_action_email": NotRequired[
            "capo_cognito_identity_provider.types.notify_email_type.NotifyEmailType"
        ],
        "mfa_email": NotRequired[
            "capo_cognito_identity_provider.types.notify_email_type.NotifyEmailType"
        ],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyConfigurationType) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = value["from"]
    if "reply_to" in value:
        out["ReplyTo"] = value["reply_to"]
    out["SourceArn"] = value["source_arn"]
    if "block_email" in value:
        import capo_cognito_identity_provider.types.notify_email_type

        out["BlockEmail"] = (
            capo_cognito_identity_provider.types.notify_email_type.serialize_aws_json_1_1(
                value["block_email"]
            )
        )
    if "no_action_email" in value:
        import capo_cognito_identity_provider.types.notify_email_type

        out["NoActionEmail"] = (
            capo_cognito_identity_provider.types.notify_email_type.serialize_aws_json_1_1(
                value["no_action_email"]
            )
        )
    if "mfa_email" in value:
        import capo_cognito_identity_provider.types.notify_email_type

        out["MfaEmail"] = (
            capo_cognito_identity_provider.types.notify_email_type.serialize_aws_json_1_1(
                value["mfa_email"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyConfigurationType:
    out: NotifyConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("From") is not None:
        out["from"] = data["From"]
    if data.get("ReplyTo") is not None:
        out["reply_to"] = data["ReplyTo"]
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("BlockEmail") is not None:
        import capo_cognito_identity_provider.types.notify_email_type

        out["block_email"] = (
            capo_cognito_identity_provider.types.notify_email_type.deserialize_aws_json_1_1(
                data["BlockEmail"]
            )
        )
    if data.get("NoActionEmail") is not None:
        import capo_cognito_identity_provider.types.notify_email_type

        out["no_action_email"] = (
            capo_cognito_identity_provider.types.notify_email_type.deserialize_aws_json_1_1(
                data["NoActionEmail"]
            )
        )
    if data.get("MfaEmail") is not None:
        import capo_cognito_identity_provider.types.notify_email_type

        out["mfa_email"] = (
            capo_cognito_identity_provider.types.notify_email_type.deserialize_aws_json_1_1(
                data["MfaEmail"]
            )
        )
    return out
