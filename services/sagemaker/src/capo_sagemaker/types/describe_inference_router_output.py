"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeInferenceRouterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_arn
    import capo_sagemaker.types.inference_router_name
    import capo_sagemaker.types.inference_router_status
    import capo_sagemaker.types.inference_router_status_reason
    import capo_sagemaker.types.routing_target_list
    import capo_sagemaker.types.timestamp


class DescribeInferenceRouterOutput(TypedDict, closed=True):
    inference_router_name: NotRequired[
        "capo_sagemaker.types.inference_router_name.InferenceRouterName"
    ]
    """<p>The name of the inference router.</p>"""
    inference_router_arn: NotRequired[
        "capo_sagemaker.types.inference_router_arn.InferenceRouterArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference router.</p>"""
    routing_targets: NotRequired[
        "capo_sagemaker.types.routing_target_list.RoutingTargetList"
    ]
    """<p>The routing targets of the inference router. Each destination includes its <code>RoutingStatus</code>. You can send these routing targets back in an <code>UpdateInferenceRouter</code> request without changes.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.inference_router_status.InferenceRouterStatus"
    ]
    """<p>The status of the inference router.</p>"""
    status_reason: NotRequired[
        "capo_sagemaker.types.inference_router_status_reason.InferenceRouterStatusReason"
    ]
    """<p>If the status is <code>Failed</code>, the reason that the inference router failed.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the inference router was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the inference router was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInferenceRouterOutput) -> dict:
    out: dict = {}
    if "inference_router_name" in value:
        out["InferenceRouterName"] = value["inference_router_name"]
    if "inference_router_arn" in value:
        out["InferenceRouterArn"] = value["inference_router_arn"]
    if "routing_targets" in value:
        import capo_sagemaker.types.routing_target_list

        out["RoutingTargets"] = (
            capo_sagemaker.types.routing_target_list.serialize_aws_json_1_1(
                value["routing_targets"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.inference_router_status

        out["Status"] = (
            capo_sagemaker.types.inference_router_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInferenceRouterOutput:
    out: DescribeInferenceRouterOutput = {}  # type: ignore[typeddict-item]
    if data.get("InferenceRouterName") is not None:
        out["inference_router_name"] = data["InferenceRouterName"]
    if data.get("InferenceRouterArn") is not None:
        out["inference_router_arn"] = data["InferenceRouterArn"]
    if data.get("RoutingTargets") is not None:
        import capo_sagemaker.types.routing_target_list

        out["routing_targets"] = (
            capo_sagemaker.types.routing_target_list.deserialize_aws_json_1_1(
                data["RoutingTargets"]
            )
        )
    if data.get("Status") is not None:
        import capo_sagemaker.types.inference_router_status

        out["status"] = (
            capo_sagemaker.types.inference_router_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
