"""Generated from Smithy shape ``com.amazonaws.iot#AssociateTargetsWithJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.comment
    import capo_iot.types.job_id
    import capo_iot.types.job_targets
    import capo_iot.types.namespace_id


class AssociateTargetsWithJobRequest(TypedDict, closed=True):
    targets: "capo_iot.types.job_targets.JobTargets"
    """<p>A list of thing group ARNs that define the targets of the job.</p>"""
    job_id: "capo_iot.types.job_id.JobId"
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    comment: NotRequired["capo_iot.types.comment.Comment"]
    """<p>An optional comment string describing why the job was associated with the targets.</p>"""
    namespace_id: NotRequired["capo_iot.types.namespace_id.NamespaceId"]
    """<p>The namespace used to indicate that a job is a customer-managed job.</p> <p>When you specify a value for this parameter, Amazon Web Services IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.</p> <p> <code>$aws/things/<i>THING_NAME</i>/jobs/<i>JOB_ID</i>/notify-namespace-<i>NAMESPACE_ID</i>/</code> </p> <note> <p>The <code>namespaceId</code> feature is only supported by IoT Greengrass at this time. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html">Setting up IoT Greengrass core devices.</a> </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTargetsWithJobRequest) -> dict:
    out: dict = {}
    import capo_iot.types.job_targets

    out["targets"] = capo_iot.types.job_targets.serialize_json(value["targets"])
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> AssociateTargetsWithJobRequest:
    out: AssociateTargetsWithJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("targets") is not None:
        import capo_iot.types.job_targets

        out["targets"] = capo_iot.types.job_targets.deserialize_json(data["targets"])
    else:
        raise DeserializationError("AssociateTargetsWithJobRequest.targets required")
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    return out
