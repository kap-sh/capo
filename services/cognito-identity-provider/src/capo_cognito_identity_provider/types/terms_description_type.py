"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsDescriptionType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.terms_enforcement_type
    import capo_cognito_identity_provider.types.terms_id_type
    import capo_cognito_identity_provider.types.terms_name_type


class TermsDescriptionType(TypedDict, closed=True):
    terms_id: "capo_cognito_identity_provider.types.terms_id_type.TermsIdType"
    """<p>The ID of the requested terms documents.</p>"""
    terms_name: "capo_cognito_identity_provider.types.terms_name_type.TermsNameType"
    """<p>The type and friendly name of the requested terms documents.</p>"""
    enforcement: "capo_cognito_identity_provider.types.terms_enforcement_type.TermsEnforcementType"
    """<p>This parameter is reserved for future use and currently accepts one value.</p>"""
    creation_date: "capo_cognito_identity_provider.types.date_type.DateType"
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    last_modified_date: "capo_cognito_identity_provider.types.date_type.DateType"
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermsDescriptionType) -> dict:
    out: dict = {}
    out["TermsId"] = value["terms_id"]
    out["TermsName"] = value["terms_name"]
    import capo_cognito_identity_provider.types.terms_enforcement_type

    out["Enforcement"] = (
        capo_cognito_identity_provider.types.terms_enforcement_type.serialize_aws_json_1_1(
            value["enforcement"]
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


def deserialize_aws_json_1_1(data: dict) -> TermsDescriptionType:
    out: TermsDescriptionType = {}  # type: ignore[typeddict-item]
    if data.get("TermsId") is not None:
        out["terms_id"] = data["TermsId"]
    else:
        out["terms_id"] = ""
    if data.get("TermsName") is not None:
        out["terms_name"] = data["TermsName"]
    else:
        out["terms_name"] = ""
    if data.get("Enforcement") is not None:
        import capo_cognito_identity_provider.types.terms_enforcement_type

        out["enforcement"] = (
            capo_cognito_identity_provider.types.terms_enforcement_type.deserialize_aws_json_1_1(
                data["Enforcement"]
            )
        )
    else:
        import typing

        out["enforcement"] = typing.cast(
            "capo_cognito_identity_provider.types.terms_enforcement_type.TermsEnforcementType",
            "",
        )
    if data.get("CreationDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastModifiedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    else:
        import datetime

        out["last_modified_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
