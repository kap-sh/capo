"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDataAccessorsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessors
    import capo_qbusiness.types.next_token1500


class ListDataAccessorsResponse(TypedDict, closed=True):
    data_accessors: NotRequired["capo_qbusiness.types.data_accessors.DataAccessors"]
    """<p>The list of data accessors.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token1500.NextToken1500"]
    """<p>The token to use to retrieve the next set of results, if there are any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAccessorsResponse) -> dict:
    out: dict = {}
    if "data_accessors" in value:
        import capo_qbusiness.types.data_accessors

        out["dataAccessors"] = capo_qbusiness.types.data_accessors.serialize_json(
            value["data_accessors"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAccessorsResponse:
    out: ListDataAccessorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataAccessors") is not None:
        import capo_qbusiness.types.data_accessors

        out["data_accessors"] = capo_qbusiness.types.data_accessors.deserialize_json(
            data["dataAccessors"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListDataAccessorsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_accessors" in value:
        import capo_qbusiness.types.data_accessors

        out["data_accessors"] = capo_qbusiness.types.data_accessors.redact_sensitive(
            value["data_accessors"]
        )
    return out
