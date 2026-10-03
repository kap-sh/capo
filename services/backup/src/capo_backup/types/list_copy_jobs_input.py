"""Generated from Smithy shape ``com.amazonaws.backup#ListCopyJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.arn
    import capo_backup.types.copy_job_state
    import capo_backup.types.max_results
    import capo_backup.types.resource_type
    import capo_backup.types.string
    import capo_backup.types.timestamp


class ListCopyJobsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return MaxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token. </p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p>"""
    by_resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>Returns only copy jobs that match the specified resource Amazon Resource Name (ARN). </p>"""
    by_state: NotRequired["capo_backup.types.copy_job_state.CopyJobState"]
    """<p>Returns only copy jobs that are in the specified state.</p>"""
    by_created_before: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only copy jobs that were created before the specified date.</p>"""
    by_created_after: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only copy jobs that were created after the specified date.</p>"""
    by_resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>Returns only backup jobs for the specified resources:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>"""
    by_destination_vault_arn: NotRequired["capo_backup.types.string.string"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a source backup vault to copy from; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>. </p>"""
    by_account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>The account ID to list the jobs from. Returns only copy jobs associated with the specified account ID.</p>"""
    by_complete_before: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).</p>"""
    by_complete_after: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).</p>"""
    by_parent_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>This is a filter to list child (nested) jobs based on parent job ID.</p>"""
    by_message_category: NotRequired["capo_backup.types.string.string"]
    """<p>This is an optional parameter that can be used to filter out jobs with a MessageCategory which matches the value you input.</p> <p>Example strings may include <code>AccessDenied</code>, <code>SUCCESS</code>, <code>AGGREGATE_ALL</code>, and <code>INVALIDPARAMETERS</code>.</p> <p>View <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> for a list of accepted strings.</p> <p>The the value ANY returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum.</p>"""
    by_source_recovery_point_arn: NotRequired["capo_backup.types.string.string"]
    """<p>Filters copy jobs by the specified source recovery point ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCopyJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCopyJobsInput:
    out: ListCopyJobsInput = {}  # type: ignore[typeddict-item]
    return out
