"""Generated from Smithy shape ``com.amazonaws.quicksight#SharePointParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.auth_type
    import capo_quicksight.types.share_point_client_id
    import capo_quicksight.types.share_point_domain
    import capo_quicksight.types.share_point_tenant_id


class SharePointParameters(TypedDict, closed=True):
    share_point_domain: "capo_quicksight.types.share_point_domain.SharePointDomain"
    """<p>The SharePoint domain for the data source.</p>"""
    tenant_id: NotRequired[
        "capo_quicksight.types.share_point_tenant_id.SharePointTenantId"
    ]
    """<p>The tenant ID for the SharePoint data source.</p>"""
    client_id: NotRequired[
        "capo_quicksight.types.share_point_client_id.SharePointClientId"
    ]
    """<p>The client ID for the SharePoint data source.</p>"""
    auth_type: NotRequired["capo_quicksight.types.auth_type.AuthType"]
    """<p>The authentication type for the SharePoint data source. Valid values include:</p> <ul> <li> <p> <code>TWO_LEGGED_OAUTH</code> – Server-to-server authentication using client credentials that do not require user interaction.</p> </li> <li> <p> <code>THREE_LEGGED_OAUTH</code> – Interactive OAuth that requires user consent.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharePointParameters) -> dict:
    out: dict = {}
    out["SharePointDomain"] = value["share_point_domain"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "auth_type" in value:
        import capo_quicksight.types.auth_type

        out["AuthType"] = capo_quicksight.types.auth_type.serialize_json(
            value["auth_type"]
        )
    return out


def deserialize_json(data: dict) -> SharePointParameters:
    out: SharePointParameters = {}  # type: ignore[typeddict-item]
    if data.get("SharePointDomain") is not None:
        out["share_point_domain"] = data["SharePointDomain"]
    else:
        out["share_point_domain"] = ""
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("AuthType") is not None:
        import capo_quicksight.types.auth_type

        out["auth_type"] = capo_quicksight.types.auth_type.deserialize_json(
            data["AuthType"]
        )
    return out
