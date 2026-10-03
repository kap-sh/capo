"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateDirectoryRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.directory_registration_arn


class CreateDirectoryRegistrationResponse(TypedDict, closed=True):
    directory_registration_arn: NotRequired[
        "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDirectoryRegistrationResponse) -> dict:
    out: dict = {}
    if "directory_registration_arn" in value:
        out["DirectoryRegistrationArn"] = value["directory_registration_arn"]
    return out


def deserialize_json(data: dict) -> CreateDirectoryRegistrationResponse:
    out: CreateDirectoryRegistrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryRegistrationArn") is not None:
        out["directory_registration_arn"] = data["DirectoryRegistrationArn"]
    return out
