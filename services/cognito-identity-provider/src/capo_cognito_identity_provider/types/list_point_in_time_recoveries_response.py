"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListPointInTimeRecoveriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key_type
    import capo_cognito_identity_provider.types.restoration_list_type


class ListPointInTimeRecoveriesResponse(TypedDict, closed=True):
    restorations: NotRequired[
        "capo_cognito_identity_provider.types.restoration_list_type.RestorationListType"
    ]
    """<p>A summary of each requested recovery, including its ID, status, and the point in time that it restores the user pool to.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPointInTimeRecoveriesResponse) -> dict:
    out: dict = {}
    if "restorations" in value:
        import capo_cognito_identity_provider.types.restoration_list_type

        out["Restorations"] = (
            capo_cognito_identity_provider.types.restoration_list_type.serialize_aws_json_1_1(
                value["restorations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPointInTimeRecoveriesResponse:
    out: ListPointInTimeRecoveriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Restorations") is not None:
        import capo_cognito_identity_provider.types.restoration_list_type

        out["restorations"] = (
            capo_cognito_identity_provider.types.restoration_list_type.deserialize_aws_json_1_1(
                data["Restorations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
