"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#GetRoleCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account_access_runtime.types.access_type
    import capo_account_access_runtime.types.session_name
    import capo_account_access_runtime.types.tenant_id


class GetRoleCredentialsRequest(TypedDict, closed=True):
    tenant_id: "capo_account_access_runtime.types.tenant_id.TenantId"
    """<p>The identifier of the tenant that the request applies to. A tenant ID begins with <code>aa-</code> and is 3 to 24 characters long. It can contain lowercase letters, numbers, and hyphens.</p>"""
    role_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the role to retrieve credentials for. You must be entitled to assume this role.</p>"""
    access_type: "capo_account_access_runtime.types.access_type.AccessType"
    """<p>The type of access to request for the role. Specify <code>PROGRAMMATIC_ACCESS</code> to receive access key credentials for use with the CLI or an Amazon Web Services SDK.</p>"""
    session_name: NotRequired[
        "capo_account_access_runtime.types.session_name.SessionName"
    ]
    """<p>An optional name for the role session. The name can be 2 to 64 characters and can contain alphanumeric characters and the following symbols: plus (+), equal (=), comma (,), period (.), at (@), and hyphen (-). The session name appears in CloudTrail logs for the assumed role session.</p>"""
    session_duration: NotRequired["int"]
    """<p>The duration, in seconds, that the returned credentials remain valid. If you don't specify a value, the service uses the default session duration. The maximum value can't exceed the maximum session duration configured for the role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoleCredentialsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRoleCredentialsRequest:
    out: GetRoleCredentialsRequest = {}  # type: ignore[typeddict-item]
    return out
