"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePatchesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.instance_id
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_compliance_max_results
    import capo_ssm.types.patch_orchestrator_filter_list


class DescribeInstancePatchesRequest(TypedDict, closed=True):
    instance_id: "capo_ssm.types.instance_id.InstanceId"
    """<p>The ID of the managed node whose patch state information should be retrieved.</p>"""
    filters: NotRequired[
        "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
    ]
    """<p>Each element in the array is a structure containing a key-value pair.</p> <p>Supported keys for <code>DescribeInstancePatches</code>include the following:</p> <ul> <li> <p> <b> <code>Classification</code> </b> </p> <p>Sample values: <code>Security</code> | <code>SecurityUpdates</code> </p> </li> <li> <p> <b> <code>KBId</code> </b> </p> <p>Sample values: <code>KB4480056</code> | <code>java-1.7.0-openjdk.x86_64</code> </p> </li> <li> <p> <b> <code>Severity</code> </b> </p> <p>Sample values: <code>Important</code> | <code>Medium</code> | <code>Low</code> </p> </li> <li> <p> <b> <code>State</code> </b> </p> <p>Sample values: <code>Installed</code> | <code>InstalledOther</code> | <code>InstalledPendingReboot</code> </p> <p>For lists of all <code>State</code> values, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-states.html">Patch compliance state values</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </li> </ul>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "capo_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
    ]
    """<p>The maximum number of patches to return (per page).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancePatchesRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "filters" in value:
        import capo_ssm.types.patch_orchestrator_filter_list

        out["Filters"] = (
            capo_ssm.types.patch_orchestrator_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstancePatchesRequest:
    out: DescribeInstancePatchesRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "DescribeInstancePatchesRequest.instance_id required"
        )
    if data.get("Filters") is not None:
        import capo_ssm.types.patch_orchestrator_filter_list

        out["filters"] = (
            capo_ssm.types.patch_orchestrator_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
