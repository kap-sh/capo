"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribePointInTimeRecoveryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.restoration_type


class DescribePointInTimeRecoveryResponse(TypedDict, closed=True):
    restoration: NotRequired[
        "capo_cognito_identity_provider.types.restoration_type.RestorationType"
    ]
    """<p>The details of the requested recovery, including its status, the point in time that it restores the user pool to, and the recovery preview.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePointInTimeRecoveryResponse) -> dict:
    out: dict = {}
    if "restoration" in value:
        import capo_cognito_identity_provider.types.restoration_type

        out["Restoration"] = (
            capo_cognito_identity_provider.types.restoration_type.serialize_aws_json_1_1(
                value["restoration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePointInTimeRecoveryResponse:
    out: DescribePointInTimeRecoveryResponse = {}  # type: ignore[typeddict-item]
    if data.get("Restoration") is not None:
        import capo_cognito_identity_provider.types.restoration_type

        out["restoration"] = (
            capo_cognito_identity_provider.types.restoration_type.deserialize_aws_json_1_1(
                data["Restoration"]
            )
        )
    return out
