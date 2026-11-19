"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.succeeded_in_stage_filter


class PipelineExecutionFilter(TypedDict, closed=True):
    succeeded_in_stage: NotRequired[
        "capo_codepipeline.types.succeeded_in_stage_filter.SucceededInStageFilter"
    ]
    """<p>Filter for pipeline executions where the stage was successful in the current pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionFilter) -> dict:
    out: dict = {}
    if "succeeded_in_stage" in value:
        import capo_codepipeline.types.succeeded_in_stage_filter

        out["succeededInStage"] = (
            capo_codepipeline.types.succeeded_in_stage_filter.serialize_aws_json_1_1(
                value["succeeded_in_stage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionFilter:
    out: PipelineExecutionFilter = {}  # type: ignore[typeddict-item]
    if data.get("succeededInStage") is not None:
        import capo_codepipeline.types.succeeded_in_stage_filter

        out["succeeded_in_stage"] = (
            capo_codepipeline.types.succeeded_in_stage_filter.deserialize_aws_json_1_1(
                data["succeededInStage"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineExecutionFilter) -> dict:
    out: dict = {}
    if "succeeded_in_stage" in value:
        import capo_codepipeline.types.succeeded_in_stage_filter

        out["succeededInStage"] = (
            capo_codepipeline.types.succeeded_in_stage_filter.serialize_cbor(
                value["succeeded_in_stage"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PipelineExecutionFilter:
    out: PipelineExecutionFilter = {}  # type: ignore[typeddict-item]
    if data.get("succeededInStage") is not None:
        import capo_codepipeline.types.succeeded_in_stage_filter

        out["succeeded_in_stage"] = (
            capo_codepipeline.types.succeeded_in_stage_filter.deserialize_cbor(
                data["succeededInStage"]
            )
        )
    return out
