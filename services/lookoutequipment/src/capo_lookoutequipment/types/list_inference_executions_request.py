"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListInferenceExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.inference_execution_status
    import capo_lookoutequipment.types.inference_scheduler_identifier
    import capo_lookoutequipment.types.max_results
    import capo_lookoutequipment.types.next_token
    import capo_lookoutequipment.types.timestamp


class ListInferenceExecutionsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p>An opaque pagination token indicating where to continue the listing of inference executions.</p>"""
    max_results: NotRequired["capo_lookoutequipment.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of inference executions to list. </p>"""
    inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    """<p>The name of the inference scheduler for the inference execution listed. </p>"""
    data_start_time_after: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The time reference in the inferenced dataset after which Amazon Lookout for Equipment started the inference execution. </p>"""
    data_end_time_before: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>The time reference in the inferenced dataset before which Amazon Lookout for Equipment stopped the inference execution. </p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.inference_execution_status.InferenceExecutionStatus"
    ]
    """<p>The status of the inference execution. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInferenceExecutionsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "data_start_time_after" in value:
        import capo_lookoutequipment.types.timestamp

        out["DataStartTimeAfter"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_start_time_after"]
            )
        )
    if "data_end_time_before" in value:
        import capo_lookoutequipment.types.timestamp

        out["DataEndTimeBefore"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_end_time_before"]
            )
        )
    if "status" in value:
        import capo_lookoutequipment.types.inference_execution_status

        out["Status"] = (
            capo_lookoutequipment.types.inference_execution_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInferenceExecutionsRequest:
    out: ListInferenceExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("InferenceSchedulerName") is not None:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        out["inference_scheduler_name"] = ""
    if data.get("DataStartTimeAfter") is not None:
        import capo_lookoutequipment.types.timestamp

        out["data_start_time_after"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataStartTimeAfter"]
            )
        )
    if data.get("DataEndTimeBefore") is not None:
        import capo_lookoutequipment.types.timestamp

        out["data_end_time_before"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataEndTimeBefore"]
            )
        )
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.inference_execution_status

        out["status"] = (
            capo_lookoutequipment.types.inference_execution_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
