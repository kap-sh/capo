"""Generated from Smithy shape ``com.amazonaws.osis#RevokePipelineEndpointConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_arn
    import capo_osis.types.pipeline_endpoint_ids_list


class RevokePipelineEndpointConnectionsRequest(TypedDict, closed=True):
    pipeline_arn: "capo_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the pipeline from which to revoke endpoint connections.</p>"""
    endpoint_ids: "capo_osis.types.pipeline_endpoint_ids_list.PipelineEndpointIdsList"
    """<p>A list of endpoint IDs for which to revoke access to the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokePipelineEndpointConnectionsRequest) -> dict:
    out: dict = {}
    out["PipelineArn"] = value["pipeline_arn"]
    import capo_osis.types.pipeline_endpoint_ids_list

    out["EndpointIds"] = capo_osis.types.pipeline_endpoint_ids_list.serialize_json(
        value["endpoint_ids"]
    )
    return out


def deserialize_json(data: dict) -> RevokePipelineEndpointConnectionsRequest:
    out: RevokePipelineEndpointConnectionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineArn") is not None:
        out["pipeline_arn"] = data["PipelineArn"]
    else:
        out["pipeline_arn"] = ""
    if data.get("EndpointIds") is not None:
        import capo_osis.types.pipeline_endpoint_ids_list

        out["endpoint_ids"] = (
            capo_osis.types.pipeline_endpoint_ids_list.deserialize_json(
                data["EndpointIds"]
            )
        )
    else:
        out["endpoint_ids"] = []
    return out
