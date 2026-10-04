"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cloud_provider_name
    import capo_securityhub.types.non_empty_string


class RemediationResource(TypedDict, closed=True):
    account_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account that recorded the resource data in Security Hub.</p>"""
    region: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region in which Security Hub recorded the resource data.</p>"""
    resource_owner_account_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the cloud account that owns the resource. For Amazon Web Services resources, this is the Amazon Web Services account ID. For Azure resources, this is the Azure subscription ID.</p>"""
    resource_owner_org_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the cloud organization that owns the resource. For Amazon Web Services resources, this is the Organizations ID. For Azure resources, this is the Azure tenant ID.</p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of the resource.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the resource.</p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for a resource.</p>"""
    resource_guid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The global identifier used to identify a resource.</p>"""
    resource_region: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The native cloud region where the resource is located. For Amazon Web Services, this is an Amazon Web Services Region (for example, <code>us-east-1</code>). For Azure resources, this is the Azure region (for example, <code>westus2</code>). This field is always included.</p>"""
    cloud_provider: NotRequired[
        "capo_securityhub.types.cloud_provider_name.CloudProviderName"
    ]
    """<p>The cloud provider where the resource exists.</p> <ul> <li> <p> <code>AWS</code> specifies that the resource exists in Amazon Web Services.</p> </li> <li> <p> <code>Azure</code> specifies that the resource exists in Microsoft Azure.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationResource) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_owner_account_id" in value:
        out["ResourceOwnerAccountId"] = value["resource_owner_account_id"]
    if "resource_owner_org_id" in value:
        out["ResourceOwnerOrgId"] = value["resource_owner_org_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "resource_guid" in value:
        out["ResourceGuid"] = value["resource_guid"]
    if "resource_region" in value:
        out["ResourceRegion"] = value["resource_region"]
    if "cloud_provider" in value:
        import capo_securityhub.types.cloud_provider_name

        out["CloudProvider"] = (
            capo_securityhub.types.cloud_provider_name.serialize_json(
                value["cloud_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemediationResource:
    out: RemediationResource = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("ResourceOwnerAccountId") is not None:
        out["resource_owner_account_id"] = data["ResourceOwnerAccountId"]
    if data.get("ResourceOwnerOrgId") is not None:
        out["resource_owner_org_id"] = data["ResourceOwnerOrgId"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ResourceGuid") is not None:
        out["resource_guid"] = data["ResourceGuid"]
    if data.get("ResourceRegion") is not None:
        out["resource_region"] = data["ResourceRegion"]
    if data.get("CloudProvider") is not None:
        import capo_securityhub.types.cloud_provider_name

        out["cloud_provider"] = (
            capo_securityhub.types.cloud_provider_name.deserialize_json(
                data["CloudProvider"]
            )
        )
    return out
