"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.stack_set_accounts
    import capo_service_catalog.types.stack_set_regions


class ProvisioningArtifactPreferences(TypedDict, closed=True):
    stack_set_accounts: NotRequired[
        "capo_service_catalog.types.stack_set_accounts.StackSetAccounts"
    ]
    """<p>One or more Amazon Web Services accounts where stack instances are deployed from the stack set. These accounts can be scoped in <code>ProvisioningPreferences$StackSetAccounts</code> and <code>UpdateProvisioningPreferences$StackSetAccounts</code>.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p>"""
    stack_set_regions: NotRequired[
        "capo_service_catalog.types.stack_set_regions.StackSetRegions"
    ]
    """<p>One or more Amazon Web Services Regions where stack instances are deployed from the stack set. These Regions can be scoped in <code>ProvisioningPreferences$StackSetRegions</code> and <code>UpdateProvisioningPreferences$StackSetRegions</code>.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactPreferences) -> dict:
    out: dict = {}
    if "stack_set_accounts" in value:
        import capo_service_catalog.types.stack_set_accounts

        out["StackSetAccounts"] = (
            capo_service_catalog.types.stack_set_accounts.serialize_aws_json_1_1(
                value["stack_set_accounts"]
            )
        )
    if "stack_set_regions" in value:
        import capo_service_catalog.types.stack_set_regions

        out["StackSetRegions"] = (
            capo_service_catalog.types.stack_set_regions.serialize_aws_json_1_1(
                value["stack_set_regions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactPreferences:
    out: ProvisioningArtifactPreferences = {}  # type: ignore[typeddict-item]
    if data.get("StackSetAccounts") is not None:
        import capo_service_catalog.types.stack_set_accounts

        out["stack_set_accounts"] = (
            capo_service_catalog.types.stack_set_accounts.deserialize_aws_json_1_1(
                data["StackSetAccounts"]
            )
        )
    if data.get("StackSetRegions") is not None:
        import capo_service_catalog.types.stack_set_regions

        out["stack_set_regions"] = (
            capo_service_catalog.types.stack_set_regions.deserialize_aws_json_1_1(
                data["StackSetRegions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactPreferences) -> dict:
    out: dict = {}
    if "stack_set_accounts" in value:
        import capo_service_catalog.types.stack_set_accounts

        out["StackSetAccounts"] = (
            capo_service_catalog.types.stack_set_accounts.serialize_cbor(
                value["stack_set_accounts"]
            )
        )
    if "stack_set_regions" in value:
        import capo_service_catalog.types.stack_set_regions

        out["StackSetRegions"] = (
            capo_service_catalog.types.stack_set_regions.serialize_cbor(
                value["stack_set_regions"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ProvisioningArtifactPreferences:
    out: ProvisioningArtifactPreferences = {}  # type: ignore[typeddict-item]
    if data.get("StackSetAccounts") is not None:
        import capo_service_catalog.types.stack_set_accounts

        out["stack_set_accounts"] = (
            capo_service_catalog.types.stack_set_accounts.deserialize_cbor(
                data["StackSetAccounts"]
            )
        )
    if data.get("StackSetRegions") is not None:
        import capo_service_catalog.types.stack_set_regions

        out["stack_set_regions"] = (
            capo_service_catalog.types.stack_set_regions.deserialize_cbor(
                data["StackSetRegions"]
            )
        )
    return out
