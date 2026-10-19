"""Generated from Smithy shape ``com.amazonaws.transfer#StartDirectoryListingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listing_id
    import capo_transfer.types.output_file_name


class StartDirectoryListingResponse(TypedDict, closed=True):
    listing_id: "capo_transfer.types.listing_id.ListingId"
    """<p>Returns a unique identifier for the directory listing call.</p>"""
    output_file_name: "capo_transfer.types.output_file_name.OutputFileName"
    """<p>Returns the file name where the results are stored. This is a combination of the connector ID and the listing ID: <code>&lt;connector-id&gt;-&lt;listing-id&gt;.json</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDirectoryListingResponse) -> dict:
    out: dict = {}
    out["ListingId"] = value["listing_id"]
    out["OutputFileName"] = value["output_file_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDirectoryListingResponse:
    out: StartDirectoryListingResponse = {}  # type: ignore[typeddict-item]
    if data.get("ListingId") is not None:
        out["listing_id"] = data["ListingId"]
    else:
        out["listing_id"] = ""
    if data.get("OutputFileName") is not None:
        out["output_file_name"] = data["OutputFileName"]
    else:
        out["output_file_name"] = ""
    return out
