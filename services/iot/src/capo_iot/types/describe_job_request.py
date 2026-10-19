"""Generated from Smithy shape ``com.amazonaws.iot#DescribeJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.before_substitution_flag
    import capo_iot.types.job_id


class DescribeJobRequest(TypedDict, closed=True):
    job_id: "capo_iot.types.job_id.JobId"
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    before_substitution: NotRequired[
        "capo_iot.types.before_substitution_flag.BeforeSubstitutionFlag"
    ]
    """<p>Provides a view of the job document before and after the substitution parameters have been resolved with their exact values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobRequest:
    out: DescribeJobRequest = {}  # type: ignore[typeddict-item]
    return out
