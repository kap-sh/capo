"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.application_description
    import capo_application_discovery_service.types.application_name
    import capo_application_discovery_service.types.application_wave


class CreateApplicationRequest(TypedDict, closed=True):
    name: "capo_application_discovery_service.types.application_name.ApplicationName"
    """<p>The name of the application to be created.</p>"""
    description: NotRequired[
        "capo_application_discovery_service.types.application_description.ApplicationDescription"
    ]
    """<p>The description of the application to be created.</p>"""
    wave: NotRequired[
        "capo_application_discovery_service.types.application_wave.ApplicationWave"
    ]
    """<p>The name of the migration wave of the application to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "wave" in value:
        out["wave"] = value["wave"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("wave") is not None:
        out["wave"] = data["wave"]
    return out
