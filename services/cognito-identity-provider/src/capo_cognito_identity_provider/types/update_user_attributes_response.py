"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.code_delivery_details_list_type


class UpdateUserAttributesResponse(TypedDict, closed=True):
    code_delivery_details_list: NotRequired[
        "capo_cognito_identity_provider.types.code_delivery_details_list_type.CodeDeliveryDetailsListType"
    ]
    """<p>When the attribute-update request includes an email address or phone number attribute, Amazon Cognito sends a message to users with a code that confirms ownership of the new value that they entered. The <code>CodeDeliveryDetails</code> object is information about the delivery destination for that link or code. This behavior happens in user pools configured to automatically verify changes to those attributes. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#verifying-when-users-change-their-email-or-phone-number">Verifying when users change their email or phone number</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserAttributesResponse) -> dict:
    out: dict = {}
    if "code_delivery_details_list" in value:
        import capo_cognito_identity_provider.types.code_delivery_details_list_type

        out["CodeDeliveryDetailsList"] = (
            capo_cognito_identity_provider.types.code_delivery_details_list_type.serialize_aws_json_1_1(
                value["code_delivery_details_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserAttributesResponse:
    out: UpdateUserAttributesResponse = {}  # type: ignore[typeddict-item]
    if data.get("CodeDeliveryDetailsList") is not None:
        import capo_cognito_identity_provider.types.code_delivery_details_list_type

        out["code_delivery_details_list"] = (
            capo_cognito_identity_provider.types.code_delivery_details_list_type.deserialize_aws_json_1_1(
                data["CodeDeliveryDetailsList"]
            )
        )
    return out
