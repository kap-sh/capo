"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.application_id


class CreateApplicationResponse(TypedDict, closed=True):
    application_id: "capo_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the created application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    return out
