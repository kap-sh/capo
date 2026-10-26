"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListProductSubscriptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.box_integer
    import capo_license_manager_user_subscriptions.types.filter_list
    import capo_license_manager_user_subscriptions.types.identity_provider


class ListProductSubscriptionsRequest(TypedDict, closed=True):
    product: NotRequired["str"]
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>An object that specifies details for the identity provider.</p>"""
    max_results: NotRequired[
        "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
    ]
    """<p>The maximum number of results to return from a single request.</p>"""
    filters: NotRequired[
        "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
    ]
    """<p>You can use the following filters to streamline results:</p> <ul> <li> <p>Status</p> </li> <li> <p>Username</p> </li> <li> <p>Domain</p> </li> </ul>"""
    next_token: NotRequired["str"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProductSubscriptionsRequest) -> dict:
    out: dict = {}
    if "product" in value:
        out["Product"] = value["product"]
    import capo_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_license_manager_user_subscriptions.types.filter_list

        out["Filters"] = (
            capo_license_manager_user_subscriptions.types.filter_list.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProductSubscriptionsRequest:
    out: ListProductSubscriptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Product") is not None:
        out["product"] = data["Product"]
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        out["identity_provider"] = {"$unknown": {"name": ""}}
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_license_manager_user_subscriptions.types.filter_list

        out["filters"] = (
            capo_license_manager_user_subscriptions.types.filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
