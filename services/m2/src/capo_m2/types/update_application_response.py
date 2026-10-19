"""Generated from Smithy shape ``com.amazonaws.m2#UpdateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.version


class UpdateApplicationResponse(TypedDict, closed=True):
    application_version: "capo_m2.types.version.Version"
    """<p>The new version of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationResponse) -> dict:
    out: dict = {}
    out["applicationVersion"] = value["application_version"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationResponse:
    out: UpdateApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationVersion") is not None:
        out["application_version"] = data["applicationVersion"]
    else:
        out["application_version"] = 0
    return out
