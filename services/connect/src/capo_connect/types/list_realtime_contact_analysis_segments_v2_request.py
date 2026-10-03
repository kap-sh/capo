"""Generated from Smithy shape ``com.amazonaws.connect#ListRealtimeContactAnalysisSegmentsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.large_next_token
    import capo_connect.types.max_result100
    import capo_connect.types.real_time_contact_analysis_output_type
    import capo_connect.types.real_time_contact_analysis_segment_types


class ListRealtimeContactAnalysisSegmentsV2Request(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    output_type: "capo_connect.types.real_time_contact_analysis_output_type.RealTimeContactAnalysisOutputType"
    """<p>The Contact Lens output type to be returned.</p>"""
    segment_types: "capo_connect.types.real_time_contact_analysis_segment_types.RealTimeContactAnalysisSegmentTypes"
    """<p>Enum with segment types . Each value corresponds to a segment type returned in the segments list of the API. Each segment type has its own structure. Different channels may have different sets of supported segment types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRealtimeContactAnalysisSegmentsV2Request) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_connect.types.real_time_contact_analysis_output_type

    out["OutputType"] = (
        capo_connect.types.real_time_contact_analysis_output_type.serialize_json(
            value["output_type"]
        )
    )
    import capo_connect.types.real_time_contact_analysis_segment_types

    out["SegmentTypes"] = (
        capo_connect.types.real_time_contact_analysis_segment_types.serialize_json(
            value["segment_types"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListRealtimeContactAnalysisSegmentsV2Request:
    out: ListRealtimeContactAnalysisSegmentsV2Request = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("OutputType") is not None:
        import capo_connect.types.real_time_contact_analysis_output_type

        out["output_type"] = (
            capo_connect.types.real_time_contact_analysis_output_type.deserialize_json(
                data["OutputType"]
            )
        )
    else:
        raise DeserializationError(
            "ListRealtimeContactAnalysisSegmentsV2Request.output_type required"
        )
    if data.get("SegmentTypes") is not None:
        import capo_connect.types.real_time_contact_analysis_segment_types

        out["segment_types"] = (
            capo_connect.types.real_time_contact_analysis_segment_types.deserialize_json(
                data["SegmentTypes"]
            )
        )
    else:
        raise DeserializationError(
            "ListRealtimeContactAnalysisSegmentsV2Request.segment_types required"
        )
    return out
