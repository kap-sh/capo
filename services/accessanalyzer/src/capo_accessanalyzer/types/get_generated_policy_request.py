"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetGeneratedPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.job_id


class GetGeneratedPolicyRequest(TypedDict, closed=True):
    job_id: "capo_accessanalyzer.types.job_id.JobId"
    """<p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>"""
    include_resource_placeholders: NotRequired["bool"]
    """<p>The level of detail that you want to generate. You can specify whether to generate policies with placeholders for resource ARNs for actions that support resource level granularity in policies.</p> <p>For example, in the resource section of a policy, you can receive a placeholder such as <code>"Resource":"arn:aws:s3:::${BucketName}"</code> instead of <code>"*"</code>.</p>"""
    include_service_level_template: NotRequired["bool"]
    """<p>The level of detail that you want to generate. You can specify whether to generate service-level policies. </p> <p>IAM Access Analyzer uses <code>iam:servicelastaccessed</code> to identify services that have been used recently to create this service-level template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGeneratedPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGeneratedPolicyRequest:
    out: GetGeneratedPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
