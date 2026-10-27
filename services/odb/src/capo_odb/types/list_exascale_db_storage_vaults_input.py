"""Generated from Smithy shape ``com.amazonaws.odb#ListExascaleDbStorageVaultsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.exascale_db_storage_vault_type
    import capo_odb.types.resource_id_or_arn


class ListExascaleDbStorageVaultsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    cloud_exadata_infrastructure_id: NotRequired[
        "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier or Amazon Resource Name (ARN) of an Exadata infrastructure. If you specify this value, the operation returns only the Exascale storage vaults on that infrastructure that you own or that are shared with you. The infrastructure can be one that's shared with you through Amazon Web Services Resource Access Manager (Amazon Web Services RAM). You can't combine this filter with a <code>vaultType</code> of <code>EXASCALE_INFRASTRUCTURE</code>.</p>"""
    vault_type: NotRequired[
        "capo_odb.types.exascale_db_storage_vault_type.ExascaleDbStorageVaultType"
    ]
    """<p>The type of Exascale storage vaults to return. Specify <code>DEDICATED_INFRASTRUCTURE</code> to return Exascale storage vaults on dedicated Exadata infrastructure, or <code>EXASCALE_INFRASTRUCTURE</code> to return Exascale storage vaults for Exascale VM clusters. If you don't specify a value, the operation returns both types. You can't combine <code>EXASCALE_INFRASTRUCTURE</code> with the <code>cloudExadataInfrastructureId</code> filter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListExascaleDbStorageVaultsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "vault_type" in value:
        import capo_odb.types.exascale_db_storage_vault_type

        out["vaultType"] = (
            capo_odb.types.exascale_db_storage_vault_type.serialize_aws_json_1_0(
                value["vault_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListExascaleDbStorageVaultsInput:
    out: ListExascaleDbStorageVaultsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    if data.get("vaultType") is not None:
        import capo_odb.types.exascale_db_storage_vault_type

        out["vault_type"] = (
            capo_odb.types.exascale_db_storage_vault_type.deserialize_aws_json_1_0(
                data["vaultType"]
            )
        )
    return out
