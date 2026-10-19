"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationAuthenticationMethodsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.token


class ListApplicationAuthenticationMethodsRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the authentication methods you want to list.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationAuthenticationMethodsRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationAuthenticationMethodsRequest:
    out: ListApplicationAuthenticationMethodsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
