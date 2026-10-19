"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StopTestRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_id
    import capo_resiliencehubv2.types.test_run_status


class StopTestRunResponse(TypedDict, closed=True):
    test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId"
    """<p>The identifier of the stopped test run.</p>"""
    status: "capo_resiliencehubv2.types.test_run_status.TestRunStatus"
    """<p>The status of the test run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopTestRunResponse) -> dict:
    out: dict = {}
    out["testRunId"] = value["test_run_id"]
    import capo_resiliencehubv2.types.test_run_status

    out["status"] = capo_resiliencehubv2.types.test_run_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> StopTestRunResponse:
    out: StopTestRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("testRunId") is not None:
        out["test_run_id"] = data["testRunId"]
    else:
        out["test_run_id"] = ""
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.test_run_status

        out["status"] = capo_resiliencehubv2.types.test_run_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehubv2.types.test_run_status.TestRunStatus", ""
        )
    return out
