"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSetResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeDataSetResponse(TypedDict, closed=True):
    data_set: NotRequired["capo_quicksight.types.data_set.DataSet"]
    """<p>Information on the dataset.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSetResponse) -> dict:
    out: dict = {}
    if "data_set" in value:
        import capo_quicksight.types.data_set

        out["DataSet"] = capo_quicksight.types.data_set.serialize_json(
            value["data_set"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDataSetResponse:
    out: DescribeDataSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("DataSet") is not None:
        import capo_quicksight.types.data_set

        out["data_set"] = capo_quicksight.types.data_set.deserialize_json(
            data["DataSet"]
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeDataSetResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_set" in value:
        import capo_quicksight.types.data_set

        out["data_set"] = capo_quicksight.types.data_set.redact_sensitive(
            value["data_set"]
        )
    return out
