"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUICustomizationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.ui_customization_type


class GetUICustomizationResponse(TypedDict, closed=True):
    ui_customization: (
        "capo_cognito_identity_provider.types.ui_customization_type.UICustomizationType"
    )
    """<p>Information about the classic hosted UI custom CSS and logo-image branding that you applied to the user pool or app client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUICustomizationResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.ui_customization_type

    out["UICustomization"] = (
        capo_cognito_identity_provider.types.ui_customization_type.serialize_aws_json_1_1(
            value["ui_customization"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUICustomizationResponse:
    out: GetUICustomizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("UICustomization") is not None:
        import capo_cognito_identity_provider.types.ui_customization_type

        out["ui_customization"] = (
            capo_cognito_identity_provider.types.ui_customization_type.deserialize_aws_json_1_1(
                data["UICustomization"]
            )
        )
    else:
        raise DeserializationError(
            "GetUICustomizationResponse.ui_customization required"
        )
    return out


def redact_sensitive(value: GetUICustomizationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ui_customization" in value:
        import capo_cognito_identity_provider.types.ui_customization_type

        out["ui_customization"] = (
            capo_cognito_identity_provider.types.ui_customization_type.redact_sensitive(
                value["ui_customization"]
            )
        )
    return out
