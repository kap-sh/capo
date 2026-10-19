"""Generated from Smithy shape ``com.amazonaws.transfer#TestIdentityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.message
    import capo_transfer.types.response
    import capo_transfer.types.status_code
    import capo_transfer.types.url


class TestIdentityProviderResponse(TypedDict, closed=True):
    response: NotRequired["capo_transfer.types.response.Response"]
    """<p>The response that is returned from your API Gateway or your Lambda function.</p>"""
    status_code: "capo_transfer.types.status_code.StatusCode"
    """<p>The HTTP status code that is the response from your API Gateway or your Lambda function.</p>"""
    message: NotRequired["capo_transfer.types.message.Message"]
    """<p>A message that indicates whether the test was successful or not.</p> <note> <p>If an empty string is returned, the most likely cause is that the authentication failed due to an incorrect username or password.</p> </note>"""
    url: "capo_transfer.types.url.Url"
    """<p>The endpoint of the service used to authenticate a user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestIdentityProviderResponse) -> dict:
    out: dict = {}
    if "response" in value:
        out["Response"] = value["response"]
    out["StatusCode"] = value.get("status_code", 0)
    if "message" in value:
        out["Message"] = value["message"]
    out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestIdentityProviderResponse:
    out: TestIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("Response") is not None:
        out["response"] = data["Response"]
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    else:
        out["status_code"] = 0
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    return out
