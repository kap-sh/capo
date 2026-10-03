"""Generated from Smithy shape ``com.amazonaws.greengrassv2#EffectiveDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_greengrassv2.types.deployment_id
    import capo_greengrassv2.types.deployment_name
    import capo_greengrassv2.types.description
    import capo_greengrassv2.types.effective_deployment_execution_status
    import capo_greengrassv2.types.effective_deployment_status_details
    import capo_greengrassv2.types.io_t_job_arn
    import capo_greengrassv2.types.io_t_job_id
    import capo_greengrassv2.types.reason
    import capo_greengrassv2.types.target_arn
    import capo_greengrassv2.types.timestamp


class EffectiveDeployment(TypedDict, closed=True):
    deployment_id: "capo_greengrassv2.types.deployment_id.DeploymentID"
    """<p>The ID of the deployment.</p>"""
    deployment_name: "capo_greengrassv2.types.deployment_name.DeploymentName"
    """<p>The name of the deployment.</p>"""
    iot_job_id: NotRequired["capo_greengrassv2.types.io_t_job_id.IoTJobId"]
    """<p>The ID of the IoT job that applies the deployment to target devices.</p>"""
    iot_job_arn: NotRequired["capo_greengrassv2.types.io_t_job_arn.IoTJobARN"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IoT job that applies the deployment to target devices.</p>"""
    description: NotRequired["capo_greengrassv2.types.description.Description"]
    """<p>The description of the deployment job.</p>"""
    target_arn: "capo_greengrassv2.types.target_arn.TargetARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the target IoT thing or thing group.</p>"""
    core_device_execution_status: "capo_greengrassv2.types.effective_deployment_execution_status.EffectiveDeploymentExecutionStatus"
    """<p>The status of the deployment job on the Greengrass core device.</p> <ul> <li> <p> <code>IN_PROGRESS</code> – The deployment job is running.</p> </li> <li> <p> <code>QUEUED</code> – The deployment job is in the job queue and waiting to run.</p> </li> <li> <p> <code>FAILED</code> – The deployment failed. For more information, see the <code>statusDetails</code> field.</p> </li> <li> <p> <code>COMPLETED</code> – The deployment to an IoT thing was completed successfully.</p> </li> <li> <p> <code>TIMED_OUT</code> – The deployment didn't complete in the allotted time. </p> </li> <li> <p> <code>CANCELED</code> – The deployment was canceled by the user.</p> </li> <li> <p> <code>REJECTED</code> – The deployment was rejected. For more information, see the <code>statusDetails</code> field.</p> </li> <li> <p> <code>SUCCEEDED</code> – The deployment to an IoT thing group was completed successfully.</p> </li> </ul>"""
    reason: NotRequired["capo_greengrassv2.types.reason.Reason"]
    """<p>The reason code for the update, if the job was updated.</p>"""
    creation_timestamp: "capo_greengrassv2.types.timestamp.Timestamp"
    """<p>The time at which the deployment was created, expressed in ISO 8601 format.</p>"""
    modified_timestamp: "capo_greengrassv2.types.timestamp.Timestamp"
    """<p>The time at which the deployment job was last modified, expressed in ISO 8601 format.</p>"""
    status_details: NotRequired[
        "capo_greengrassv2.types.effective_deployment_status_details.EffectiveDeploymentStatusDetails"
    ]
    """<p>The status details that explain why a deployment has an error. This response will be null if the deployment is in a success state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveDeployment) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    out["deploymentName"] = value["deployment_name"]
    if "iot_job_id" in value:
        out["iotJobId"] = value["iot_job_id"]
    if "iot_job_arn" in value:
        out["iotJobArn"] = value["iot_job_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["targetArn"] = value["target_arn"]
    import capo_greengrassv2.types.effective_deployment_execution_status

    out["coreDeviceExecutionStatus"] = (
        capo_greengrassv2.types.effective_deployment_execution_status.serialize_json(
            value["core_device_execution_status"]
        )
    )
    if "reason" in value:
        out["reason"] = value["reason"]
    import capo_greengrassv2.types.timestamp

    out["creationTimestamp"] = capo_greengrassv2.types.timestamp.serialize_json(
        value["creation_timestamp"]
    )
    import capo_greengrassv2.types.timestamp

    out["modifiedTimestamp"] = capo_greengrassv2.types.timestamp.serialize_json(
        value["modified_timestamp"]
    )
    if "status_details" in value:
        import capo_greengrassv2.types.effective_deployment_status_details

        out["statusDetails"] = (
            capo_greengrassv2.types.effective_deployment_status_details.serialize_json(
                value["status_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> EffectiveDeployment:
    out: EffectiveDeployment = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("EffectiveDeployment.deployment_id required")
    if data.get("deploymentName") is not None:
        out["deployment_name"] = data["deploymentName"]
    else:
        raise DeserializationError("EffectiveDeployment.deployment_name required")
    if data.get("iotJobId") is not None:
        out["iot_job_id"] = data["iotJobId"]
    if data.get("iotJobArn") is not None:
        out["iot_job_arn"] = data["iotJobArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("EffectiveDeployment.target_arn required")
    if data.get("coreDeviceExecutionStatus") is not None:
        import capo_greengrassv2.types.effective_deployment_execution_status

        out["core_device_execution_status"] = (
            capo_greengrassv2.types.effective_deployment_execution_status.deserialize_json(
                data["coreDeviceExecutionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "EffectiveDeployment.core_device_execution_status required"
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("creationTimestamp") is not None:
        import capo_greengrassv2.types.timestamp

        out["creation_timestamp"] = capo_greengrassv2.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    else:
        raise DeserializationError("EffectiveDeployment.creation_timestamp required")
    if data.get("modifiedTimestamp") is not None:
        import capo_greengrassv2.types.timestamp

        out["modified_timestamp"] = capo_greengrassv2.types.timestamp.deserialize_json(
            data["modifiedTimestamp"]
        )
    else:
        raise DeserializationError("EffectiveDeployment.modified_timestamp required")
    if data.get("statusDetails") is not None:
        import capo_greengrassv2.types.effective_deployment_status_details

        out["status_details"] = (
            capo_greengrassv2.types.effective_deployment_status_details.deserialize_json(
                data["statusDetails"]
            )
        )
    return out
