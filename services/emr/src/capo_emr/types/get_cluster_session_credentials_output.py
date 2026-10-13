"""Generated from Smithy shape ``com.amazonaws.emr#GetClusterSessionCredentialsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.credentials
    import capo_emr.types.date


class GetClusterSessionCredentialsOutput(TypedDict, closed=True):
    credentials: NotRequired["capo_emr.types.credentials.Credentials"]
    """<p>The credentials that you can use to connect to cluster endpoints that support username and password authentication.</p>"""
    expires_at: NotRequired["capo_emr.types.date.Date"]
    """<p>The time when the credentials that are returned by the <code>GetClusterSessionCredentials</code> API expire.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetClusterSessionCredentialsOutput) -> dict:
    out: dict = {}
    if "credentials" in value:
        import capo_emr.types.credentials

        out["Credentials"] = capo_emr.types.credentials.serialize_aws_json_1_1(
            value["credentials"]
        )
    if "expires_at" in value:
        import capo_emr.types.date

        out["ExpiresAt"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["expires_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetClusterSessionCredentialsOutput:
    out: GetClusterSessionCredentialsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Credentials") is not None:
        import capo_emr.types.credentials

        out["credentials"] = capo_emr.types.credentials.deserialize_aws_json_1_1(
            data["Credentials"]
        )
    if data.get("ExpiresAt") is not None:
        import capo_emr.types.date

        out["expires_at"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["ExpiresAt"]
        )
    return out


def redact_sensitive(value: GetClusterSessionCredentialsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_emr.types.credentials

        out["credentials"] = capo_emr.types.credentials.redact_sensitive(
            value["credentials"]
        )
    return out
