"""Generated from Smithy shape ``com.amazonaws.codepipeline#PollForThirdPartyJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_type_id
    import capo_codepipeline.types.max_batch_size


class PollForThirdPartyJobsInput(TypedDict, closed=True):
    action_type_id: "capo_codepipeline.types.action_type_id.ActionTypeId"
    """<p>Represents information about an action type.</p>"""
    max_batch_size: NotRequired["capo_codepipeline.types.max_batch_size.MaxBatchSize"]
    """<p>The maximum number of jobs to return in a poll for jobs call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollForThirdPartyJobsInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type_id

    out["actionTypeId"] = capo_codepipeline.types.action_type_id.serialize_aws_json_1_1(
        value["action_type_id"]
    )
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PollForThirdPartyJobsInput:
    out: PollForThirdPartyJobsInput = {}  # type: ignore[typeddict-item]
    if data.get("actionTypeId") is not None:
        import capo_codepipeline.types.action_type_id

        out["action_type_id"] = (
            capo_codepipeline.types.action_type_id.deserialize_aws_json_1_1(
                data["actionTypeId"]
            )
        )
    else:
        raise DeserializationError("PollForThirdPartyJobsInput.action_type_id required")
    if data.get("maxBatchSize") is not None:
        out["max_batch_size"] = data["maxBatchSize"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PollForThirdPartyJobsInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type_id

    out["actionTypeId"] = capo_codepipeline.types.action_type_id.serialize_cbor(
        value["action_type_id"]
    )
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    return out


def deserialize_cbor(data: dict) -> PollForThirdPartyJobsInput:
    out: PollForThirdPartyJobsInput = {}  # type: ignore[typeddict-item]
    if data.get("actionTypeId") is not None:
        import capo_codepipeline.types.action_type_id

        out["action_type_id"] = capo_codepipeline.types.action_type_id.deserialize_cbor(
            data["actionTypeId"]
        )
    else:
        raise DeserializationError("PollForThirdPartyJobsInput.action_type_id required")
    if data.get("maxBatchSize") is not None:
        out["max_batch_size"] = data["maxBatchSize"]
    return out
