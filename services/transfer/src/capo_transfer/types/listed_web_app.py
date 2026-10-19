"""Generated from Smithy shape ``com.amazonaws.transfer#ListedWebApp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.web_app_access_endpoint
    import capo_transfer.types.web_app_endpoint
    import capo_transfer.types.web_app_endpoint_type
    import capo_transfer.types.web_app_id


class ListedWebApp(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the web app.</p>"""
    web_app_id: "capo_transfer.types.web_app_id.WebAppId"
    """<p>The unique identifier for the web app.</p>"""
    access_endpoint: NotRequired[
        "capo_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
    ]
    """<p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p>"""
    web_app_endpoint: NotRequired["capo_transfer.types.web_app_endpoint.WebAppEndpoint"]
    """<p>The <code>WebAppEndpoint</code> is the unique URL for your Transfer Family web app. This is the value that you use when you configure <b>Origins</b> on CloudFront.</p>"""
    endpoint_type: NotRequired[
        "capo_transfer.types.web_app_endpoint_type.WebAppEndpointType"
    ]
    """<p>The type of endpoint hosting the web app. Valid values are <code>PUBLIC</code> for publicly accessible endpoints and <code>VPC</code> for VPC-hosted endpoints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedWebApp) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["WebAppId"] = value["web_app_id"]
    if "access_endpoint" in value:
        out["AccessEndpoint"] = value["access_endpoint"]
    if "web_app_endpoint" in value:
        out["WebAppEndpoint"] = value["web_app_endpoint"]
    if "endpoint_type" in value:
        import capo_transfer.types.web_app_endpoint_type

        out["EndpointType"] = (
            capo_transfer.types.web_app_endpoint_type.serialize_aws_json_1_1(
                value["endpoint_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedWebApp:
    out: ListedWebApp = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("WebAppId") is not None:
        out["web_app_id"] = data["WebAppId"]
    else:
        out["web_app_id"] = ""
    if data.get("AccessEndpoint") is not None:
        out["access_endpoint"] = data["AccessEndpoint"]
    if data.get("WebAppEndpoint") is not None:
        out["web_app_endpoint"] = data["WebAppEndpoint"]
    if data.get("EndpointType") is not None:
        import capo_transfer.types.web_app_endpoint_type

        out["endpoint_type"] = (
            capo_transfer.types.web_app_endpoint_type.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    return out
