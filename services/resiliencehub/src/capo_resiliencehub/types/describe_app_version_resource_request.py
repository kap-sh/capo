"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppVersionResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.aws_region
    import capo_resiliencehub.types.customer_id
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.logical_resource_id
    import capo_resiliencehub.types.string2048


class DescribeAppVersionResourceRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>Resilience Hub application version.</p>"""
    resource_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the resource.</p>"""
    logical_resource_id: NotRequired[
        "capo_resiliencehub.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>Logical identifier of the resource.</p>"""
    physical_resource_id: NotRequired["capo_resiliencehub.types.string2048.String2048"]
    """<p>Physical identifier of the resource.</p>"""
    aws_region: NotRequired["capo_resiliencehub.types.aws_region.AwsRegion"]
    """<p>Amazon Web Services region that owns the physical resource.</p>"""
    aws_account_id: NotRequired["capo_resiliencehub.types.customer_id.CustomerId"]
    """<p>Amazon Web Services account that owns the physical resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppVersionResourceRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "logical_resource_id" in value:
        import capo_resiliencehub.types.logical_resource_id

        out["logicalResourceId"] = (
            capo_resiliencehub.types.logical_resource_id.serialize_json(
                value["logical_resource_id"]
            )
        )
    if "physical_resource_id" in value:
        out["physicalResourceId"] = value["physical_resource_id"]
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    return out


def deserialize_json(data: dict) -> DescribeAppVersionResourceRequest:
    out: DescribeAppVersionResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("DescribeAppVersionResourceRequest.app_arn required")
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "DescribeAppVersionResourceRequest.app_version required"
        )
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    if data.get("logicalResourceId") is not None:
        import capo_resiliencehub.types.logical_resource_id

        out["logical_resource_id"] = (
            capo_resiliencehub.types.logical_resource_id.deserialize_json(
                data["logicalResourceId"]
            )
        )
    if data.get("physicalResourceId") is not None:
        out["physical_resource_id"] = data["physicalResourceId"]
    if data.get("awsRegion") is not None:
        out["aws_region"] = data["awsRegion"]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    return out
