"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#OrganizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.organization_configuration_account_ids
    import capo_compute_optimizer_automation.types.rule_apply_order


class OrganizationConfiguration(TypedDict, closed=True):
    rule_apply_order: NotRequired[
        "capo_compute_optimizer_automation.types.rule_apply_order.RuleApplyOrder"
    ]
    """<p>Specifies when organization rules should be applied relative to account rules.</p>"""
    account_ids: NotRequired[
        "capo_compute_optimizer_automation.types.organization_configuration_account_ids.OrganizationConfigurationAccountIds"
    ]
    """<p>List of specific Amazon Web Services account IDs where the organization rule should be applied.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OrganizationConfiguration) -> dict:
    out: dict = {}
    if "rule_apply_order" in value:
        import capo_compute_optimizer_automation.types.rule_apply_order

        out["ruleApplyOrder"] = (
            capo_compute_optimizer_automation.types.rule_apply_order.serialize_aws_json_1_0(
                value["rule_apply_order"]
            )
        )
    if "account_ids" in value:
        import capo_compute_optimizer_automation.types.organization_configuration_account_ids

        out["accountIds"] = (
            capo_compute_optimizer_automation.types.organization_configuration_account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OrganizationConfiguration:
    out: OrganizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ruleApplyOrder") is not None:
        import capo_compute_optimizer_automation.types.rule_apply_order

        out["rule_apply_order"] = (
            capo_compute_optimizer_automation.types.rule_apply_order.deserialize_aws_json_1_0(
                data["ruleApplyOrder"]
            )
        )
    if data.get("accountIds") is not None:
        import capo_compute_optimizer_automation.types.organization_configuration_account_ids

        out["account_ids"] = (
            capo_compute_optimizer_automation.types.organization_configuration_account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationConfiguration) -> dict:
    out: dict = {}
    if "rule_apply_order" in value:
        import capo_compute_optimizer_automation.types.rule_apply_order

        out["ruleApplyOrder"] = (
            capo_compute_optimizer_automation.types.rule_apply_order.serialize_cbor(
                value["rule_apply_order"]
            )
        )
    if "account_ids" in value:
        import capo_compute_optimizer_automation.types.organization_configuration_account_ids

        out["accountIds"] = (
            capo_compute_optimizer_automation.types.organization_configuration_account_ids.serialize_cbor(
                value["account_ids"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> OrganizationConfiguration:
    out: OrganizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ruleApplyOrder") is not None:
        import capo_compute_optimizer_automation.types.rule_apply_order

        out["rule_apply_order"] = (
            capo_compute_optimizer_automation.types.rule_apply_order.deserialize_cbor(
                data["ruleApplyOrder"]
            )
        )
    if data.get("accountIds") is not None:
        import capo_compute_optimizer_automation.types.organization_configuration_account_ids

        out["account_ids"] = (
            capo_compute_optimizer_automation.types.organization_configuration_account_ids.deserialize_cbor(
                data["accountIds"]
            )
        )
    return out
