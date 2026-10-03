"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetDirectoryRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.directory_registration_arn


class GetDirectoryRegistrationRequest(TypedDict, closed=True):
    directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectoryRegistrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDirectoryRegistrationRequest:
    out: GetDirectoryRegistrationRequest = {}  # type: ignore[typeddict-item]
    return out
