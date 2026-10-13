"""Generated from Smithy shape ``com.amazonaws.drs#TerminateRecoveryInstancesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.job


class TerminateRecoveryInstancesResponse(TypedDict, closed=True):
    job: NotRequired["capo_drs.types.job.Job"]
    """<p>The Job for terminating the Recovery Instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateRecoveryInstancesResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_drs.types.job

        out["job"] = capo_drs.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> TerminateRecoveryInstancesResponse:
    out: TerminateRecoveryInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("job") is not None:
        import capo_drs.types.job

        out["job"] = capo_drs.types.job.deserialize_json(data["job"])
    return out


def redact_sensitive(value: TerminateRecoveryInstancesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job" in value:
        import capo_drs.types.job

        out["job"] = capo_drs.types.job.redact_sensitive(value["job"])
    return out
