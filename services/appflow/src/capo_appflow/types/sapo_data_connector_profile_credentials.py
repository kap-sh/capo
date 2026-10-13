"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.basic_auth_credentials
    import capo_appflow.types.o_auth_credentials


class SAPODataConnectorProfileCredentials(TypedDict, closed=True):
    basic_auth_credentials: NotRequired[
        "capo_appflow.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p> The SAPOData basic authentication credentials. </p>"""
    o_auth_credentials: NotRequired[
        "capo_appflow.types.o_auth_credentials.OAuthCredentials"
    ]
    """<p> The SAPOData OAuth type authentication credentials. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataConnectorProfileCredentials) -> dict:
    out: dict = {}
    if "basic_auth_credentials" in value:
        import capo_appflow.types.basic_auth_credentials

        out["basicAuthCredentials"] = (
            capo_appflow.types.basic_auth_credentials.serialize_json(
                value["basic_auth_credentials"]
            )
        )
    if "o_auth_credentials" in value:
        import capo_appflow.types.o_auth_credentials

        out["oAuthCredentials"] = capo_appflow.types.o_auth_credentials.serialize_json(
            value["o_auth_credentials"]
        )
    return out


def deserialize_json(data: dict) -> SAPODataConnectorProfileCredentials:
    out: SAPODataConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("basicAuthCredentials") is not None:
        import capo_appflow.types.basic_auth_credentials

        out["basic_auth_credentials"] = (
            capo_appflow.types.basic_auth_credentials.deserialize_json(
                data["basicAuthCredentials"]
            )
        )
    if data.get("oAuthCredentials") is not None:
        import capo_appflow.types.o_auth_credentials

        out["o_auth_credentials"] = (
            capo_appflow.types.o_auth_credentials.deserialize_json(
                data["oAuthCredentials"]
            )
        )
    return out


def redact_sensitive(value: SAPODataConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "basic_auth_credentials" in value:
        import capo_appflow.types.basic_auth_credentials

        out["basic_auth_credentials"] = (
            capo_appflow.types.basic_auth_credentials.redact_sensitive(
                value["basic_auth_credentials"]
            )
        )
    if "o_auth_credentials" in value:
        import capo_appflow.types.o_auth_credentials

        out["o_auth_credentials"] = (
            capo_appflow.types.o_auth_credentials.redact_sensitive(
                value["o_auth_credentials"]
            )
        )
    return out
