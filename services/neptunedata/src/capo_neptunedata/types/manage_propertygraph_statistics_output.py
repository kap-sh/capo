"""Generated from Smithy shape ``com.amazonaws.neptunedata#ManagePropertygraphStatisticsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.refresh_statistics_id_map


class ManagePropertygraphStatisticsOutput(TypedDict, closed=True):
    status: "str"
    """<p>The HTTP return code of the request. If the request succeeded, the code is 200.</p>"""
    payload: NotRequired[
        "capo_neptunedata.types.refresh_statistics_id_map.RefreshStatisticsIdMap"
    ]
    """<p>This is only returned for refresh mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagePropertygraphStatisticsOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "payload" in value:
        import capo_neptunedata.types.refresh_statistics_id_map

        out["payload"] = (
            capo_neptunedata.types.refresh_statistics_id_map.serialize_json(
                value["payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagePropertygraphStatisticsOutput:
    out: ManagePropertygraphStatisticsOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("payload") is not None:
        import capo_neptunedata.types.refresh_statistics_id_map

        out["payload"] = (
            capo_neptunedata.types.refresh_statistics_id_map.deserialize_json(
                data["payload"]
            )
        )
    return out
