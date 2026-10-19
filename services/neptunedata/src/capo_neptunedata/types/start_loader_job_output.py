"""Generated from Smithy shape ``com.amazonaws.neptunedata#StartLoaderJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.string_valued_map


class StartLoaderJobOutput(TypedDict, closed=True):
    status: "str"
    """<p>The HTTP return code indicating the status of the load job.</p>"""
    payload: "capo_neptunedata.types.string_valued_map.StringValuedMap"
    """<p>Contains a <code>loadId</code> name-value pair that provides an identifier for the load operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartLoaderJobOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    import capo_neptunedata.types.string_valued_map

    out["payload"] = capo_neptunedata.types.string_valued_map.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> StartLoaderJobOutput:
    out: StartLoaderJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("payload") is not None:
        import capo_neptunedata.types.string_valued_map

        out["payload"] = capo_neptunedata.types.string_valued_map.deserialize_json(
            data["payload"]
        )
    else:
        out["payload"] = {}
    return out
