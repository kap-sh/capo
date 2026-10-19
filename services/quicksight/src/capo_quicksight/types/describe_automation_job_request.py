"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAutomationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.automate_id
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean


class DescribeAutomationJobRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the automation job.</p>"""
    automation_group_id: "capo_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation group that contains the automation.</p>"""
    automation_id: "capo_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation that the job belongs to.</p>"""
    include_input_payload: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>A Boolean value that indicates whether to include the input payload in the response. If set to <code>true</code>, the input payload will be included. If set to <code>false</code>, the input payload will be returned as <code>null</code>.</p>"""
    include_output_payload: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>A Boolean value that indicates whether to include the output payload in the response. If set to <code>true</code>, the output payload will be included. If set to <code>false</code>, the output payload will be returned as <code>null</code>.</p>"""
    job_id: "capo_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation job to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAutomationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAutomationJobRequest:
    out: DescribeAutomationJobRequest = {}  # type: ignore[typeddict-item]
    return out
