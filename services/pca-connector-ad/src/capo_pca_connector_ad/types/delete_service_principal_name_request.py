"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DeleteServicePrincipalNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.directory_registration_arn


class DeleteServicePrincipalNameRequest(TypedDict, closed=True):
    directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>"""
    connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn"
    """<p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServicePrincipalNameRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServicePrincipalNameRequest:
    out: DeleteServicePrincipalNameRequest = {}  # type: ignore[typeddict-item]
    return out
