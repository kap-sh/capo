"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateServicePrincipalNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.client_token
    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.directory_registration_arn


class CreateServicePrincipalNameRequest(TypedDict, closed=True):
    directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>"""
    connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn"
    """<p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>"""
    client_token: NotRequired["capo_pca_connector_ad.types.client_token.ClientToken"]
    """<p>Idempotency token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServicePrincipalNameRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateServicePrincipalNameRequest:
    out: CreateServicePrincipalNameRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
