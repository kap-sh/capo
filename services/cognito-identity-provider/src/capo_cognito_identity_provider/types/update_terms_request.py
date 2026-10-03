"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateTermsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.links_type
    import capo_cognito_identity_provider.types.terms_enforcement_type
    import capo_cognito_identity_provider.types.terms_id_type
    import capo_cognito_identity_provider.types.terms_name_type
    import capo_cognito_identity_provider.types.terms_source_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class UpdateTermsRequest(TypedDict, closed=True):
    terms_id: "capo_cognito_identity_provider.types.terms_id_type.TermsIdType"
    """<p>The ID of the terms document that you want to update.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the terms that you want to update.</p>"""
    terms_name: NotRequired[
        "capo_cognito_identity_provider.types.terms_name_type.TermsNameType"
    ]
    """<p>The new name that you want to apply to the requested terms documents.</p>"""
    terms_source: NotRequired[
        "capo_cognito_identity_provider.types.terms_source_type.TermsSourceType"
    ]
    """<p>This parameter is reserved for future use and currently accepts only one value.</p>"""
    enforcement: NotRequired[
        "capo_cognito_identity_provider.types.terms_enforcement_type.TermsEnforcementType"
    ]
    """<p>This parameter is reserved for future use and currently accepts only one value.</p>"""
    links: NotRequired["capo_cognito_identity_provider.types.links_type.LinksType"]
    """<p>A map of URLs to languages. For each localized language that will view the requested <code>TermsName</code>, assign a URL. A selection of <code>cognito:default</code> displays for all languages that don't have a language-specific URL.</p> <p>For example, <code>"cognito:default": "https://terms.example.com", "cognito:spanish": "https://terms.example.com/es"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTermsRequest) -> dict:
    out: dict = {}
    out["TermsId"] = value["terms_id"]
    out["UserPoolId"] = value["user_pool_id"]
    if "terms_name" in value:
        out["TermsName"] = value["terms_name"]
    if "terms_source" in value:
        import capo_cognito_identity_provider.types.terms_source_type

        out["TermsSource"] = (
            capo_cognito_identity_provider.types.terms_source_type.serialize_aws_json_1_1(
                value["terms_source"]
            )
        )
    if "enforcement" in value:
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


def deserialize_aws_json_1_1(data: dict) -> UpdateTermsRequest:
    out: UpdateTermsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TermsId") is not None:
        out["terms_id"] = data["TermsId"]
    else:
        raise DeserializationError("UpdateTermsRequest.terms_id required")
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("UpdateTermsRequest.user_pool_id required")
    if data.get("TermsName") is not None:
        out["terms_name"] = data["TermsName"]
    if data.get("TermsSource") is not None:
        import capo_cognito_identity_provider.types.terms_source_type

        out["terms_source"] = (
            capo_cognito_identity_provider.types.terms_source_type.deserialize_aws_json_1_1(
                data["TermsSource"]
            )
        )
    if data.get("Enforcement") is not None:
        import capo_cognito_identity_provider.types.terms_enforcement_type

        out["enforcement"] = (
            capo_cognito_identity_provider.types.terms_enforcement_type.deserialize_aws_json_1_1(
                data["Enforcement"]
            )
        )
    if data.get("Links") is not None:
        import capo_cognito_identity_provider.types.links_type

        out["links"] = (
            capo_cognito_identity_provider.types.links_type.deserialize_aws_json_1_1(
                data["Links"]
            )
        )
    return out
