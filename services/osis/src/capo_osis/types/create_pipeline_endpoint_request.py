"""Generated from Smithy shape ``com.amazonaws.osis#CreatePipelineEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_osis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_osis.types.pipeline_arn
    import capo_osis.types.pipeline_endpoint_vpc_options


class CreatePipelineEndpointRequest(TypedDict, closed=True):
    pipeline_arn: "capo_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the pipeline to create the endpoint for.</p>"""
    vpc_options: (
        "capo_osis.types.pipeline_endpoint_vpc_options.PipelineEndpointVpcOptions"
    )
    """<p>Container for the VPC configuration for the pipeline endpoint, including subnet IDs and security group IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipelineEndpointRequest) -> dict:
    out: dict = {}
    out["PipelineArn"] = value["pipeline_arn"]
    import capo_osis.types.pipeline_endpoint_vpc_options

    out["VpcOptions"] = capo_osis.types.pipeline_endpoint_vpc_options.serialize_json(
        value["vpc_options"]
    )
    return out


def deserialize_json(data: dict) -> CreatePipelineEndpointRequest:
    out: CreatePipelineEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineArn") is not None:
        out["pipeline_arn"] = data["PipelineArn"]
    else:
        out["pipeline_arn"] = ""
    if data.get("VpcOptions") is not None:
        import capo_osis.types.pipeline_endpoint_vpc_options

        out["vpc_options"] = (
            capo_osis.types.pipeline_endpoint_vpc_options.deserialize_json(
                data["VpcOptions"]
            )
        )
    else:
        raise DeserializationError("CreatePipelineEndpointRequest.vpc_options required")
    return out
