"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#ListRolesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account_access_runtime.types.tenant_id
    import capo_account_access_runtime.types.token


class ListRolesRequest(TypedDict, closed=True):
    tenant_id: "capo_account_access_runtime.types.tenant_id.TenantId"
    """<p>The identifier of the tenant whose roles you want to list. A tenant ID begins with <code>aa-</code> and is 3 to 24 characters long. It can contain lowercase letters, numbers, and hyphens.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of roles to return in a single response. If more roles are available than the specified value, the response includes a <code>nextToken</code> value that you can use to retrieve the next page of results. If you don't specify a value, the service uses a default page size.</p>"""
    next_token: NotRequired["capo_account_access_runtime.types.token.Token"]
    """<p>The pagination token from a previous <code>ListRoles</code> response. Use it to retrieve the next page of results. Omit this parameter on the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRolesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRolesRequest:
    out: ListRolesRequest = {}  # type: ignore[typeddict-item]
    return out
