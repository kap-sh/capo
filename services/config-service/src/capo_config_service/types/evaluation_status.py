"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.resource_evaluation_status
    import capo_config_service.types.string_with_char_limit1024


class EvaluationStatus(TypedDict, closed=True):
    status: (
        "capo_config_service.types.resource_evaluation_status.ResourceEvaluationStatus"
    )
    """<p>The status of an execution. The valid values are In_Progress, Succeeded or Failed. </p>"""
    failure_reason: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>An explanation for failed execution status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationStatus) -> dict:
    out: dict = {}
    import capo_config_service.types.resource_evaluation_status

    out["Status"] = (
        capo_config_service.types.resource_evaluation_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationStatus:
    out: EvaluationStatus = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_config_service.types.resource_evaluation_status

        out["status"] = (
            capo_config_service.types.resource_evaluation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_config_service.types.resource_evaluation_status.ResourceEvaluationStatus",
            "",
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    return out
