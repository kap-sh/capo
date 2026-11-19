"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRouterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_arn
    import capo_sagemaker.types.inference_router_name
    import capo_sagemaker.types.timestamp


class InferenceRouterSummary(TypedDict, closed=True):
    inference_router_name: NotRequired[
        "capo_sagemaker.types.inference_router_name.InferenceRouterName"
    ]
    """<p>The name of the inference router.</p>"""
    inference_router_arn: NotRequired[
        "capo_sagemaker.types.inference_router_arn.InferenceRouterArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference router.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the inference router was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the inference router was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRouterSummary) -> dict:
    out: dict = {}
    if "inference_router_name" in value:
        out["InferenceRouterName"] = value["inference_router_name"]
    if "inference_router_arn" in value:
        out["InferenceRouterArn"] = value["inference_router_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> InferenceRouterSummary:
    out: InferenceRouterSummary = {}  # type: ignore[typeddict-item]
    if data.get("InferenceRouterName") is not None:
        out["inference_router_name"] = data["InferenceRouterName"]
    if data.get("InferenceRouterArn") is not None:
        out["inference_router_arn"] = data["InferenceRouterArn"]
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
