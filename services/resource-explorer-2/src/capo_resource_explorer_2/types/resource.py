"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resource_explorer_2.types.resource_property_list


class Resource(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the resource.</p>"""
    owning_account_id: NotRequired["str"]
    """<p>The Amazon Web Services account that owns the resource.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region in which the resource was created and exists.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource.</p>"""
    service: NotRequired["str"]
    """<p>The Amazon Web Services service that owns the resource and is responsible for creating and updating it.</p>"""
    cfn_resource_type: NotRequired["str"]
    """<p>The CloudFormation resource type identifier for the resource, such as <code>AWS::EC2::Instance</code> or <code>AWS::S3::Bucket</code>.</p>"""
    last_reported_at: NotRequired["datetime.datetime"]
    """<p>The date and time that Resource Explorer last queried this resource and updated the index with the latest information about the resource.</p>"""
    properties: NotRequired[
        "capo_resource_explorer_2.types.resource_property_list.ResourcePropertyList"
    ]
    """<p>A structure with additional type-specific details about the resource. These properties can be added by turning on integration between Resource Explorer and other Amazon Web Services services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owning_account_id" in value:
        out["OwningAccountId"] = value["owning_account_id"]
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "service" in value:
        out["Service"] = value["service"]
    if "cfn_resource_type" in value:
        out["CfnResourceType"] = value["cfn_resource_type"]
    if "last_reported_at" in value:
        import capo_resource_explorer_2._protocol.serialize

        out["LastReportedAt"] = (
            capo_resource_explorer_2._protocol.serialize.fmt_date_time(
                value["last_reported_at"]
            )
        )
    if "properties" in value:
        import capo_resource_explorer_2.types.resource_property_list

        out["Properties"] = (
            capo_resource_explorer_2.types.resource_property_list.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("OwningAccountId") is not None:
        out["owning_account_id"] = data["OwningAccountId"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    if data.get("CfnResourceType") is not None:
        out["cfn_resource_type"] = data["CfnResourceType"]
    if data.get("LastReportedAt") is not None:
        import datetime

        out["last_reported_at"] = datetime.datetime.fromisoformat(
            data["LastReportedAt"].replace("Z", "+00:00")
        )
    if data.get("Properties") is not None:
        import capo_resource_explorer_2.types.resource_property_list

        out["properties"] = (
            capo_resource_explorer_2.types.resource_property_list.deserialize_json(
                data["Properties"]
            )
        )
    return out
