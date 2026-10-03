"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.service_attributes_map


class ServiceAttributes(TypedDict, closed=True):
    service_arn: NotRequired["capo_servicediscovery.types.arn.Arn"]
    """<p>The ARN of the service that the attributes are associated with.</p>"""
    resource_owner: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that created the namespace with which the service is associated. If this isn't your account ID, it is the ID of the account that shared the namespace with your account. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    attributes: NotRequired[
        "capo_servicediscovery.types.service_attributes_map.ServiceAttributesMap"
    ]
    """<p>A string map that contains the following information for the service that you specify in <code>ServiceArn</code>:</p> <ul> <li> <p>The attributes that apply to the service. </p> </li> <li> <p>For each attribute, the applicable value.</p> </li> </ul> <p>You can specify a total of 30 attributes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceAttributes) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["ServiceArn"] = value["service_arn"]
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "attributes" in value:
        import capo_servicediscovery.types.service_attributes_map

        out["Attributes"] = (
            capo_servicediscovery.types.service_attributes_map.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceAttributes:
    out: ServiceAttributes = {}  # type: ignore[typeddict-item]
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    if data.get("ResourceOwner") is not None:
        out["resource_owner"] = data["ResourceOwner"]
    if data.get("Attributes") is not None:
        import capo_servicediscovery.types.service_attributes_map

        out["attributes"] = (
            capo_servicediscovery.types.service_attributes_map.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out
