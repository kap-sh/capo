"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUICustomizationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.ui_customization_type


class SetUICustomizationResponse(TypedDict, closed=True):
    ui_customization: (
        "capo_cognito_identity_provider.types.ui_customization_type.UICustomizationType"
    )
    """<p>Information about the hosted UI branding that you applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUICustomizationResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.ui_customization_type

    out["UICustomization"] = (
        capo_cognito_identity_provider.types.ui_customization_type.serialize_aws_json_1_1(
            value["ui_customization"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUICustomizationResponse:
    out: SetUICustomizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("UICustomization") is not None:
        import capo_cognito_identity_provider.types.ui_customization_type

        out["ui_customization"] = (
            capo_cognito_identity_provider.types.ui_customization_type.deserialize_aws_json_1_1(
                data["UICustomization"]
            )
        )
    else:
        raise DeserializationError(
            "SetUICustomizationResponse.ui_customization required"
        )
    return out


def redact_sensitive(value: SetUICustomizationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ui_customization" in value:
        import capo_cognito_identity_provider.types.ui_customization_type

        out["ui_customization"] = (
            capo_cognito_identity_provider.types.ui_customization_type.redact_sensitive(
                value["ui_customization"]
            )
        )
    return out
