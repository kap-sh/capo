"""Generated from Smithy shape ``com.amazonaws.sts#GetCallerIdentityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.account_type
    import capo_sts.types.arn_type
    import capo_sts.types.user_id_type


class GetCallerIdentityResponse(TypedDict, closed=True):
    user_id: NotRequired["capo_sts.types.user_id_type.userIdType"]
    """<p>The unique identifier of the calling entity. The exact value depends on the type of entity that is making the call. The values returned are those listed in the <b>aws:userid</b> column in the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#principaltable">Principal table</a> found on the <b>Policy Variables</b> reference page in the <i>IAM User Guide</i>.</p>"""
    account: NotRequired["capo_sts.types.account_type.accountType"]
    """<p>The Amazon Web Services account ID number of the account that owns or contains the calling entity.</p>"""
    arn: NotRequired["capo_sts.types.arn_type.arnType"]
    """<p>The Amazon Web Services ARN associated with the calling entity.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetCallerIdentityResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_id" in value:
        pairs.append((f"{key_prefix}UserId", str(value["user_id"])))
    if "account" in value:
        pairs.append((f"{key_prefix}Account", str(value["account"])))
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))


def deserialize_query(el: Element) -> GetCallerIdentityResponse:
    out: GetCallerIdentityResponse = {}  # type: ignore[typeddict-item]
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_account = el.find("Account")
    if child_account is not None:
        out["account"] = str(child_account.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
