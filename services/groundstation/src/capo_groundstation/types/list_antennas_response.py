"""Generated from Smithy shape ``com.amazonaws.groundstation#ListAntennasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.antenna_list
    import capo_groundstation.types.pagination_token


class ListAntennasResponse(TypedDict, closed=True):
    antenna_list: "capo_groundstation.types.antenna_list.AntennaList"
    """<p>List of antennas.</p>"""
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token to be used in a subsequent <code>ListAntennas</code> call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAntennasResponse) -> dict:
    out: dict = {}
    import capo_groundstation.types.antenna_list

    out["antennaList"] = capo_groundstation.types.antenna_list.serialize_json(
        value["antenna_list"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAntennasResponse:
    out: ListAntennasResponse = {}  # type: ignore[typeddict-item]
    if data.get("antennaList") is not None:
        import capo_groundstation.types.antenna_list

        out["antenna_list"] = capo_groundstation.types.antenna_list.deserialize_json(
            data["antennaList"]
        )
    else:
        out["antenna_list"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
