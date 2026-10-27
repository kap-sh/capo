"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_worker_error_code
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.string
    import capo_deadline.types.worker_id


class BatchGetWorkerError(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the worker that could not be retrieved."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the worker that could not be retrieved."""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """The worker ID of the worker that could not be retrieved."""
    code: "capo_deadline.types.batch_get_worker_error_code.BatchGetWorkerErrorCode"
    """The error code."""
    message: "capo_deadline.types.string.String"
    """The error message."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerError) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    import capo_deadline.types.batch_get_worker_error_code

    out["code"] = capo_deadline.types.batch_get_worker_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetWorkerError:
    out: BatchGetWorkerError = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    if data.get("workerId") is not None:
        out["worker_id"] = data["workerId"]
    else:
        out["worker_id"] = ""
    if data.get("code") is not None:
        import capo_deadline.types.batch_get_worker_error_code

        out["code"] = capo_deadline.types.batch_get_worker_error_code.deserialize_json(
            data["code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_deadline.types.batch_get_worker_error_code.BatchGetWorkerErrorCode",
            "",
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
