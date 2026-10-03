"""Generated from Smithy shape ``com.amazonaws.iot#ListJobExecutionsForThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_execution_status
    import capo_iot.types.job_id
    import capo_iot.types.laser_max_results
    import capo_iot.types.namespace_id
    import capo_iot.types.next_token
    import capo_iot.types.thing_name


class ListJobExecutionsForThingRequest(TypedDict, closed=True):
    thing_name: "capo_iot.types.thing_name.ThingName"
    """<p>The thing name.</p>"""
    status: NotRequired["capo_iot.types.job_execution_status.JobExecutionStatus"]
    """<p>An optional filter that lets you search for jobs that have the specified status.</p>"""
    namespace_id: NotRequired["capo_iot.types.namespace_id.NamespaceId"]
    """<p>The namespace used to indicate that a job is a customer-managed job.</p> <p>When you specify a value for this parameter, Amazon Web Services IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.</p> <p> <code>$aws/things/<i>THING_NAME</i>/jobs/<i>JOB_ID</i>/notify-namespace-<i>NAMESPACE_ID</i>/</code> </p> <note> <p>The <code>namespaceId</code> feature is only supported by IoT Greengrass at this time. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html">Setting up IoT Greengrass core devices.</a> </p> </note>"""
    max_results: NotRequired["capo_iot.types.laser_max_results.LaserMaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to retrieve the next set of results.</p>"""
    job_id: NotRequired["capo_iot.types.job_id.JobId"]
    """<p>The unique identifier you assigned to this job when it was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobExecutionsForThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobExecutionsForThingRequest:
    out: ListJobExecutionsForThingRequest = {}  # type: ignore[typeddict-item]
    return out
