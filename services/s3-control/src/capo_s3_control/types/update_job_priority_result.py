"""Generated from Smithy shape ``com.amazonaws.s3control#UpdateJobPriorityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.job_id
    import capo_s3_control.types.job_priority


class UpdateJobPriorityResult(TypedDict, closed=True):
    job_id: "capo_s3_control.types.job_id.JobId"
    """<p>The ID for the job whose priority Amazon S3 updated.</p>"""
    priority: "capo_s3_control.types.job_priority.JobPriority"
    """<p>The new priority assigned to the specified job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateJobPriorityResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "JobId").text = str(value["job_id"])
    SubElement(el, "Priority").text = str(value.get("priority", 0))


def deserialize_xml(el: Element) -> UpdateJobPriorityResult:
    out: UpdateJobPriorityResult = {}  # type: ignore[typeddict-item]
    child_job_id = el.find("JobId")
    if child_job_id is not None:
        out["job_id"] = str(child_job_id.text or "")
    else:
        out["job_id"] = ""
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    else:
        out["priority"] = 0
    return out
