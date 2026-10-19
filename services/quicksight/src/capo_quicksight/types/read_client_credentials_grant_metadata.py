"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadClientCredentialsGrantMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.client_credentials_source
    import capo_quicksight.types.endpoint
    import capo_quicksight.types.read_client_credentials_details


class ReadClientCredentialsGrantMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for the OAuth2 client credentials grant flow.</p>"""
    read_client_credentials_details: NotRequired[
        "capo_quicksight.types.read_client_credentials_details.ReadClientCredentialsDetails"
    ]
    """<p>The read-only client credentials configuration details.</p>"""
    client_credentials_source: NotRequired[
        "capo_quicksight.types.client_credentials_source.ClientCredentialsSource"
    ]
    """<p>The source of client credentials for the OAuth2 client credentials grant flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadClientCredentialsGrantMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    if "read_client_credentials_details" in value:
        import capo_quicksight.types.read_client_credentials_details

        out["ReadClientCredentialsDetails"] = (
            capo_quicksight.types.read_client_credentials_details.serialize_json(
                value["read_client_credentials_details"]
            )
        )
    if "client_credentials_source" in value:
        import capo_quicksight.types.client_credentials_source

        out["ClientCredentialsSource"] = (
            capo_quicksight.types.client_credentials_source.serialize_json(
                value["client_credentials_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReadClientCredentialsGrantMetadata:
    out: ReadClientCredentialsGrantMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        out["base_endpoint"] = ""
    if data.get("ReadClientCredentialsDetails") is not None:
        import capo_quicksight.types.read_client_credentials_details

        out["read_client_credentials_details"] = (
            capo_quicksight.types.read_client_credentials_details.deserialize_json(
                data["ReadClientCredentialsDetails"]
            )
        )
    if data.get("ClientCredentialsSource") is not None:
        import capo_quicksight.types.client_credentials_source

        out["client_credentials_source"] = (
            capo_quicksight.types.client_credentials_source.deserialize_json(
                data["ClientCredentialsSource"]
            )
        )
    return out
