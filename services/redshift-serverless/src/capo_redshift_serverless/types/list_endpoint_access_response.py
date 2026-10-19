"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListEndpointAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.endpoint_access_list


class ListEndpointAccessResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    endpoints: "capo_redshift_serverless.types.endpoint_access_list.EndpointAccessList"
    """<p>The returned VPC endpoints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointAccessResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_redshift_serverless.types.endpoint_access_list

    out["endpoints"] = (
        capo_redshift_serverless.types.endpoint_access_list.serialize_aws_json_1_1(
            value["endpoints"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointAccessResponse:
    out: ListEndpointAccessResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("endpoints") is not None:
        import capo_redshift_serverless.types.endpoint_access_list

        out["endpoints"] = (
            capo_redshift_serverless.types.endpoint_access_list.deserialize_aws_json_1_1(
                data["endpoints"]
            )
        )
    else:
        out["endpoints"] = []
    return out
