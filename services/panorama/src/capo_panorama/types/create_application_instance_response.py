"""Generated from Smithy shape ``com.amazonaws.panorama#CreateApplicationInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.application_instance_id


class CreateApplicationInstanceResponse(TypedDict, closed=True):
    application_instance_id: (
        "capo_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>The application instance's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationInstanceResponse) -> dict:
    out: dict = {}
    out["ApplicationInstanceId"] = value["application_instance_id"]
    return out


def deserialize_json(data: dict) -> CreateApplicationInstanceResponse:
    out: CreateApplicationInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationInstanceId") is not None:
        out["application_instance_id"] = data["ApplicationInstanceId"]
    else:
        out["application_instance_id"] = ""
    return out
