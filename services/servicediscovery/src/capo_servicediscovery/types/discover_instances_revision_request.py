"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DiscoverInstancesRevisionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.namespace_name
    import capo_servicediscovery.types.service_name


class DiscoverInstancesRevisionRequest(TypedDict, closed=True):
    namespace_name: "capo_servicediscovery.types.namespace_name.NamespaceName"
    """<p>The <code>HttpName</code> name of the namespace. The <code>HttpName</code> is found in the <code>HttpProperties</code> member of the <code>Properties</code> member of the namespace.</p>"""
    service_name: "capo_servicediscovery.types.service_name.ServiceName"
    """<p>The name of the service that you specified when you registered the instance.</p>"""
    owner_account: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that owns the namespace associated with the instance, as specified in the namespace <code>ResourceOwner</code> field. For instances associated with namespaces that are shared with your account, you must specify an <code>OwnerAccount</code>. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverInstancesRevisionRequest) -> dict:
    out: dict = {}
    out["NamespaceName"] = value["namespace_name"]
    out["ServiceName"] = value["service_name"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverInstancesRevisionRequest:
    out: DiscoverInstancesRevisionRequest = {}  # type: ignore[typeddict-item]
    if data.get("NamespaceName") is not None:
        out["namespace_name"] = data["NamespaceName"]
    else:
        raise DeserializationError(
            "DiscoverInstancesRevisionRequest.namespace_name required"
        )
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    else:
        raise DeserializationError(
            "DiscoverInstancesRevisionRequest.service_name required"
        )
    if data.get("OwnerAccount") is not None:
        out["owner_account"] = data["OwnerAccount"]
    return out
