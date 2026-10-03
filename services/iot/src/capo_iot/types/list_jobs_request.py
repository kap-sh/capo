"""Generated from Smithy shape ``com.amazonaws.iot#ListJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_status
    import capo_iot.types.laser_max_results
    import capo_iot.types.namespace_id
    import capo_iot.types.next_token
    import capo_iot.types.target_selection
    import capo_iot.types.thing_group_id
    import capo_iot.types.thing_group_name


class ListJobsRequest(TypedDict, closed=True):
    status: NotRequired["capo_iot.types.job_status.JobStatus"]
    """<p>An optional filter that lets you search for jobs that have the specified status.</p>"""
    target_selection: NotRequired["capo_iot.types.target_selection.TargetSelection"]
    """<p>Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group. </p> <note> <p>We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.</p> </note>"""
    max_results: NotRequired["capo_iot.types.laser_max_results.LaserMaxResults"]
    """<p>The maximum number of results to return per request.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to retrieve the next set of results.</p>"""
    thing_group_name: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>A filter that limits the returned jobs to those for the specified group.</p>"""
    thing_group_id: NotRequired["capo_iot.types.thing_group_id.ThingGroupId"]
    """<p>A filter that limits the returned jobs to those for the specified group.</p>"""
    namespace_id: NotRequired["capo_iot.types.namespace_id.NamespaceId"]
    """<p>The namespace used to indicate that a job is a customer-managed job.</p> <p>When you specify a value for this parameter, Amazon Web Services IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.</p> <p> <code>$aws/things/<i>THING_NAME</i>/jobs/<i>JOB_ID</i>/notify-namespace-<i>NAMESPACE_ID</i>/</code> </p> <note> <p>The <code>namespaceId</code> feature is only supported by IoT Greengrass at this time. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html">Setting up IoT Greengrass core devices.</a> </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobsRequest:
    out: ListJobsRequest = {}  # type: ignore[typeddict-item]
    return out
