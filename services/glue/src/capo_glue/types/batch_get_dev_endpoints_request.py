"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDevEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dev_endpoint_names


class BatchGetDevEndpointsRequest(TypedDict, closed=True):
    dev_endpoint_names: "capo_glue.types.dev_endpoint_names.DevEndpointNames"
    """<p>The list of <code>DevEndpoint</code> names, which might be the names returned from the <code>ListDevEndpoint</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDevEndpointsRequest) -> dict:
    out: dict = {}
    import capo_glue.types.dev_endpoint_names

    out["DevEndpointNames"] = capo_glue.types.dev_endpoint_names.serialize_aws_json_1_1(
        value["dev_endpoint_names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDevEndpointsRequest:
    out: BatchGetDevEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DevEndpointNames") is not None:
        import capo_glue.types.dev_endpoint_names

        out["dev_endpoint_names"] = (
            capo_glue.types.dev_endpoint_names.deserialize_aws_json_1_1(
                data["DevEndpointNames"]
            )
        )
    else:
        out["dev_endpoint_names"] = []
    return out
