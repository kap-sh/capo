"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSelfUpgradeConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.self_upgrade_status


class UpdateSelfUpgradeConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the Quick self-upgrade configuration that you want to update.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The Quick namespace that you want to update the Quick self-upgrade configuration for.</p>"""
    self_upgrade_status: "capo_quicksight.types.self_upgrade_status.SelfUpgradeStatus"
    """<p>The self-upgrade status that you want to set for the Quick account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSelfUpgradeConfigurationRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.self_upgrade_status

    out["SelfUpgradeStatus"] = capo_quicksight.types.self_upgrade_status.serialize_json(
        value["self_upgrade_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSelfUpgradeConfigurationRequest:
    out: UpdateSelfUpgradeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SelfUpgradeStatus") is not None:
        import capo_quicksight.types.self_upgrade_status

        out["self_upgrade_status"] = (
            capo_quicksight.types.self_upgrade_status.deserialize_json(
                data["SelfUpgradeStatus"]
            )
        )
    else:
        import typing

        out["self_upgrade_status"] = typing.cast(
            "capo_quicksight.types.self_upgrade_status.SelfUpgradeStatus", ""
        )
    return out
