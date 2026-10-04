"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeTermsByClientResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.terms_type


class DescribeTermsByClientResponse(TypedDict, closed=True):
    terms: NotRequired["capo_cognito_identity_provider.types.terms_type.TermsType"]
    """<p>A summary of the requested terms documents, including a unique identifier for later changes to the terms documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTermsByClientResponse) -> dict:
    out: dict = {}
    if "terms" in value:
        import capo_cognito_identity_provider.types.terms_type

        out["Terms"] = (
            capo_cognito_identity_provider.types.terms_type.serialize_aws_json_1_1(
                value["terms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTermsByClientResponse:
    out: DescribeTermsByClientResponse = {}  # type: ignore[typeddict-item]
    if data.get("Terms") is not None:
        import capo_cognito_identity_provider.types.terms_type

        out["terms"] = (
            capo_cognito_identity_provider.types.terms_type.deserialize_aws_json_1_1(
                data["Terms"]
            )
        )
    return out
