"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_config_name
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.endpoint_status
    import capo_sagemaker.types.failure_reason


class EndpointMetadata(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint.</p>"""
    endpoint_config_name: NotRequired[
        "capo_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The name of the endpoint configuration.</p>"""
    endpoint_status: NotRequired["capo_sagemaker.types.endpoint_status.EndpointStatus"]
    """<p> The status of the endpoint. For possible values of the status of an endpoint, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EndpointSummary.html">EndpointSummary</a>. </p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p> If the status of the endpoint is <code>Failed</code>, or the status is <code>InService</code> but update operation fails, this provides the reason why it failed. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointMetadata) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "endpoint_status" in value:
        import capo_sagemaker.types.endpoint_status

        out["EndpointStatus"] = (
            capo_sagemaker.types.endpoint_status.serialize_aws_json_1_1(
                value["endpoint_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointMetadata:
    out: EndpointMetadata = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("EndpointConfigName") is not None:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if data.get("EndpointStatus") is not None:
        import capo_sagemaker.types.endpoint_status

        out["endpoint_status"] = (
            capo_sagemaker.types.endpoint_status.deserialize_aws_json_1_1(
                data["EndpointStatus"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    return out
