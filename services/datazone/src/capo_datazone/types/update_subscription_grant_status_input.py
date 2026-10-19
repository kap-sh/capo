"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateSubscriptionGrantStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.domain_id
    import capo_datazone.types.failure_cause
    import capo_datazone.types.subscription_grant_id
    import capo_datazone.types.subscription_grant_status


class UpdateSubscriptionGrantStatusInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a subscription grant status is to be updated.</p>"""
    identifier: "capo_datazone.types.subscription_grant_id.SubscriptionGrantId"
    """<p>The identifier of the subscription grant the status of which is to be updated.</p>"""
    asset_identifier: "capo_datazone.types.asset_id.AssetId"
    """<p>The identifier of the asset the subscription grant status of which is to be updated.</p>"""
    status: "capo_datazone.types.subscription_grant_status.SubscriptionGrantStatus"
    """<p>The status to be updated as part of the <code>UpdateSubscriptionGrantStatus</code> action.</p>"""
    failure_cause: NotRequired["capo_datazone.types.failure_cause.FailureCause"]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    target_name: NotRequired["str"]
    """<p>The target name to be updated as part of the <code>UpdateSubscriptionGrantStatus</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionGrantStatusInput) -> dict:
    out: dict = {}
    import capo_datazone.types.subscription_grant_status

    out["status"] = capo_datazone.types.subscription_grant_status.serialize_json(
        value["status"]
    )
    if "failure_cause" in value:
        import capo_datazone.types.failure_cause

        out["failureCause"] = capo_datazone.types.failure_cause.serialize_json(
            value["failure_cause"]
        )
    if "target_name" in value:
        out["targetName"] = value["target_name"]
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionGrantStatusInput:
    out: UpdateSubscriptionGrantStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_datazone.types.subscription_grant_status

        out["status"] = capo_datazone.types.subscription_grant_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.subscription_grant_status.SubscriptionGrantStatus", ""
        )
    if data.get("failureCause") is not None:
        import capo_datazone.types.failure_cause

        out["failure_cause"] = capo_datazone.types.failure_cause.deserialize_json(
            data["failureCause"]
        )
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    return out
