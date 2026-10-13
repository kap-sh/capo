"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptSubscriptionRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.accepted_asset_scopes
    import capo_datazone.types.asset_permissions
    import capo_datazone.types.decision_comment
    import capo_datazone.types.domain_id
    import capo_datazone.types.subscription_request_id


class AcceptSubscriptionRequestInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The Amazon DataZone domain where the specified subscription request is being accepted.</p>"""
    identifier: "capo_datazone.types.subscription_request_id.SubscriptionRequestId"
    """<p>The unique identifier of the subscription request that is to be accepted.</p>"""
    decision_comment: NotRequired[
        "capo_datazone.types.decision_comment.DecisionComment"
    ]
    """<p>A description that specifies the reason for accepting the specified subscription request.</p>"""
    asset_scopes: NotRequired[
        "capo_datazone.types.accepted_asset_scopes.AcceptedAssetScopes"
    ]
    """<p>The asset scopes of the accept subscription request.</p>"""
    asset_permissions: NotRequired[
        "capo_datazone.types.asset_permissions.AssetPermissions"
    ]
    """<p>The asset permissions of the accept subscription request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptSubscriptionRequestInput) -> dict:
    out: dict = {}
    if "decision_comment" in value:
        out["decisionComment"] = value["decision_comment"]
    if "asset_scopes" in value:
        import capo_datazone.types.accepted_asset_scopes

        out["assetScopes"] = capo_datazone.types.accepted_asset_scopes.serialize_json(
            value["asset_scopes"]
        )
    if "asset_permissions" in value:
        import capo_datazone.types.asset_permissions

        out["assetPermissions"] = capo_datazone.types.asset_permissions.serialize_json(
            value["asset_permissions"]
        )
    return out


def deserialize_json(data: dict) -> AcceptSubscriptionRequestInput:
    out: AcceptSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("decisionComment") is not None:
        out["decision_comment"] = data["decisionComment"]
    if data.get("assetScopes") is not None:
        import capo_datazone.types.accepted_asset_scopes

        out["asset_scopes"] = (
            capo_datazone.types.accepted_asset_scopes.deserialize_json(
                data["assetScopes"]
            )
        )
    if data.get("assetPermissions") is not None:
        import capo_datazone.types.asset_permissions

        out["asset_permissions"] = (
            capo_datazone.types.asset_permissions.deserialize_json(
                data["assetPermissions"]
            )
        )
    return out


def redact_sensitive(value: AcceptSubscriptionRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "decision_comment" in value:
        out["decision_comment"] = "*** Sensitive Data Redacted ***"
    return out
