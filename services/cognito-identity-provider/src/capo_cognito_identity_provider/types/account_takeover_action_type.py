"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AccountTakeoverActionType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.account_takeover_action_notify_type
    import capo_cognito_identity_provider.types.account_takeover_event_action_type


class AccountTakeoverActionType(TypedDict, closed=True):
    notify: "capo_cognito_identity_provider.types.account_takeover_action_notify_type.AccountTakeoverActionNotifyType"
    """<p>Determines whether Amazon Cognito sends a user a notification message when your user pools assesses a user's session at the associated risk level.</p>"""
    event_action: "capo_cognito_identity_provider.types.account_takeover_event_action_type.AccountTakeoverEventActionType"
    """<p>The action to take for the attempted account takeover action for the associated risk level. Valid values are as follows:</p> <ul> <li> <p> <code>BLOCK</code>: Block the request.</p> </li> <li> <p> <code>MFA_IF_CONFIGURED</code>: Present an MFA challenge if possible. MFA is possible if the user pool has active MFA methods that the user can set up. For example, if the user pool only supports SMS message MFA but the user doesn't have a phone number attribute, MFA setup isn't possible. If MFA setup isn't possible, allow the request.</p> </li> <li> <p> <code>MFA_REQUIRED</code>: Present an MFA challenge if possible. Block the request if a user hasn't set up MFA. To sign in with required MFA, users must have an email address or phone number attribute, or a registered TOTP factor.</p> </li> <li> <p> <code>NO_ACTION</code>: Take no action. Permit sign-in.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountTakeoverActionType) -> dict:
    out: dict = {}
    out["Notify"] = value.get("notify", False)
    import capo_cognito_identity_provider.types.account_takeover_event_action_type

    out["EventAction"] = (
        capo_cognito_identity_provider.types.account_takeover_event_action_type.serialize_aws_json_1_1(
            value["event_action"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountTakeoverActionType:
    out: AccountTakeoverActionType = {}  # type: ignore[typeddict-item]
    if data.get("Notify") is not None:
        out["notify"] = data["Notify"]
    else:
        out["notify"] = False
    if data.get("EventAction") is not None:
        import capo_cognito_identity_provider.types.account_takeover_event_action_type

        out["event_action"] = (
            capo_cognito_identity_provider.types.account_takeover_event_action_type.deserialize_aws_json_1_1(
                data["EventAction"]
            )
        )
    else:
        import typing

        out["event_action"] = typing.cast(
            "capo_cognito_identity_provider.types.account_takeover_event_action_type.AccountTakeoverEventActionType",
            "",
        )
    return out
