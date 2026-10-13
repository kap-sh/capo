"""Generated from Smithy shape ``com.amazonaws.cleanrooms#StartProtectedJobOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job


class StartProtectedJobOutput(TypedDict, closed=True):
    protected_job: "capo_cleanrooms.types.protected_job.ProtectedJob"
    """<p> The protected job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProtectedJobOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_job

    out["protectedJob"] = capo_cleanrooms.types.protected_job.serialize_json(
        value["protected_job"]
    )
    return out


def deserialize_json(data: dict) -> StartProtectedJobOutput:
    out: StartProtectedJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("protectedJob") is not None:
        import capo_cleanrooms.types.protected_job

        out["protected_job"] = capo_cleanrooms.types.protected_job.deserialize_json(
            data["protectedJob"]
        )
    else:
        raise DeserializationError("StartProtectedJobOutput.protected_job required")
    return out


def redact_sensitive(value: StartProtectedJobOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "protected_job" in value:
        import capo_cleanrooms.types.protected_job

        out["protected_job"] = capo_cleanrooms.types.protected_job.redact_sensitive(
            value["protected_job"]
        )
    return out
