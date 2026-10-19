"""Generated from Smithy shape ``com.amazonaws.inspector2#FailedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.error_code
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.resource_status
    import capo_inspector2.types.status


class FailedAccount(TypedDict, closed=True):
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    status: NotRequired["capo_inspector2.types.status.Status"]
    """<p>The status of Amazon Inspector for the account.</p>"""
    resource_status: NotRequired["capo_inspector2.types.resource_status.ResourceStatus"]
    """<p>An object detailing which resources Amazon Inspector is enabled to scan for the account.</p>"""
    error_code: "capo_inspector2.types.error_code.ErrorCode"
    """<p>The error code explaining why the account failed to enable Amazon Inspector.</p>"""
    error_message: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The error message received when the account failed to enable Amazon Inspector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedAccount) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "resource_status" in value:
        import capo_inspector2.types.resource_status

        out["resourceStatus"] = capo_inspector2.types.resource_status.serialize_json(
            value["resource_status"]
        )
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedAccount:
    out: FailedAccount = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("resourceStatus") is not None:
        import capo_inspector2.types.resource_status

        out["resource_status"] = capo_inspector2.types.resource_status.deserialize_json(
            data["resourceStatus"]
        )
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
