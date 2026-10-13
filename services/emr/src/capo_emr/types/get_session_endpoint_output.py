"""Generated from Smithy shape ``com.amazonaws.emr#GetSessionEndpointOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.credentials
    import capo_emr.types.date
    import capo_emr.types.sensitive_string
    import capo_emr.types.xml_string


class GetSessionEndpointOutput(TypedDict, closed=True):
    endpoint: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The Spark Connect endpoint URL to use in the PySpark client.</p>"""
    auth_token: NotRequired["capo_emr.types.sensitive_string.SensitiveString"]
    """<p>A time-limited authentication token used to connect to the Spark Connect endpoint.</p>"""
    auth_token_expiration_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The time at which the authentication token expires. After this time, call <code>GetSessionEndpoint</code> again to obtain a new token.</p>"""
    credentials: NotRequired["capo_emr.types.credentials.Credentials"]
    """<p>Username and password used to authenticate with the Spark Connect server when connecting directly over VPC peering.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointOutput) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "auth_token" in value:
        out["AuthToken"] = value["auth_token"]
    if "auth_token_expiration_time" in value:
        import capo_emr.types.date

        out["AuthTokenExpirationTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["auth_token_expiration_time"]
        )
    if "credentials" in value:
        import capo_emr.types.credentials

        out["Credentials"] = capo_emr.types.credentials.serialize_aws_json_1_1(
            value["credentials"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointOutput:
    out: GetSessionEndpointOutput = {}  # type: ignore[typeddict-item]
    if data.get("Endpoint") is not None:
        out["endpoint"] = data["Endpoint"]
    if data.get("AuthToken") is not None:
        out["auth_token"] = data["AuthToken"]
    if data.get("AuthTokenExpirationTime") is not None:
        import capo_emr.types.date

        out["auth_token_expiration_time"] = (
            capo_emr.types.date.deserialize_aws_json_1_1(
                data["AuthTokenExpirationTime"]
            )
        )
    if data.get("Credentials") is not None:
        import capo_emr.types.credentials

        out["credentials"] = capo_emr.types.credentials.deserialize_aws_json_1_1(
            data["Credentials"]
        )
    return out


def redact_sensitive(value: GetSessionEndpointOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_token" in value:
        out["auth_token"] = "*** Sensitive Data Redacted ***"
    if "credentials" in value:
        import capo_emr.types.credentials

        out["credentials"] = capo_emr.types.credentials.redact_sensitive(
            value["credentials"]
        )
    return out
