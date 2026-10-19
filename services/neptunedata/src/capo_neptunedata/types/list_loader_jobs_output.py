"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListLoaderJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptunedata.types.loader_id_result


class ListLoaderJobsOutput(TypedDict, closed=True):
    status: "str"
    """<p>Returns the status of the job list request.</p>"""
    payload: "capo_neptunedata.types.loader_id_result.LoaderIdResult"
    """<p>The requested list of job IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLoaderJobsOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    import capo_neptunedata.types.loader_id_result

    out["payload"] = capo_neptunedata.types.loader_id_result.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> ListLoaderJobsOutput:
    out: ListLoaderJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("payload") is not None:
        import capo_neptunedata.types.loader_id_result

        out["payload"] = capo_neptunedata.types.loader_id_result.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("ListLoaderJobsOutput.payload required")
    return out
