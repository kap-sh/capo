"""Generated from Smithy shape ``com.amazonaws.mailmanager#StartArchiveSearchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.search_id


class StartArchiveSearchResponse(TypedDict, closed=True):
    search_id: NotRequired["capo_mailmanager.types.search_id.SearchId"]
    """<p>The unique identifier for the initiated search job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartArchiveSearchResponse) -> dict:
    out: dict = {}
    if "search_id" in value:
        out["SearchId"] = value["search_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartArchiveSearchResponse:
    out: StartArchiveSearchResponse = {}  # type: ignore[typeddict-item]
    if data.get("SearchId") is not None:
        out["search_id"] = data["SearchId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartArchiveSearchResponse) -> dict:
    out: dict = {}
    if "search_id" in value:
        out["SearchId"] = value["search_id"]
    return out


def deserialize_cbor(data: dict) -> StartArchiveSearchResponse:
    out: StartArchiveSearchResponse = {}  # type: ignore[typeddict-item]
    if data.get("SearchId") is not None:
        out["search_id"] = data["SearchId"]
    return out
