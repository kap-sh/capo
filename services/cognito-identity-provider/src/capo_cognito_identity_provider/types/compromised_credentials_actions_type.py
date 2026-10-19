"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CompromisedCredentialsActionsType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.compromised_credentials_event_action_type


class CompromisedCredentialsActionsType(TypedDict, closed=True):
    event_action: "capo_cognito_identity_provider.types.compromised_credentials_event_action_type.CompromisedCredentialsEventActionType"
    """<p>The action that Amazon Cognito takes when it detects compromised credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompromisedCredentialsActionsType) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.compromised_credentials_event_action_type

    out["EventAction"] = (
        capo_cognito_identity_provider.types.compromised_credentials_event_action_type.serialize_aws_json_1_1(
            value["event_action"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompromisedCredentialsActionsType:
    out: CompromisedCredentialsActionsType = {}  # type: ignore[typeddict-item]
    if data.get("EventAction") is not None:
        import capo_cognito_identity_provider.types.compromised_credentials_event_action_type

        out["event_action"] = (
            capo_cognito_identity_provider.types.compromised_credentials_event_action_type.deserialize_aws_json_1_1(
                data["EventAction"]
            )
        )
    else:
        import typing

        out["event_action"] = typing.cast(
            "capo_cognito_identity_provider.types.compromised_credentials_event_action_type.CompromisedCredentialsEventActionType",
            "",
        )
    return out
