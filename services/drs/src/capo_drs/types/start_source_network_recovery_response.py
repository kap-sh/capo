"""Generated from Smithy shape ``com.amazonaws.drs#StartSourceNetworkRecoveryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.job


class StartSourceNetworkRecoveryResponse(TypedDict, closed=True):
    job: NotRequired["capo_drs.types.job.Job"]
    """<p>The Source Network recovery Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSourceNetworkRecoveryResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_drs.types.job

        out["job"] = capo_drs.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> StartSourceNetworkRecoveryResponse:
    out: StartSourceNetworkRecoveryResponse = {}  # type: ignore[typeddict-item]
    if data.get("job") is not None:
        import capo_drs.types.job

        out["job"] = capo_drs.types.job.deserialize_json(data["job"])
    return out


def redact_sensitive(value: StartSourceNetworkRecoveryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job" in value:
        import capo_drs.types.job

        out["job"] = capo_drs.types.job.redact_sensitive(value["job"])
    return out
