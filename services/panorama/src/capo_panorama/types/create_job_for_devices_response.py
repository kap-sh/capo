"""Generated from Smithy shape ``com.amazonaws.panorama#CreateJobForDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.job_list


class CreateJobForDevicesResponse(TypedDict, closed=True):
    jobs: "capo_panorama.types.job_list.JobList"
    """<p>A list of jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobForDevicesResponse) -> dict:
    out: dict = {}
    import capo_panorama.types.job_list

    out["Jobs"] = capo_panorama.types.job_list.serialize_json(value["jobs"])
    return out


def deserialize_json(data: dict) -> CreateJobForDevicesResponse:
    out: CreateJobForDevicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Jobs") is not None:
        import capo_panorama.types.job_list

        out["jobs"] = capo_panorama.types.job_list.deserialize_json(data["Jobs"])
    else:
        out["jobs"] = []
    return out
