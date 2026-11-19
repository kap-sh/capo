"""Generated from Smithy shape ``com.amazonaws.codepipeline#PollForJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_type_id
    import capo_codepipeline.types.max_batch_size
    import capo_codepipeline.types.query_param_map


class PollForJobsInput(TypedDict, closed=True):
    action_type_id: "capo_codepipeline.types.action_type_id.ActionTypeId"
    """<p>Represents information about an action type.</p>"""
    max_batch_size: NotRequired["capo_codepipeline.types.max_batch_size.MaxBatchSize"]
    """<p>The maximum number of jobs to return in a poll for jobs call.</p>"""
    query_param: NotRequired["capo_codepipeline.types.query_param_map.QueryParamMap"]
    """<p>A map of property names and values. For an action type with no queryable properties, this value must be null or an empty map. For an action type with a queryable property, you must supply that property as a key in the map. Only jobs whose action configuration matches the mapped value are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollForJobsInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type_id

    out["actionTypeId"] = capo_codepipeline.types.action_type_id.serialize_aws_json_1_1(
        value["action_type_id"]
    )
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    if "query_param" in value:
        import capo_codepipeline.types.query_param_map

        out["queryParam"] = (
            capo_codepipeline.types.query_param_map.serialize_aws_json_1_1(
                value["query_param"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PollForJobsInput:
    out: PollForJobsInput = {}  # type: ignore[typeddict-item]
    if data.get("actionTypeId") is not None:
        import capo_codepipeline.types.action_type_id

        out["action_type_id"] = (
            capo_codepipeline.types.action_type_id.deserialize_aws_json_1_1(
                data["actionTypeId"]
            )
        )
    else:
        raise DeserializationError("PollForJobsInput.action_type_id required")
    if data.get("maxBatchSize") is not None:
        out["max_batch_size"] = data["maxBatchSize"]
    if data.get("queryParam") is not None:
        import capo_codepipeline.types.query_param_map

        out["query_param"] = (
            capo_codepipeline.types.query_param_map.deserialize_aws_json_1_1(
                data["queryParam"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PollForJobsInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type_id

    out["actionTypeId"] = capo_codepipeline.types.action_type_id.serialize_cbor(
        value["action_type_id"]
    )
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    if "query_param" in value:
        import capo_codepipeline.types.query_param_map

        out["queryParam"] = capo_codepipeline.types.query_param_map.serialize_cbor(
            value["query_param"]
        )
    return out


def deserialize_cbor(data: dict) -> PollForJobsInput:
    out: PollForJobsInput = {}  # type: ignore[typeddict-item]
    if data.get("actionTypeId") is not None:
        import capo_codepipeline.types.action_type_id

        out["action_type_id"] = capo_codepipeline.types.action_type_id.deserialize_cbor(
            data["actionTypeId"]
        )
    else:
        raise DeserializationError("PollForJobsInput.action_type_id required")
    if data.get("maxBatchSize") is not None:
        out["max_batch_size"] = data["maxBatchSize"]
    if data.get("queryParam") is not None:
        import capo_codepipeline.types.query_param_map

        out["query_param"] = capo_codepipeline.types.query_param_map.deserialize_cbor(
            data["queryParam"]
        )
    return out
