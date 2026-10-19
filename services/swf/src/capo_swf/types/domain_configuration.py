"""Generated from Smithy shape ``com.amazonaws.swf#DomainConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.duration_in_days


class DomainConfiguration(TypedDict, closed=True):
    workflow_execution_retention_period_in_days: (
        "capo_swf.types.duration_in_days.DurationInDays"
    )
    """<p>The retention period for workflow executions in this domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainConfiguration) -> dict:
    out: dict = {}
    out["workflowExecutionRetentionPeriodInDays"] = value[
        "workflow_execution_retention_period_in_days"
    ]
    return out


def deserialize_aws_json_1_0(data: dict) -> DomainConfiguration:
    out: DomainConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("workflowExecutionRetentionPeriodInDays") is not None:
        out["workflow_execution_retention_period_in_days"] = data[
            "workflowExecutionRetentionPeriodInDays"
        ]
    else:
        out["workflow_execution_retention_period_in_days"] = ""
    return out
