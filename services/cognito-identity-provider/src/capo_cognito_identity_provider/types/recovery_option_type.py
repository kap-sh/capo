"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RecoveryOptionType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.priority_type
    import capo_cognito_identity_provider.types.recovery_option_name_type


class RecoveryOptionType(TypedDict, closed=True):
    priority: "capo_cognito_identity_provider.types.priority_type.PriorityType"
    """<p>Your priority preference for using the specified attribute in account recovery. The highest priority is <code>1</code>.</p>"""
    name: "capo_cognito_identity_provider.types.recovery_option_name_type.RecoveryOptionNameType"
    """<p>The recovery method that this object sets a recovery option for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecoveryOptionType) -> dict:
    out: dict = {}
    out["Priority"] = value["priority"]
    import capo_cognito_identity_provider.types.recovery_option_name_type

    out["Name"] = (
        capo_cognito_identity_provider.types.recovery_option_name_type.serialize_aws_json_1_1(
            value["name"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecoveryOptionType:
    out: RecoveryOptionType = {}  # type: ignore[typeddict-item]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if data.get("Name") is not None:
        import capo_cognito_identity_provider.types.recovery_option_name_type

        out["name"] = (
            capo_cognito_identity_provider.types.recovery_option_name_type.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_cognito_identity_provider.types.recovery_option_name_type.RecoveryOptionNameType",
            "",
        )
    return out
