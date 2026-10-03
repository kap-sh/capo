"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.namespace_name
    import capo_servicediscovery.types.namespace_properties
    import capo_servicediscovery.types.namespace_type
    import capo_servicediscovery.types.resource_count
    import capo_servicediscovery.types.resource_description
    import capo_servicediscovery.types.resource_id
    import capo_servicediscovery.types.timestamp


class NamespaceSummary(TypedDict, closed=True):
    id: NotRequired["capo_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID of the namespace.</p>"""
    arn: NotRequired["capo_servicediscovery.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that Cloud Map assigns to the namespace when you create it.</p>"""
    resource_owner: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that created the namespace. If this isn't your account ID, it's the ID of the account that shared the namespace with your account. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    name: NotRequired["capo_servicediscovery.types.namespace_name.NamespaceName"]
    """<p>The name of the namespace. When you create a namespace, Cloud Map automatically creates a Route 53 hosted zone that has the same name as the namespace.</p>"""
    type: NotRequired["capo_servicediscovery.types.namespace_type.NamespaceType"]
    """<p>The type of the namespace, either public or private.</p>"""
    description: NotRequired[
        "capo_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>A description for the namespace.</p>"""
    service_count: NotRequired[
        "capo_servicediscovery.types.resource_count.ResourceCount"
    ]
    """<p>The number of services that were created using the namespace.</p>"""
    properties: NotRequired[
        "capo_servicediscovery.types.namespace_properties.NamespaceProperties"
    ]
    """<p>The properties of the namespace.</p>"""
    create_date: NotRequired["capo_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date and time that the namespace was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_servicediscovery.types.namespace_type

        out["Type"] = capo_servicediscovery.types.namespace_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "service_count" in value:
        out["ServiceCount"] = value["service_count"]
    if "properties" in value:
        import capo_servicediscovery.types.namespace_properties

        out["Properties"] = (
            capo_servicediscovery.types.namespace_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "create_date" in value:
        import capo_servicediscovery.types.timestamp

        out["CreateDate"] = (
            capo_servicediscovery.types.timestamp.serialize_aws_json_1_1(
                value["create_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NamespaceSummary:
    out: NamespaceSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ResourceOwner") is not None:
        out["resource_owner"] = data["ResourceOwner"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_servicediscovery.types.namespace_type

        out["type"] = (
            capo_servicediscovery.types.namespace_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ServiceCount") is not None:
        out["service_count"] = data["ServiceCount"]
    if data.get("Properties") is not None:
        import capo_servicediscovery.types.namespace_properties

        out["properties"] = (
            capo_servicediscovery.types.namespace_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if data.get("CreateDate") is not None:
        import capo_servicediscovery.types.timestamp

        out["create_date"] = (
            capo_servicediscovery.types.timestamp.deserialize_aws_json_1_1(
                data["CreateDate"]
            )
        )
    return out
