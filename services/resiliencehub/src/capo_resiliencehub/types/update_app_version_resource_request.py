"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateAppVersionResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.additional_info_map
    import capo_resiliencehub.types.app_component_name_list
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.aws_region
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.customer_id
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.logical_resource_id
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.string2048


class UpdateAppVersionResourceRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
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
    resource_type: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Type of resource.</p>"""
    app_components: NotRequired[
        "capo_resiliencehub.types.app_component_name_list.AppComponentNameList"
    ]
    """<p>List of Application Components that this resource belongs to. If an Application Component is not part of the Resilience Hub application, it will be added.</p>"""
    additional_info: NotRequired[
        "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
    ]
    """<p>Currently, there is no supported additional information for resources.</p>"""
    excluded: NotRequired["capo_resiliencehub.types.boolean_optional.BooleanOptional"]
    """<p>Indicates if a resource is excluded from an Resilience Hub application.</p> <note> <p>You can exclude only imported resources from an Resilience Hub application.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppVersionResourceRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
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
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "app_components" in value:
        import capo_resiliencehub.types.app_component_name_list

        out["appComponents"] = (
            capo_resiliencehub.types.app_component_name_list.serialize_json(
                value["app_components"]
            )
        )
    if "additional_info" in value:
        import capo_resiliencehub.types.additional_info_map

        out["additionalInfo"] = (
            capo_resiliencehub.types.additional_info_map.serialize_json(
                value["additional_info"]
            )
        )
    if "excluded" in value:
        out["excluded"] = value["excluded"]
    return out


def deserialize_json(data: dict) -> UpdateAppVersionResourceRequest:
    out: UpdateAppVersionResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("UpdateAppVersionResourceRequest.app_arn required")
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
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("appComponents") is not None:
        import capo_resiliencehub.types.app_component_name_list

        out["app_components"] = (
            capo_resiliencehub.types.app_component_name_list.deserialize_json(
                data["appComponents"]
            )
        )
    if data.get("additionalInfo") is not None:
        import capo_resiliencehub.types.additional_info_map

        out["additional_info"] = (
            capo_resiliencehub.types.additional_info_map.deserialize_json(
                data["additionalInfo"]
            )
        )
    if data.get("excluded") is not None:
        out["excluded"] = data["excluded"]
    return out
