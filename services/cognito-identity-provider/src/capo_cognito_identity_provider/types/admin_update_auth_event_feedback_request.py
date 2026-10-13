"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminUpdateAuthEventFeedbackRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.event_id_type
    import capo_cognito_identity_provider.types.feedback_value_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminUpdateAuthEventFeedbackRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to submit authentication-event feedback.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    event_id: "capo_cognito_identity_provider.types.event_id_type.EventIdType"
    """<p>The ID of the threat protection authentication event that you want to update.</p>"""
    feedback_value: (
        "capo_cognito_identity_provider.types.feedback_value_type.FeedbackValueType"
    )
    """<p>Your feedback to the authentication event. When you provide a <code>FeedbackValue</code> value of <code>valid</code>, you tell Amazon Cognito that you trust a user session where Amazon Cognito has evaluated some level of risk. When you provide a <code>FeedbackValue</code> value of <code>invalid</code>, you tell Amazon Cognito that you don't trust a user session, or you don't believe that Amazon Cognito evaluated a high-enough risk level.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminUpdateAuthEventFeedbackRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    out["EventId"] = value["event_id"]
    import capo_cognito_identity_provider.types.feedback_value_type

    out["FeedbackValue"] = (
        capo_cognito_identity_provider.types.feedback_value_type.serialize_aws_json_1_1(
            value["feedback_value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminUpdateAuthEventFeedbackRequest:
    out: AdminUpdateAuthEventFeedbackRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "AdminUpdateAuthEventFeedbackRequest.user_pool_id required"
        )
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError(
            "AdminUpdateAuthEventFeedbackRequest.username required"
        )
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    else:
        raise DeserializationError(
            "AdminUpdateAuthEventFeedbackRequest.event_id required"
        )
    if data.get("FeedbackValue") is not None:
        import capo_cognito_identity_provider.types.feedback_value_type

        out["feedback_value"] = (
            capo_cognito_identity_provider.types.feedback_value_type.deserialize_aws_json_1_1(
                data["FeedbackValue"]
            )
        )
    else:
        raise DeserializationError(
            "AdminUpdateAuthEventFeedbackRequest.feedback_value required"
        )
    return out


def redact_sensitive(value: AdminUpdateAuthEventFeedbackRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
