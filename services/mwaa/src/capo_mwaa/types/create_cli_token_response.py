"""Generated from Smithy shape ``com.amazonaws.mwaa#CreateCliTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.hostname
    import capo_mwaa.types.token


class CreateCliTokenResponse(TypedDict, closed=True):
    cli_token: NotRequired["capo_mwaa.types.token.Token"]
    """<p>An Airflow CLI login token.</p>"""
    web_server_hostname: NotRequired["capo_mwaa.types.hostname.Hostname"]
    """<p>The Airflow web server hostname for the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCliTokenResponse) -> dict:
    out: dict = {}
    if "cli_token" in value:
        out["CliToken"] = value["cli_token"]
    if "web_server_hostname" in value:
        out["WebServerHostname"] = value["web_server_hostname"]
    return out


def deserialize_json(data: dict) -> CreateCliTokenResponse:
    out: CreateCliTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("CliToken") is not None:
        out["cli_token"] = data["CliToken"]
    if data.get("WebServerHostname") is not None:
        out["web_server_hostname"] = data["WebServerHostname"]
    return out


def redact_sensitive(value: CreateCliTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cli_token" in value:
        out["cli_token"] = "*** Sensitive Data Redacted ***"
    return out
