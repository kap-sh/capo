"""Generated from Smithy shape ``com.amazonaws.iam#GetAccessKeyLastUsedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.access_key_last_used
    import capo_iam.types.existing_user_name_type


class GetAccessKeyLastUsedResponse(TypedDict, closed=True):
    user_name: NotRequired[
        "capo_iam.types.existing_user_name_type.existingUserNameType"
    ]
    """<p>The name of the IAM user that owns this access key.</p> <p/>"""
    access_key_last_used: NotRequired[
        "capo_iam.types.access_key_last_used.AccessKeyLastUsed"
    ]
    """<p>Contains information about the last time the access key was used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccessKeyLastUsedResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    if "access_key_last_used" in value:
        import capo_iam.types.access_key_last_used

        capo_iam.types.access_key_last_used.serialize_query(
            value["access_key_last_used"], pairs, f"{key_prefix}AccessKeyLastUsed"
        )


def deserialize_query(el: Element) -> GetAccessKeyLastUsedResponse:
    out: GetAccessKeyLastUsedResponse = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_access_key_last_used = el.find("AccessKeyLastUsed")
    if child_access_key_last_used is not None:
        import capo_iam.types.access_key_last_used

        out["access_key_last_used"] = (
            capo_iam.types.access_key_last_used.deserialize_query(
                child_access_key_last_used
            )
        )
    return out
