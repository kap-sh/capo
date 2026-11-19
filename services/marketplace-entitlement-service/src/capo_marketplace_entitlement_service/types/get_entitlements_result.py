"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#GetEntitlementsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_entitlement_service.types.entitlement_list
    import capo_marketplace_entitlement_service.types.non_empty_string


class GetEntitlementsResult(TypedDict, closed=True):
    entitlements: NotRequired[
        "capo_marketplace_entitlement_service.types.entitlement_list.EntitlementList"
    ]
    """<p>The set of entitlements found through the GetEntitlements operation. If the result contains an empty set of entitlements, NextToken might still be present and should be used.</p>"""
    next_token: NotRequired[
        "capo_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
    ]
    """<p>For paginated results, use NextToken in subsequent calls to GetEntitlements. If the result contains an empty set of entitlements, NextToken might still be present and should be used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntitlementsResult) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import capo_marketplace_entitlement_service.types.entitlement_list

        out["Entitlements"] = (
            capo_marketplace_entitlement_service.types.entitlement_list.serialize_aws_json_1_1(
                value["entitlements"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntitlementsResult:
    out: GetEntitlementsResult = {}  # type: ignore[typeddict-item]
    if data.get("Entitlements") is not None:
        import capo_marketplace_entitlement_service.types.entitlement_list

        out["entitlements"] = (
            capo_marketplace_entitlement_service.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetEntitlementsResult) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import capo_marketplace_entitlement_service.types.entitlement_list

        out["Entitlements"] = (
            capo_marketplace_entitlement_service.types.entitlement_list.serialize_cbor(
                value["entitlements"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetEntitlementsResult:
    out: GetEntitlementsResult = {}  # type: ignore[typeddict-item]
    if data.get("Entitlements") is not None:
        import capo_marketplace_entitlement_service.types.entitlement_list

        out["entitlements"] = (
            capo_marketplace_entitlement_service.types.entitlement_list.deserialize_cbor(
                data["Entitlements"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
