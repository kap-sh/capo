"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSelfUpgradeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.self_upgrade_admin_action
    import capo_quicksight.types.string


class UpdateSelfUpgradeRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the self-upgrade request.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The Quick namespace for the self-upgrade request.</p>"""
    upgrade_request_id: "capo_quicksight.types.string.String"
    """<p>The ID of the self-upgrade request to update.</p>"""
    action: "capo_quicksight.types.self_upgrade_admin_action.SelfUpgradeAdminAction"
    """<p>The action to perform on the self-upgrade request. Valid values are <code>APPROVE</code>, <code>DENY</code>, or <code>VERIFY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSelfUpgradeRequest) -> dict:
    out: dict = {}
    out["UpgradeRequestId"] = value["upgrade_request_id"]
    import capo_quicksight.types.self_upgrade_admin_action

    out["Action"] = capo_quicksight.types.self_upgrade_admin_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSelfUpgradeRequest:
    out: UpdateSelfUpgradeRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpgradeRequestId") is not None:
        out["upgrade_request_id"] = data["UpgradeRequestId"]
    else:
        out["upgrade_request_id"] = ""
    if data.get("Action") is not None:
        import capo_quicksight.types.self_upgrade_admin_action

        out["action"] = (
            capo_quicksight.types.self_upgrade_admin_action.deserialize_json(
                data["Action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_quicksight.types.self_upgrade_admin_action.SelfUpgradeAdminAction", ""
        )
    return out
