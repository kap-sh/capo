"""Generated from Smithy shape ``com.amazonaws.backup#ListRecoveryPointsByResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.boolean2
    import capo_backup.types.max_results
    import capo_backup.types.string


class ListRecoveryPointsByResourceInput(TypedDict, closed=True):
    resource_arn: "capo_backup.types.arn.ARN"
    """<p>An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p> <note> <p>Amazon RDS requires a value of at least 20.</p> </note>"""
    managed_by_aws_backup_only: NotRequired["capo_backup.types.boolean2.Boolean2"]
    """<p>This attribute filters recovery points based on ownership.</p> <p>If this is set to <code>TRUE</code>, the response will contain recovery points associated with the selected resources that are managed by Backup.</p> <p>If this is set to <code>FALSE</code>, the response will contain all recovery points associated with the selected resource, except for EBS snapshots copied within the same Region and account.</p> <p>Type: Boolean</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPointsByResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecoveryPointsByResourceInput:
    out: ListRecoveryPointsByResourceInput = {}  # type: ignore[typeddict-item]
    return out
