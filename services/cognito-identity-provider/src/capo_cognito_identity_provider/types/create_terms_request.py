"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateTermsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.links_type
    import capo_cognito_identity_provider.types.terms_enforcement_type
    import capo_cognito_identity_provider.types.terms_name_type
    import capo_cognito_identity_provider.types.terms_source_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class CreateTermsRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to create terms documents.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client where you want to create terms documents. Must be an app client in the requested user pool.</p>"""
    terms_name: "capo_cognito_identity_provider.types.terms_name_type.TermsNameType"
    """<p>A friendly name for the document that you want to create in the current request. Must begin with <code>terms-of-use</code> or <code>privacy-policy</code> as identification of the document type. Provide URLs for both <code>terms-of-use</code> and <code>privacy-policy</code> in separate requests.</p>"""
    terms_source: (
        "capo_cognito_identity_provider.types.terms_source_type.TermsSourceType"
    )
    """<p>This parameter is reserved for future use and currently accepts only one value.</p>"""
    enforcement: "capo_cognito_identity_provider.types.terms_enforcement_type.TermsEnforcementType"
    """<p>This parameter is reserved for future use and currently accepts only one value.</p>"""
    links: NotRequired["capo_cognito_identity_provider.types.links_type.LinksType"]
    """<p>A map of URLs to languages. For each localized language that will view the requested <code>TermsName</code>, assign a URL. A selection of <code>cognito:default</code> displays for all languages that don't have a language-specific URL.</p> <p>For example, <code>"cognito:default": "https://terms.example.com", "cognito:spanish": "https://terms.example.com/es"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTermsRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    out["TermsName"] = value["terms_name"]
    import capo_cognito_identity_provider.types.terms_source_type

    out["TermsSource"] = (
        capo_cognito_identity_provider.types.terms_source_type.serialize_aws_json_1_1(
            value["terms_source"]
        )
    )
    import capo_cognito_identity_provider.types.terms_enforcement_type

    out["Enforcement"] = (
        capo_cognito_identity_provider.types.terms_enforcement_type.serialize_aws_json_1_1(
            value["enforcement"]
        )
    )
    if "links" in value:
        import capo_cognito_identity_provider.types.links_type

        out["Links"] = (
            capo_cognito_identity_provider.types.links_type.serialize_aws_json_1_1(
                value["links"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTermsRequest:
    out: CreateTermsRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("CreateTermsRequest.user_pool_id required")
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("CreateTermsRequest.client_id required")
    if data.get("TermsName") is not None:
        out["terms_name"] = data["TermsName"]
    else:
        raise DeserializationError("CreateTermsRequest.terms_name required")
    if data.get("TermsSource") is not None:
        import capo_cognito_identity_provider.types.terms_source_type

        out["terms_source"] = (
            capo_cognito_identity_provider.types.terms_source_type.deserialize_aws_json_1_1(
                data["TermsSource"]
            )
        )
    else:
        raise DeserializationError("CreateTermsRequest.terms_source required")
    if data.get("Enforcement") is not None:
        import capo_cognito_identity_provider.types.terms_enforcement_type

        out["enforcement"] = (
            capo_cognito_identity_provider.types.terms_enforcement_type.deserialize_aws_json_1_1(
                data["Enforcement"]
            )
        )
    else:
        raise DeserializationError("CreateTermsRequest.enforcement required")
    if data.get("Links") is not None:
        import capo_cognito_identity_provider.types.links_type

        out["links"] = (
            capo_cognito_identity_provider.types.links_type.deserialize_aws_json_1_1(
                data["Links"]
            )
        )
    return out
