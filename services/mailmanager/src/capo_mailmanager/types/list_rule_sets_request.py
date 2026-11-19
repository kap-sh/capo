"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListRuleSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.page_size
    import capo_mailmanager.types.pagination_token


class ListRuleSetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>"""
    page_size: NotRequired["capo_mailmanager.types.page_size.PageSize"]
    """<p>The maximum number of rule set resources that are returned per call. You can use NextToken to obtain further rule sets.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRuleSetsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRuleSetsRequest:
    out: ListRuleSetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRuleSetsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_cbor(data: dict) -> ListRuleSetsRequest:
    out: ListRuleSetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    return out
