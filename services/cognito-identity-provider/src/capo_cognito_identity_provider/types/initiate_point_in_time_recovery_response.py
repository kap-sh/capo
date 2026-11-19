"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InitiatePointInTimeRecoveryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.restoration_type


class InitiatePointInTimeRecoveryResponse(TypedDict, closed=True):
    restoration: NotRequired[
        "capo_cognito_identity_provider.types.restoration_type.RestorationType"
    ]
    """<p>The details of the recovery that you initiated. Includes the recovery ID that you can use in later requests to describe, start, or cancel the recovery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InitiatePointInTimeRecoveryResponse) -> dict:
    out: dict = {}
    if "restoration" in value:
        import capo_cognito_identity_provider.types.restoration_type

        out["Restoration"] = (
            capo_cognito_identity_provider.types.restoration_type.serialize_aws_json_1_1(
                value["restoration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InitiatePointInTimeRecoveryResponse:
    out: InitiatePointInTimeRecoveryResponse = {}  # type: ignore[typeddict-item]
    if data.get("Restoration") is not None:
        import capo_cognito_identity_provider.types.restoration_type

        out["restoration"] = (
            capo_cognito_identity_provider.types.restoration_type.deserialize_aws_json_1_1(
                data["Restoration"]
            )
        )
    return out
