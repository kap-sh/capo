"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.arn
    import capo_backup.types.backup_job_state
    import capo_backup.types.backup_vault_name
    import capo_backup.types.max_results
    import capo_backup.types.resource_type
    import capo_backup.types.string
    import capo_backup.types.timestamp


class ListBackupJobsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p>"""
    by_resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>Returns only backup jobs that match the specified resource Amazon Resource Name (ARN).</p>"""
    by_state: NotRequired["capo_backup.types.backup_job_state.BackupJobState"]
    """<p>Returns only backup jobs that are in the specified state.</p> <p> <code>Completed with issues</code> is a status found only in the Backup console. For API, this status refers to jobs with a state of <code>COMPLETED</code> and a <code>MessageCategory</code> with a value other than <code>SUCCESS</code>; that is, the status is completed but comes with a status message.</p> <p>To obtain the job count for <code>Completed with issues</code>, run two GET requests, and subtract the second, smaller number:</p> <p>GET /backup-jobs/?state=COMPLETED</p> <p>GET /backup-jobs/?messageCategory=SUCCESS&state=COMPLETED</p>"""
    by_backup_vault_name: NotRequired[
        "capo_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>Returns only backup jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    by_created_before: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only backup jobs that were created before the specified date.</p>"""
    by_created_after: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only backup jobs that were created after the specified date.</p>"""
    by_resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>Returns only backup jobs for the specified resources:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>"""
    by_account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.</p> <p>If used from an Organizations management account, passing <code>*</code> returns all jobs across the organization.</p>"""
    by_complete_after: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only backup jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).</p>"""
    by_complete_before: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).</p>"""
    by_parent_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>This is a filter to list child (nested) jobs based on parent job ID.</p>"""
    by_message_category: NotRequired["capo_backup.types.string.string"]
    """<p>This is an optional parameter that can be used to filter out jobs with a MessageCategory which matches the value you input.</p> <p>Example strings may include <code>AccessDenied</code>, <code>SUCCESS</code>, <code>AGGREGATE_ALL</code>, and <code>InvalidParameters</code>.</p> <p>View <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> </p> <p>The wildcard () returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBackupJobsInput:
    out: ListBackupJobsInput = {}  # type: ignore[typeddict-item]
    return out
