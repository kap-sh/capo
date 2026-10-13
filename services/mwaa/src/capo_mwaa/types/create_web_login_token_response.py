"""Generated from Smithy shape ``com.amazonaws.mwaa#CreateWebLoginTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.airflow_identity
    import capo_mwaa.types.hostname
    import capo_mwaa.types.iam_identity
    import capo_mwaa.types.token


class CreateWebLoginTokenResponse(TypedDict, closed=True):
    web_token: NotRequired["capo_mwaa.types.token.Token"]
    """<p>An Airflow web server login token.</p>"""
    web_server_hostname: NotRequired["capo_mwaa.types.hostname.Hostname"]
    """<p>The Airflow web server hostname for the environment.</p>"""
    iam_identity: NotRequired["capo_mwaa.types.iam_identity.IamIdentity"]
    """<p>The name of the IAM identity creating the web login token. This might be an IAM user, or an assumed or federated identity. For example, <code>assumed-role/Admin/your-name</code>.</p>"""
    airflow_identity: NotRequired["capo_mwaa.types.airflow_identity.AirflowIdentity"]
    """<p>The user name of the Apache Airflow identity creating the web login token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebLoginTokenResponse) -> dict:
    out: dict = {}
    if "web_token" in value:
        out["WebToken"] = value["web_token"]
    if "web_server_hostname" in value:
        out["WebServerHostname"] = value["web_server_hostname"]
    if "iam_identity" in value:
        out["IamIdentity"] = value["iam_identity"]
    if "airflow_identity" in value:
        out["AirflowIdentity"] = value["airflow_identity"]
    return out


def deserialize_json(data: dict) -> CreateWebLoginTokenResponse:
    out: CreateWebLoginTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("WebToken") is not None:
        out["web_token"] = data["WebToken"]
    if data.get("WebServerHostname") is not None:
        out["web_server_hostname"] = data["WebServerHostname"]
    if data.get("IamIdentity") is not None:
        out["iam_identity"] = data["IamIdentity"]
    if data.get("AirflowIdentity") is not None:
        out["airflow_identity"] = data["AirflowIdentity"]
    return out


def redact_sensitive(value: CreateWebLoginTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "web_token" in value:
        out["web_token"] = "*** Sensitive Data Redacted ***"
    return out
