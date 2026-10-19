"""Generated from Smithy shape ``com.amazonaws.apprunner#ListVpcConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.next_token
    import capo_apprunner.types.vpc_connectors


class ListVpcConnectorsResponse(TypedDict, closed=True):
    vpc_connectors: "capo_apprunner.types.vpc_connectors.VpcConnectors"
    """<p>A list of information records for VPC connectors. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["capo_apprunner.types.next_token.NextToken"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVpcConnectorsResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.vpc_connectors

    out["VpcConnectors"] = capo_apprunner.types.vpc_connectors.serialize_aws_json_1_0(
        value["vpc_connectors"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVpcConnectorsResponse:
    out: ListVpcConnectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("VpcConnectors") is not None:
        import capo_apprunner.types.vpc_connectors

        out["vpc_connectors"] = (
            capo_apprunner.types.vpc_connectors.deserialize_aws_json_1_0(
                data["VpcConnectors"]
            )
        )
    else:
        out["vpc_connectors"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
