"""Generated from Smithy shape ``com.amazonaws.health#AccountEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.account_id
    import capo_health.types.account_tag_set


class AccountEntity(TypedDict, closed=True):
    account_id: NotRequired["capo_health.types.account_id.accountId"]
    """<p>The 12-digit Amazon Web Services account numbers that contains the affected entities.</p>"""
    account_tags: NotRequired["capo_health.types.account_tag_set.AccountTagSet"]
    """<p>A map of tag key-value pairs attached to the affected account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountEntity) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "account_tags" in value:
        import capo_health.types.account_tag_set

        out["accountTags"] = capo_health.types.account_tag_set.serialize_aws_json_1_1(
            value["account_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountEntity:
    out: AccountEntity = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("accountTags") is not None:
        import capo_health.types.account_tag_set

        out["account_tags"] = (
            capo_health.types.account_tag_set.deserialize_aws_json_1_1(
                data["accountTags"]
            )
        )
    return out
