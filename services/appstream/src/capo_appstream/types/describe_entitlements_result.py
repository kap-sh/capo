"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeEntitlementsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.entitlement_list
    import capo_appstream.types.string


class DescribeEntitlementsResult(TypedDict, closed=True):
    entitlements: NotRequired["capo_appstream.types.entitlement_list.EntitlementList"]
    """<p>The entitlements.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntitlementsResult) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import capo_appstream.types.entitlement_list

        out["Entitlements"] = (
            capo_appstream.types.entitlement_list.serialize_aws_json_1_1(
                value["entitlements"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntitlementsResult:
    out: DescribeEntitlementsResult = {}  # type: ignore[typeddict-item]
    if data.get("Entitlements") is not None:
        import capo_appstream.types.entitlement_list

        out["entitlements"] = (
            capo_appstream.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEntitlementsResult) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import capo_appstream.types.entitlement_list

        out["Entitlements"] = capo_appstream.types.entitlement_list.serialize_cbor(
            value["entitlements"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeEntitlementsResult:
    out: DescribeEntitlementsResult = {}  # type: ignore[typeddict-item]
    if data.get("Entitlements") is not None:
        import capo_appstream.types.entitlement_list

        out["entitlements"] = capo_appstream.types.entitlement_list.deserialize_cbor(
            data["Entitlements"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
