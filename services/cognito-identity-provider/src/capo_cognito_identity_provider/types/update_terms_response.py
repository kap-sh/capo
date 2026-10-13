"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateTermsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.terms_type


class UpdateTermsResponse(TypedDict, closed=True):
    terms: NotRequired["capo_cognito_identity_provider.types.terms_type.TermsType"]
    """<p>A summary of the updates to your terms documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTermsResponse) -> dict:
    out: dict = {}
    if "terms" in value:
        import capo_cognito_identity_provider.types.terms_type

        out["Terms"] = (
            capo_cognito_identity_provider.types.terms_type.serialize_aws_json_1_1(
                value["terms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTermsResponse:
    out: UpdateTermsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Terms") is not None:
        import capo_cognito_identity_provider.types.terms_type

        out["terms"] = (
            capo_cognito_identity_provider.types.terms_type.deserialize_aws_json_1_1(
                data["Terms"]
            )
        )
    return out


def redact_sensitive(value: UpdateTermsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "terms" in value:
        import capo_cognito_identity_provider.types.terms_type

        out["terms"] = capo_cognito_identity_provider.types.terms_type.redact_sensitive(
            value["terms"]
        )
    return out
