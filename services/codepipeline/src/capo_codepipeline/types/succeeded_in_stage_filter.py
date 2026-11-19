"""Generated from Smithy shape ``com.amazonaws.codepipeline#SucceededInStageFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.stage_name


class SucceededInStageFilter(TypedDict, closed=True):
    stage_name: NotRequired["capo_codepipeline.types.stage_name.StageName"]
    """<p>The name of the stage for filtering for pipeline executions where the stage was successful in the current pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SucceededInStageFilter) -> dict:
    out: dict = {}
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SucceededInStageFilter:
    out: SucceededInStageFilter = {}  # type: ignore[typeddict-item]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SucceededInStageFilter) -> dict:
    out: dict = {}
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    return out


def deserialize_cbor(data: dict) -> SucceededInStageFilter:
    out: SucceededInStageFilter = {}  # type: ignore[typeddict-item]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    return out
