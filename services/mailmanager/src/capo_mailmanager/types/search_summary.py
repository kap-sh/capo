"""Generated from Smithy shape ``com.amazonaws.mailmanager#SearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.search_id
    import capo_mailmanager.types.search_status


class SearchSummary(TypedDict, closed=True):
    search_id: NotRequired["capo_mailmanager.types.search_id.SearchId"]
    """<p>The unique identifier of the search job.</p>"""
    status: NotRequired["capo_mailmanager.types.search_status.SearchStatus"]
    """<p>The current status of the search job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchSummary) -> dict:
    out: dict = {}
    if "search_id" in value:
        out["SearchId"] = value["search_id"]
    if "status" in value:
        import capo_mailmanager.types.search_status

        out["Status"] = capo_mailmanager.types.search_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchSummary:
    out: SearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("SearchId") is not None:
        out["search_id"] = data["SearchId"]
    if data.get("Status") is not None:
        import capo_mailmanager.types.search_status

        out["status"] = capo_mailmanager.types.search_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchSummary) -> dict:
    out: dict = {}
    if "search_id" in value:
        out["SearchId"] = value["search_id"]
    if "status" in value:
        import capo_mailmanager.types.search_status

        out["Status"] = capo_mailmanager.types.search_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> SearchSummary:
    out: SearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("SearchId") is not None:
        out["search_id"] = data["SearchId"]
    if data.get("Status") is not None:
        import capo_mailmanager.types.search_status

        out["status"] = capo_mailmanager.types.search_status.deserialize_cbor(
            data["Status"]
        )
    return out
