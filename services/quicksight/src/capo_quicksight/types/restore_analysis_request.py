"""Generated from Smithy shape ``com.amazonaws.quicksight#RestoreAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.short_restrictive_resource_id


class RestoreAnalysisRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the analysis.</p>"""
    analysis_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the analysis that you're restoring.</p>"""
    restore_to_folders: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>A boolean value that determines if the analysis will be restored to folders that it previously resided in. A <code>True</code> value restores analysis back to all folders that it previously resided in. A <code>False</code> value restores the analysis but does not restore the analysis back to all previously resided folders. Restoring a restricted analysis requires this parameter to be set to <code>True</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreAnalysisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestoreAnalysisRequest:
    out: RestoreAnalysisRequest = {}  # type: ignore[typeddict-item]
    return out
