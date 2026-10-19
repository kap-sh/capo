"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListIdentityProvidersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.identity_provider_summary_list


class ListIdentityProvidersResponse(TypedDict, closed=True):
    identity_provider_summaries: "capo_license_manager_user_subscriptions.types.identity_provider_summary_list.IdentityProviderSummaryList"
    """<p>An array of <code>IdentityProviderSummary</code> resources that contain details about the Active Directory identity providers that meet the request criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityProvidersResponse) -> dict:
    out: dict = {}
    import capo_license_manager_user_subscriptions.types.identity_provider_summary_list

    out["IdentityProviderSummaries"] = (
        capo_license_manager_user_subscriptions.types.identity_provider_summary_list.serialize_json(
            value["identity_provider_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdentityProvidersResponse:
    out: ListIdentityProvidersResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityProviderSummaries") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider_summary_list

        out["identity_provider_summaries"] = (
            capo_license_manager_user_subscriptions.types.identity_provider_summary_list.deserialize_json(
                data["IdentityProviderSummaries"]
            )
        )
    else:
        out["identity_provider_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
