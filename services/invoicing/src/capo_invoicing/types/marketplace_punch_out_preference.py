"""Generated from Smithy shape ``com.amazonaws.invoicing#MarketplacePunchOutPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space


class MarketplacePunchOutPreference(TypedDict, closed=True):
    approval_request_redirect_url: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The URL that buyers are redirected to for approval requests in the procurement portal. This is only supported for Coupa. When provided together with the procurement portal instance endpoint, its host must match the host of that endpoint.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MarketplacePunchOutPreference) -> dict:
    out: dict = {}
    if "approval_request_redirect_url" in value:
        out["ApprovalRequestRedirectUrl"] = value["approval_request_redirect_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MarketplacePunchOutPreference:
    out: MarketplacePunchOutPreference = {}  # type: ignore[typeddict-item]
    if data.get("ApprovalRequestRedirectUrl") is not None:
        out["approval_request_redirect_url"] = data["ApprovalRequestRedirectUrl"]
    return out
