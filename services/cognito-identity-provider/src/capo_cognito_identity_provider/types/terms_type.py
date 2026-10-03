"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.links_type
    import capo_cognito_identity_provider.types.terms_enforcement_type
    import capo_cognito_identity_provider.types.terms_id_type
    import capo_cognito_identity_provider.types.terms_name_type
    import capo_cognito_identity_provider.types.terms_source_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class TermsType(TypedDict, closed=True):
    terms_id: "capo_cognito_identity_provider.types.terms_id_type.TermsIdType"
    """<p>The ID of the terms documents.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the terms documents.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that the terms documents are assigned to.</p>"""
    terms_name: "capo_cognito_identity_provider.types.terms_name_type.TermsNameType"
    """<p>The type and friendly name of the terms documents.</p>"""
    terms_source: (
        "capo_cognito_identity_provider.types.terms_source_type.TermsSourceType"
    )
    """<p>This parameter is reserved for future use and currently accepts one value.</p>"""
    enforcement: "capo_cognito_identity_provider.types.terms_enforcement_type.TermsEnforcementType"
    """<p>This parameter is reserved for future use and currently accepts one value.</p>"""
    links: "capo_cognito_identity_provider.types.links_type.LinksType"
    """<p>A map of URLs to languages. For each localized language that will view the requested <code>TermsName</code>, assign a URL. A selection of <code>cognito:default</code> displays for all languages that don't have a language-specific URL.</p> <p>For example, <code>"cognito:default": "https://terms.example.com", "cognito:spanish": "https://terms.example.com/es"</code>.</p>"""
    creation_date: "capo_cognito_identity_provider.types.date_type.DateType"
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    last_modified_date: "capo_cognito_identity_provider.types.date_type.DateType"
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermsType) -> dict:
    out: dict = {}
    out["TermsId"] = value["terms_id"]
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
    import capo_cognito_identity_provider.types.links_type

    out["Links"] = (
        capo_cognito_identity_provider.types.links_type.serialize_aws_json_1_1(
            value["links"]
        )
    )
    import capo_cognito_identity_provider.types.date_type

    out["CreationDate"] = (
        capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
            value["creation_date"]
        )
    )
    import capo_cognito_identity_provider.types.date_type

    out["LastModifiedDate"] = (
        capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
            value["last_modified_date"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TermsType:
    out: TermsType = {}  # type: ignore[typeddict-item]
    if data.get("TermsId") is not None:
        out["terms_id"] = data["TermsId"]
    else:
        raise DeserializationError("TermsType.terms_id required")
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("TermsType.user_pool_id required")
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("TermsType.client_id required")
    if data.get("TermsName") is not None:
        out["terms_name"] = data["TermsName"]
    else:
        raise DeserializationError("TermsType.terms_name required")
    if data.get("TermsSource") is not None:
        import capo_cognito_identity_provider.types.terms_source_type

        out["terms_source"] = (
            capo_cognito_identity_provider.types.terms_source_type.deserialize_aws_json_1_1(
                data["TermsSource"]
            )
        )
    else:
        raise DeserializationError("TermsType.terms_source required")
    if data.get("Enforcement") is not None:
        import capo_cognito_identity_provider.types.terms_enforcement_type

        out["enforcement"] = (
            capo_cognito_identity_provider.types.terms_enforcement_type.deserialize_aws_json_1_1(
                data["Enforcement"]
            )
        )
    else:
        raise DeserializationError("TermsType.enforcement required")
    if data.get("Links") is not None:
        import capo_cognito_identity_provider.types.links_type

        out["links"] = (
            capo_cognito_identity_provider.types.links_type.deserialize_aws_json_1_1(
                data["Links"]
            )
        )
    else:
        raise DeserializationError("TermsType.links required")
    if data.get("CreationDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    else:
        raise DeserializationError("TermsType.creation_date required")
    if data.get("LastModifiedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    else:
        raise DeserializationError("TermsType.last_modified_date required")
    return out
