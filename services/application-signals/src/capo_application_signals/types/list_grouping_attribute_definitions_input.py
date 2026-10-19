"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListGroupingAttributeDefinitionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.next_token


class ListGroupingAttributeDefinitionsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of grouping attribute definitions.</p>"""
    aws_account_id: NotRequired[
        "capo_application_signals.types.aws_account_id.AwsAccountId"
    ]
    """<p>The Amazon Web Services account ID to retrieve grouping attribute definitions for. Use this when accessing grouping configurations from a different account in cross-account monitoring scenarios.</p>"""
    include_linked_accounts: NotRequired["bool"]
    """<p>If you are using this operation in a monitoring account, specify <code>true</code> to include grouping attributes from source accounts in the returned data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingAttributeDefinitionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGroupingAttributeDefinitionsInput:
    out: ListGroupingAttributeDefinitionsInput = {}  # type: ignore[typeddict-item]
    return out
