"""Generated from Smithy shape ``com.amazonaws.codepipeline#FailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.execution_id
    import capo_codepipeline.types.failure_type
    import capo_codepipeline.types.message


class FailureDetails(TypedDict, closed=True):
    type: "capo_codepipeline.types.failure_type.FailureType"
    """<p>The type of the failure.</p>"""
    message: "capo_codepipeline.types.message.Message"
    """<p>The message about the failure.</p>"""
    external_execution_id: NotRequired[
        "capo_codepipeline.types.execution_id.ExecutionId"
    ]
    """<p>The external ID of the run of the action that failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureDetails) -> dict:
    out: dict = {}
    import capo_codepipeline.types.failure_type

    out["type"] = capo_codepipeline.types.failure_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["message"] = value["message"]
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureDetails:
    out: FailureDetails = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codepipeline.types.failure_type

        out["type"] = capo_codepipeline.types.failure_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_codepipeline.types.failure_type.FailureType", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("externalExecutionId") is not None:
        out["external_execution_id"] = data["externalExecutionId"]
    return out
