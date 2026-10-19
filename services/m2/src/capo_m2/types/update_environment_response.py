"""Generated from Smithy shape ``com.amazonaws.m2#UpdateEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier


class UpdateEnvironmentResponse(TypedDict, closed=True):
    environment_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentResponse) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentResponse:
    out: UpdateEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    return out
