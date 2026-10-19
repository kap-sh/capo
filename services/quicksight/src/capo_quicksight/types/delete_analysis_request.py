"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.recovery_window_in_days
    import capo_quicksight.types.short_restrictive_resource_id


class DeleteAnalysisRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account where you want to delete an analysis.</p>"""
    analysis_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the analysis that you're deleting.</p>"""
    recovery_window_in_days: NotRequired[
        "capo_quicksight.types.recovery_window_in_days.RecoveryWindowInDays"
    ]
    """<p>A value that specifies the number of days that Amazon Quick Sight waits before it deletes the analysis. You can't use this parameter with the <code>ForceDeleteWithoutRecovery</code> option in the same API call. The default value is 30.</p>"""
    force_delete_without_recovery: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>This option defaults to the value <code>NoForceDeleteWithoutRecovery</code>. To immediately delete the analysis, add the <code>ForceDeleteWithoutRecovery</code> option. You can't restore an analysis after it's deleted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnalysisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAnalysisRequest:
    out: DeleteAnalysisRequest = {}  # type: ignore[typeddict-item]
    return out
