"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.asset_id
    import capo_datazone.types.asset_scope
    import capo_datazone.types.failure_cause
    import capo_datazone.types.permissions
    import capo_datazone.types.revision
    import capo_datazone.types.subscription_grant_status


class SubscribedAsset(TypedDict, closed=True):
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The identifier of the asset for which the subscription grant is created.</p>"""
    asset_revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the asset for which the subscription grant is created.</p>"""
    status: "capo_datazone.types.subscription_grant_status.SubscriptionGrantStatus"
    """<p>The status of the asset for which the subscription grant is created.</p>"""
    target_name: NotRequired["str"]
    """<p>The target name of the asset for which the subscription grant is created.</p>"""
    failure_cause: NotRequired["capo_datazone.types.failure_cause.FailureCause"]
    """<p>The failure cause included in the details of the asset for which the subscription grant is created.</p>"""
    granted_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the subscription grant to the asset is created.</p>"""
    failure_timestamp: NotRequired["datetime.datetime"]
    """<p>The failure timestamp included in the details of the asset for which the subscription grant is created.</p>"""
    asset_scope: NotRequired["capo_datazone.types.asset_scope.AssetScope"]
    """<p>The asset scope of the subscribed asset.</p>"""
    permissions: NotRequired["capo_datazone.types.permissions.Permissions"]
    """<p>The asset permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedAsset) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["assetRevision"] = value["asset_revision"]
    import capo_datazone.types.subscription_grant_status

    out["status"] = capo_datazone.types.subscription_grant_status.serialize_json(
        value["status"]
    )
    if "target_name" in value:
        out["targetName"] = value["target_name"]
    if "failure_cause" in value:
        import capo_datazone.types.failure_cause

        out["failureCause"] = capo_datazone.types.failure_cause.serialize_json(
            value["failure_cause"]
        )
    if "granted_timestamp" in value:
        import capo_datazone.types._prelude.timestamp

        out["grantedTimestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["granted_timestamp"]
        )
    if "failure_timestamp" in value:
        import capo_datazone.types._prelude.timestamp

        out["failureTimestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["failure_timestamp"]
        )
    if "asset_scope" in value:
        import capo_datazone.types.asset_scope

        out["assetScope"] = capo_datazone.types.asset_scope.serialize_json(
            value["asset_scope"]
        )
    if "permissions" in value:
        import capo_datazone.types.permissions

        out["permissions"] = capo_datazone.types.permissions.serialize_json(
            value["permissions"]
        )
    return out


def deserialize_json(data: dict) -> SubscribedAsset:
    out: SubscribedAsset = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("assetRevision") is not None:
        out["asset_revision"] = data["assetRevision"]
    else:
        out["asset_revision"] = ""
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
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    if data.get("failureCause") is not None:
        import capo_datazone.types.failure_cause

        out["failure_cause"] = capo_datazone.types.failure_cause.deserialize_json(
            data["failureCause"]
        )
    if data.get("grantedTimestamp") is not None:
        import capo_datazone.types._prelude.timestamp

        out["granted_timestamp"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["grantedTimestamp"]
            )
        )
    if data.get("failureTimestamp") is not None:
        import capo_datazone.types._prelude.timestamp

        out["failure_timestamp"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["failureTimestamp"]
            )
        )
    if data.get("assetScope") is not None:
        import capo_datazone.types.asset_scope

        out["asset_scope"] = capo_datazone.types.asset_scope.deserialize_json(
            data["assetScope"]
        )
    if data.get("permissions") is not None:
        import capo_datazone.types.permissions

        out["permissions"] = capo_datazone.types.permissions.deserialize_json(
            data["permissions"]
        )
    return out
