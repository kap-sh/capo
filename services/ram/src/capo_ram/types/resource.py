"""Generated from Smithy shape ``com.amazonaws.ram#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.date_time
    import capo_ram.types.resource_region_scope
    import capo_ram.types.resource_status
    import capo_ram.types.string


class Resource(TypedDict, closed=True):
    arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource.</p>"""
    type: NotRequired["capo_ram.types.string.String"]
    """<p>The resource type. This takes the form of: <code>service-code</code>:<code>resource-code</code>, and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string <code>ec2:subnet</code>.</p>"""
    resource_share_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share this resource is associated with.</p>"""
    resource_group_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource group. This value is available only if the resource is part of a resource group.</p>"""
    status: NotRequired["capo_ram.types.resource_status.ResourceStatus"]
    """<p>The current status of the resource.</p>"""
    status_message: NotRequired["capo_ram.types.string.String"]
    """<p>A message about the status of the resource.</p>"""
    creation_time: NotRequired["capo_ram.types.date_time.DateTime"]
    """<p>The date and time when the resource was associated with the resource share.</p>"""
    last_updated_time: NotRequired["capo_ram.types.date_time.DateTime"]
    """<p>The date an time when the association between the resource and the resource share was last updated.</p>"""
    resource_region_scope: NotRequired[
        "capo_ram.types.resource_region_scope.ResourceRegionScope"
    ]
    """<p>Specifies the scope of visibility of this resource:</p> <ul> <li> <p> <b>REGIONAL</b> – The resource can be accessed only by using requests that target the Amazon Web Services Region in which the resource exists.</p> </li> <li> <p> <b>GLOBAL</b> – The resource can be accessed from any Amazon Web Services Region.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        out["type"] = value["type"]
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "resource_group_arn" in value:
        out["resourceGroupArn"] = value["resource_group_arn"]
    if "status" in value:
        import capo_ram.types.resource_status

        out["status"] = capo_ram.types.resource_status.serialize_json(value["status"])
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_time" in value:
        import capo_ram.types.date_time

        out["creationTime"] = capo_ram.types.date_time.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_ram.types.date_time

        out["lastUpdatedTime"] = capo_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    if "resource_region_scope" in value:
        import capo_ram.types.resource_region_scope

        out["resourceRegionScope"] = (
            capo_ram.types.resource_region_scope.serialize_json(
                value["resource_region_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    if data.get("resourceGroupArn") is not None:
        out["resource_group_arn"] = data["resourceGroupArn"]
    if data.get("status") is not None:
        import capo_ram.types.resource_status

        out["status"] = capo_ram.types.resource_status.deserialize_json(data["status"])
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("creationTime") is not None:
        import capo_ram.types.date_time

        out["creation_time"] = capo_ram.types.date_time.deserialize_json(
            data["creationTime"]
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_ram.types.date_time

        out["last_updated_time"] = capo_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    if data.get("resourceRegionScope") is not None:
        import capo_ram.types.resource_region_scope

        out["resource_region_scope"] = (
            capo_ram.types.resource_region_scope.deserialize_json(
                data["resourceRegionScope"]
            )
        )
    return out
