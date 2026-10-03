"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelInvocationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_invocation_job_name
    import capo_bedrock.types.model_invocation_job_status
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.timestamp


class ListModelInvocationJobsRequest(TypedDict, closed=True):
    submit_time_after: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Specify a time to filter for batch inference jobs that were submitted after the time you specify.</p>"""
    submit_time_before: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Specify a time to filter for batch inference jobs that were submitted before the time you specify.</p>"""
    status_equals: NotRequired[
        "capo_bedrock.types.model_invocation_job_status.ModelInvocationJobStatus"
    ]
    """<p>Specify a status to filter for batch inference jobs whose statuses match the string you specify.</p> <p>The following statuses are possible:</p> <ul> <li> <p>Submitted – This job has been submitted to a queue for validation.</p> </li> <li> <p>Validating – This job is being validated for the requirements described in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html">Format and upload your batch inference data</a>. The criteria include the following:</p> <ul> <li> <p>Your IAM service role has access to the Amazon S3 buckets containing your files.</p> </li> <li> <p>Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesn't check if the <code>modelInput</code> value matches the request body for the model.</p> </li> <li> <p>Your files fulfill the requirements for file size and number of records. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html">Quotas for Amazon Bedrock</a>.</p> </li> </ul> </li> <li> <p>Scheduled – This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.</p> </li> <li> <p>Expired – This job timed out because it was scheduled but didn't begin before the set timeout duration. Submit a new job request.</p> </li> <li> <p>InProgress – This job has begun. You can start viewing the results in the output S3 location.</p> </li> <li> <p>Completed – This job has successfully completed. View the output files in the output S3 location.</p> </li> <li> <p>PartiallyCompleted – This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.</p> </li> <li> <p>Failed – This job has failed. Check the failure message for any further details. For further assistance, reach out to the <a href="https://console.aws.amazon.com/support/home/">Amazon Web Services Support Center</a>.</p> </li> <li> <p>Stopped – This job was stopped by a user.</p> </li> <li> <p>Stopping – This job is being stopped by a user.</p> </li> </ul>"""
    name_contains: NotRequired[
        "capo_bedrock.types.model_invocation_job_name.ModelInvocationJobName"
    ]
    """<p>Specify a string to filter for batch inference jobs whose names contain the string.</p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. If there are more results than the number that you specify, a <code>nextToken</code> value is returned. Use the <code>nextToken</code> in a request to return the next batch of results.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>If there were more results than the value you specified in the <code>maxResults</code> field in a previous <code>ListModelInvocationJobs</code> request, the response would have returned a <code>nextToken</code> value. To see the next batch of results, send the <code>nextToken</code> value in another request.</p>"""
    sort_by: NotRequired["capo_bedrock.types.sort_jobs_by.SortJobsBy"]
    """<p>An attribute by which to sort the results.</p>"""
    sort_order: NotRequired["capo_bedrock.types.sort_order.SortOrder"]
    """<p>Specifies whether to sort the results by ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelInvocationJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListModelInvocationJobsRequest:
    out: ListModelInvocationJobsRequest = {}  # type: ignore[typeddict-item]
    return out
