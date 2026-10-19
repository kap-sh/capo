"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DescribeEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.endpoints


class DescribeEndpointsResponse(TypedDict, closed=True):
    endpoints: "capo_timestream_query.types.endpoints.Endpoints"
    """<p>An <code>Endpoints</code> object is returned when a <code>DescribeEndpoints</code> request is made.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeEndpointsResponse) -> dict:
    out: dict = {}
    import capo_timestream_query.types.endpoints

    out["Endpoints"] = capo_timestream_query.types.endpoints.serialize_aws_json_1_0(
        value["endpoints"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeEndpointsResponse:
    out: DescribeEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Endpoints") is not None:
        import capo_timestream_query.types.endpoints

        out["endpoints"] = (
            capo_timestream_query.types.endpoints.deserialize_aws_json_1_0(
                data["Endpoints"]
            )
        )
    else:
        out["endpoints"] = []
    return out
