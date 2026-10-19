"""Generated from Smithy shape ``com.amazonaws.m2#RestartBatchJobIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.identifier
    import capo_m2.types.job_step_restart_marker


class RestartBatchJobIdentifier(TypedDict, closed=True):
    execution_id: "capo_m2.types.identifier.Identifier"
    """<p>The <code>executionId</code> from the <code>StartBatchJob</code> response when the job ran for the first time.</p>"""
    job_step_restart_marker: (
        "capo_m2.types.job_step_restart_marker.JobStepRestartMarker"
    )
    """<p>The step/procedure step information for a restart batch job operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestartBatchJobIdentifier) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    import capo_m2.types.job_step_restart_marker

    out["jobStepRestartMarker"] = capo_m2.types.job_step_restart_marker.serialize_json(
        value["job_step_restart_marker"]
    )
    return out


def deserialize_json(data: dict) -> RestartBatchJobIdentifier:
    out: RestartBatchJobIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("jobStepRestartMarker") is not None:
        import capo_m2.types.job_step_restart_marker

        out["job_step_restart_marker"] = (
            capo_m2.types.job_step_restart_marker.deserialize_json(
                data["jobStepRestartMarker"]
            )
        )
    else:
        raise DeserializationError(
            "RestartBatchJobIdentifier.job_step_restart_marker required"
        )
    return out
