"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.express_gateway_service_include_list
    import capo_ecs.types.string


class DescribeExpressGatewayServiceRequest(TypedDict, closed=True):
    service_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Express service to describe. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>"""
    include: NotRequired[
        "capo_ecs.types.express_gateway_service_include_list.ExpressGatewayServiceIncludeList"
    ]
    """<p>Specifies additional information to include in the response. Valid values are <code>TAGS</code> to include resource tags associated with the Express service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExpressGatewayServiceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    if "include" in value:
        import capo_ecs.types.express_gateway_service_include_list

        out["include"] = (
            capo_ecs.types.express_gateway_service_include_list.serialize_aws_json_1_1(
                value["include"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExpressGatewayServiceRequest:
    out: DescribeExpressGatewayServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("include") is not None:
        import capo_ecs.types.express_gateway_service_include_list

        out["include"] = (
            capo_ecs.types.express_gateway_service_include_list.deserialize_aws_json_1_1(
                data["include"]
            )
        )
    return out
