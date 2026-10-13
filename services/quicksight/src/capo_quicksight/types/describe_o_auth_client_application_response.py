"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeOAuthClientApplicationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.o_auth_client_application
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeOAuthClientApplicationResponse(TypedDict, closed=True):
    o_auth_client_application: NotRequired[
        "capo_quicksight.types.o_auth_client_application.OAuthClientApplication"
    ]
    """<p>The information about the OAuthClientApplication.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOAuthClientApplicationResponse) -> dict:
    out: dict = {}
    if "o_auth_client_application" in value:
        import capo_quicksight.types.o_auth_client_application

        out["OAuthClientApplication"] = (
            capo_quicksight.types.o_auth_client_application.serialize_json(
                value["o_auth_client_application"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeOAuthClientApplicationResponse:
    out: DescribeOAuthClientApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("OAuthClientApplication") is not None:
        import capo_quicksight.types.o_auth_client_application

        out["o_auth_client_application"] = (
            capo_quicksight.types.o_auth_client_application.deserialize_json(
                data["OAuthClientApplication"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeOAuthClientApplicationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "o_auth_client_application" in value:
        import capo_quicksight.types.o_auth_client_application

        out["o_auth_client_application"] = (
            capo_quicksight.types.o_auth_client_application.redact_sensitive(
                value["o_auth_client_application"]
            )
        )
    return out
