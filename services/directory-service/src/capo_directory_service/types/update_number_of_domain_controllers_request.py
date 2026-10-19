"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateNumberOfDomainControllersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.desired_number_of_domain_controllers
    import capo_directory_service.types.directory_id


class UpdateNumberOfDomainControllersRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the directory to which the domain controllers will be added or removed.</p>"""
    desired_number: "capo_directory_service.types.desired_number_of_domain_controllers.DesiredNumberOfDomainControllers"
    """<p>The number of domain controllers desired in the directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNumberOfDomainControllersRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["DesiredNumber"] = value["desired_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNumberOfDomainControllersRequest:
    out: UpdateNumberOfDomainControllersRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("DesiredNumber") is not None:
        out["desired_number"] = data["DesiredNumber"]
    else:
        out["desired_number"] = 0
    return out
