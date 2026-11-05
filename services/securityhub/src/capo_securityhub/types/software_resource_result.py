"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class SoftwareResourceResult(TypedDict, closed=True):
    account_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account that recorded the resource data in Security Hub.</p>"""
    resource_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of resource, for example <code>AWS::EC2::Instance</code> or <code>AWS::Lambda::Function</code>.</p>"""
    region: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region that recorded the resource data in Security Hub.</p>"""
    resource_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for a resource.</p>"""
    resource_provider: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The cloud provider where the resource exists. Valid values are <code>AWS</code> and <code>Azure</code>.</p>"""
    resource_owner_org_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the cloud organization that owns the resource. For Amazon Web Services resources, this is the Organizations ID. For Azure resources, this is the Azure tenant ID.</p>"""
    resource_owner_account_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the cloud account that owns the resource. For Amazon Web Services resources, this is the Amazon Web Services account ID. For Azure resources, this is the Azure subscription ID.</p>"""
    resource_cloud_partition: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The cloud partition where the resource exists. For Amazon Web Services, valid values include <code>aws</code>, <code>aws-cn</code>, and <code>aws-us-gov</code>. This field isn't returned for cloud providers that don't use partitions.</p>"""
    resource_region: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The native cloud region where the resource is located. For Amazon Web Services, this is an Amazon Web Services Region (for example, <code>us-east-1</code>). For Azure resources, this is the Azure region (for example, <code>westus2</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareResourceResult) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_provider" in value:
        out["ResourceProvider"] = value["resource_provider"]
    if "resource_owner_org_id" in value:
        out["ResourceOwnerOrgId"] = value["resource_owner_org_id"]
    if "resource_owner_account_id" in value:
        out["ResourceOwnerAccountId"] = value["resource_owner_account_id"]
    if "resource_cloud_partition" in value:
        out["ResourceCloudPartition"] = value["resource_cloud_partition"]
    if "resource_region" in value:
        out["ResourceRegion"] = value["resource_region"]
    return out


def deserialize_json(data: dict) -> SoftwareResourceResult:
    out: SoftwareResourceResult = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceProvider") is not None:
        out["resource_provider"] = data["ResourceProvider"]
    if data.get("ResourceOwnerOrgId") is not None:
        out["resource_owner_org_id"] = data["ResourceOwnerOrgId"]
    if data.get("ResourceOwnerAccountId") is not None:
        out["resource_owner_account_id"] = data["ResourceOwnerAccountId"]
    if data.get("ResourceCloudPartition") is not None:
        out["resource_cloud_partition"] = data["ResourceCloudPartition"]
    if data.get("ResourceRegion") is not None:
        out["resource_region"] = data["ResourceRegion"]
    return out
