"""Generated from Smithy shape ``com.amazonaws.quicksight#ClientCredentialsGrantMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.client_credentials_details
    import capo_quicksight.types.client_credentials_source
    import capo_quicksight.types.endpoint


class ClientCredentialsGrantMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for the external service.</p>"""
    client_credentials_source: NotRequired[
        "capo_quicksight.types.client_credentials_source.ClientCredentialsSource"
    ]
    """<p>The source of the client credentials configuration.</p>"""
    client_credentials_details: NotRequired[
        "capo_quicksight.types.client_credentials_details.ClientCredentialsDetails"
    ]
    """<p>The detailed client credentials configuration including client ID, client secret, and token endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientCredentialsGrantMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    if "client_credentials_source" in value:
        import capo_quicksight.types.client_credentials_source

        out["ClientCredentialsSource"] = (
            capo_quicksight.types.client_credentials_source.serialize_json(
                value["client_credentials_source"]
            )
        )
    if "client_credentials_details" in value:
        import capo_quicksight.types.client_credentials_details

        out["ClientCredentialsDetails"] = (
            capo_quicksight.types.client_credentials_details.serialize_json(
                value["client_credentials_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClientCredentialsGrantMetadata:
    out: ClientCredentialsGrantMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        out["base_endpoint"] = ""
    if data.get("ClientCredentialsSource") is not None:
        import capo_quicksight.types.client_credentials_source

        out["client_credentials_source"] = (
            capo_quicksight.types.client_credentials_source.deserialize_json(
                data["ClientCredentialsSource"]
            )
        )
    if data.get("ClientCredentialsDetails") is not None:
        import capo_quicksight.types.client_credentials_details

        out["client_credentials_details"] = (
            capo_quicksight.types.client_credentials_details.deserialize_json(
                data["ClientCredentialsDetails"]
            )
        )
    return out


def redact_sensitive(value: ClientCredentialsGrantMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_credentials_details" in value:
        import capo_quicksight.types.client_credentials_details

        out["client_credentials_details"] = (
            capo_quicksight.types.client_credentials_details.redact_sensitive(
                value["client_credentials_details"]
            )
        )
    return out
