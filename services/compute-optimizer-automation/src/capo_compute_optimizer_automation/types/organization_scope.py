"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#OrganizationScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.organization_configuration_account_ids


class OrganizationScope(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_compute_optimizer_automation.types.organization_configuration_account_ids.OrganizationConfigurationAccountIds"
    ]
    """<p>List of Amazon Web Services account IDs to include in the organization scope.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OrganizationScope) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer_automation.types.organization_configuration_account_ids

        out["accountIds"] = (
            capo_compute_optimizer_automation.types.organization_configuration_account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OrganizationScope:
    out: OrganizationScope = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_compute_optimizer_automation.types.organization_configuration_account_ids

        out["account_ids"] = (
            capo_compute_optimizer_automation.types.organization_configuration_account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationScope) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer_automation.types.organization_configuration_account_ids

        out["accountIds"] = (
            capo_compute_optimizer_automation.types.organization_configuration_account_ids.serialize_cbor(
                value["account_ids"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> OrganizationScope:
    out: OrganizationScope = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_compute_optimizer_automation.types.organization_configuration_account_ids

        out["account_ids"] = (
            capo_compute_optimizer_automation.types.organization_configuration_account_ids.deserialize_cbor(
                data["accountIds"]
            )
        )
    return out
