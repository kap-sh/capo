"""Generated from Smithy shape ``com.amazonaws.ssm#GetAccessTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.access_request_status
    import capo_ssm.types.credentials


class GetAccessTokenResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_ssm.types.credentials.Credentials"]
    """<p>The temporary security credentials which can be used to start just-in-time node access sessions.</p>"""
    access_request_status: NotRequired[
        "capo_ssm.types.access_request_status.AccessRequestStatus"
    ]
    """<p>The status of the access request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccessTokenResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import capo_ssm.types.credentials

        out["Credentials"] = capo_ssm.types.credentials.serialize_aws_json_1_1(
            value["credentials"]
        )
    if "access_request_status" in value:
        import capo_ssm.types.access_request_status

        out["AccessRequestStatus"] = (
            capo_ssm.types.access_request_status.serialize_aws_json_1_1(
                value["access_request_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccessTokenResponse:
    out: GetAccessTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("Credentials") is not None:
        import capo_ssm.types.credentials

        out["credentials"] = capo_ssm.types.credentials.deserialize_aws_json_1_1(
            data["Credentials"]
        )
    if data.get("AccessRequestStatus") is not None:
        import capo_ssm.types.access_request_status

        out["access_request_status"] = (
            capo_ssm.types.access_request_status.deserialize_aws_json_1_1(
                data["AccessRequestStatus"]
            )
        )
    return out


def redact_sensitive(value: GetAccessTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_ssm.types.credentials

        out["credentials"] = capo_ssm.types.credentials.redact_sensitive(
            value["credentials"]
        )
    return out
