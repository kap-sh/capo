"""Generated from Smithy shape ``com.amazonaws.workmail#ListAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.aliases
    import capo_workmail.types.next_token


class ListAliasesResponse(TypedDict, closed=True):
    aliases: NotRequired["capo_workmail.types.aliases.Aliases"]
    """<p>The entity's paginated aliases.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value is "null" when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesResponse) -> dict:
    out: dict = {}
    if "aliases" in value:
        import capo_workmail.types.aliases

        out["Aliases"] = capo_workmail.types.aliases.serialize_aws_json_1_1(
            value["aliases"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesResponse:
    out: ListAliasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Aliases") is not None:
        import capo_workmail.types.aliases

        out["aliases"] = capo_workmail.types.aliases.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
