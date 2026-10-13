"""Generated from Smithy shape ``com.amazonaws.mgn#StartTestResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.job


class StartTestResponse(TypedDict, closed=True):
    job: NotRequired["capo_mgn.types.job.Job"]
    """<p>Start Test Job response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTestResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_mgn.types.job

        out["job"] = capo_mgn.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> StartTestResponse:
    out: StartTestResponse = {}  # type: ignore[typeddict-item]
    if data.get("job") is not None:
        import capo_mgn.types.job

        out["job"] = capo_mgn.types.job.deserialize_json(data["job"])
    return out


def redact_sensitive(value: StartTestResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job" in value:
        import capo_mgn.types.job

        out["job"] = capo_mgn.types.job.redact_sensitive(value["job"])
    return out
