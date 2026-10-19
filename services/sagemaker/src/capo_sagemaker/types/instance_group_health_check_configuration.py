"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroupHealthCheckConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.deep_health_checks
    import capo_sagemaker.types.instance_ids


class InstanceGroupHealthCheckConfiguration(TypedDict, closed=True):
    instance_group_name: (
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    )
    """<p>The name of the instance group.</p>"""
    instance_ids: NotRequired["capo_sagemaker.types.instance_ids.InstanceIds"]
    """<p>A list of Amazon Elastic Compute Cloud (EC2) instance IDs on which to perform deep health checks.</p> <note> <p>Leave this field blank to perform deep health checks on the entire instance group.</p> </note>"""
    deep_health_checks: "capo_sagemaker.types.deep_health_checks.DeepHealthChecks"
    """<p>A list of deep health checks to be performed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupHealthCheckConfiguration) -> dict:
    out: dict = {}
    out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_ids" in value:
        import capo_sagemaker.types.instance_ids

        out["InstanceIds"] = capo_sagemaker.types.instance_ids.serialize_aws_json_1_1(
            value["instance_ids"]
        )
    import capo_sagemaker.types.deep_health_checks

    out["DeepHealthChecks"] = (
        capo_sagemaker.types.deep_health_checks.serialize_aws_json_1_1(
            value["deep_health_checks"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupHealthCheckConfiguration:
    out: InstanceGroupHealthCheckConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    else:
        out["instance_group_name"] = ""
    if data.get("InstanceIds") is not None:
        import capo_sagemaker.types.instance_ids

        out["instance_ids"] = (
            capo_sagemaker.types.instance_ids.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    if data.get("DeepHealthChecks") is not None:
        import capo_sagemaker.types.deep_health_checks

        out["deep_health_checks"] = (
            capo_sagemaker.types.deep_health_checks.deserialize_aws_json_1_1(
                data["DeepHealthChecks"]
            )
        )
    else:
        out["deep_health_checks"] = []
    return out
