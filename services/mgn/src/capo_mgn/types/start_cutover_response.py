"""Generated from Smithy shape ``com.amazonaws.mgn#StartCutoverResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.job


class StartCutoverResponse(TypedDict, closed=True):
    job: NotRequired["capo_mgn.types.job.Job"]
    """<p>Start Cutover Job response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCutoverResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_mgn.types.job

        out["job"] = capo_mgn.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> StartCutoverResponse:
    out: StartCutoverResponse = {}  # type: ignore[typeddict-item]
    if data.get("job") is not None:
        import capo_mgn.types.job

        out["job"] = capo_mgn.types.job.deserialize_json(data["job"])
    return out


def redact_sensitive(value: StartCutoverResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job" in value:
        import capo_mgn.types.job

        out["job"] = capo_mgn.types.job.redact_sensitive(value["job"])
    return out
