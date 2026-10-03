"""Generated from Smithy shape ``com.amazonaws.backup#ListCopyJobSummariesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.aggregation_period
    import capo_backup.types.copy_job_status
    import capo_backup.types.max_results
    import capo_backup.types.message_category
    import capo_backup.types.resource_type
    import capo_backup.types.string


class ListCopyJobSummariesInput(TypedDict, closed=True):
    account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>Returns the job count for the specified account.</p> <p>If the request is sent from a member account or an account not part of Amazon Web Services Organizations, jobs within requestor's account will be returned.</p> <p>Root, admin, and delegated administrator accounts can use the value ANY to return job counts from every account in the organization.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts from all accounts within the authenticated organization, then returns the sum.</p>"""
    state: NotRequired["capo_backup.types.copy_job_status.CopyJobStatus"]
    """<p>This parameter returns the job count for jobs with the specified state.</p> <p>The the value ANY returns count of all states.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all states and returns the sum.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>Returns the job count for the specified resource type. Use request <code>GetSupportedResourceTypes</code> to obtain strings for supported resource types.</p> <p>The the value ANY returns count of all resource types.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all resource types and returns the sum.</p> <p>The type of Amazon Web Services resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.</p>"""
    message_category: NotRequired["capo_backup.types.message_category.MessageCategory"]
    """<p>This parameter returns the job count for the specified message category.</p> <p>Example accepted strings include <code>AccessDenied</code>, <code>Success</code>, and <code>InvalidParameters</code>. See <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> for a list of accepted MessageCategory strings.</p> <p>The the value ANY returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum.</p>"""
    aggregation_period: NotRequired[
        "capo_backup.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The period for the returned results.</p> <ul> <li> <p> <code>ONE_DAY</code> - The daily job count for the prior 14 days.</p> </li> <li> <p> <code>SEVEN_DAYS</code> - The aggregated job count for the prior 7 days.</p> </li> <li> <p> <code>FOURTEEN_DAYS</code> - The aggregated job count for prior 14 days.</p> </li> </ul>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>This parameter sets the maximum number of items to be returned.</p> <p>The value is an integer. Range of accepted values is from 1 to 500.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCopyJobSummariesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCopyJobSummariesInput:
    out: ListCopyJobSummariesInput = {}  # type: ignore[typeddict-item]
    return out
