"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StartTestRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.experiment_arn_list
    import capo_resiliencehubv2.types.test_run_id
    import capo_resiliencehubv2.types.test_run_status


class StartTestRunResponse(TypedDict, closed=True):
    test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId"
    """<p>The identifier of the started test run.</p>"""
    status: "capo_resiliencehubv2.types.test_run_status.TestRunStatus"
    """<p>The status of the started test run.</p>"""
    experiment_arns: "capo_resiliencehubv2.types.experiment_arn_list.ExperimentArnList"
    """<p>The ARNs of the AWS Fault Injection Service (AWS FIS) experiments started for the run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTestRunResponse) -> dict:
    out: dict = {}
    out["testRunId"] = value["test_run_id"]
    import capo_resiliencehubv2.types.test_run_status

    out["status"] = capo_resiliencehubv2.types.test_run_status.serialize_json(
        value["status"]
    )
    import capo_resiliencehubv2.types.experiment_arn_list

    out["experimentArns"] = (
        capo_resiliencehubv2.types.experiment_arn_list.serialize_json(
            value["experiment_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartTestRunResponse:
    out: StartTestRunResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("experimentArns") is not None:
        import capo_resiliencehubv2.types.experiment_arn_list

        out["experiment_arns"] = (
            capo_resiliencehubv2.types.experiment_arn_list.deserialize_json(
                data["experimentArns"]
            )
        )
    else:
        out["experiment_arns"] = []
    return out
