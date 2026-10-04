"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ListJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.job_operation_type
    import capo_endusermessaging.types.job_status
    import capo_endusermessaging.types.max_results
    import capo_endusermessaging.types.next_token


class ListJobsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_endusermessaging.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_endusermessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>"""
    status: NotRequired["capo_endusermessaging.types.job_status.JobStatus"]
    """<p>Filters the results to jobs that have the specified status.</p>"""
    brand_profile_id: NotRequired[
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    ]
    """<p>Filters the results to jobs for the specified brand profile.</p>"""
    operation_type: NotRequired[
        "capo_endusermessaging.types.job_operation_type.JobOperationType"
    ]
    """<p>Filters the results to jobs of the specified operation type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobsInput:
    out: ListJobsInput = {}  # type: ignore[typeddict-item]
    return out
