"""Generated from Smithy shape ``com.amazonaws.fms#GetAdminScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id


class GetAdminScopeRequest(TypedDict, closed=True):
    admin_account: "capo_fms.types.aws_account_id.AWSAccountId"
    """<p>The administrator account that you want to get the details for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdminScopeRequest) -> dict:
    out: dict = {}
    out["AdminAccount"] = value["admin_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdminScopeRequest:
    out: GetAdminScopeRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccount") is not None:
        out["admin_account"] = data["AdminAccount"]
    else:
        out["admin_account"] = ""
    return out
