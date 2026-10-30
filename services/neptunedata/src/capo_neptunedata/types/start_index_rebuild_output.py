"""Generated from Smithy shape ``com.amazonaws.neptunedata#StartIndexRebuildOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.rebuild_concurrency
    import capo_neptunedata.types.rebuild_status
    import capo_neptunedata.types.scope
    import capo_neptunedata.types.write_buffer_size


class StartIndexRebuildOutput(TypedDict, closed=True):
    status: "capo_neptunedata.types.rebuild_status.RebuildStatus"
    """<p>The current status of the rebuild operation. See <code>RebuildStatus</code> for possible values.</p>"""
    rebuild_id: "str"
    """<p>The unique identifier for the index rebuild job. Use this ID with the GetIndexRebuildStatus operation to check the progress of the rebuild.</p>"""
    scope: "capo_neptunedata.types.scope.Scope"
    """<p>The scope of the rebuild operation that was requested. See <code>Scope</code> for possible values: <code>ALL</code>, <code>QUADS</code>, or <code>DICTIONARIES</code>.</p>"""
    concurrency: "capo_neptunedata.types.rebuild_concurrency.RebuildConcurrency"
    """<p>The effective concurrency used for this rebuild. This is the value supplied in the request, capped at the number of vCPUs on the writer instance.</p>"""
    write_buffer_size: "capo_neptunedata.types.write_buffer_size.WriteBufferSize"
    """<p>The <code>WriteBufferSize</code> applied to this rebuild. See the <code>WriteBufferSize</code> enum for possible values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartIndexRebuildOutput) -> dict:
    out: dict = {}
    import capo_neptunedata.types.rebuild_status

    out["status"] = capo_neptunedata.types.rebuild_status.serialize_json(
        value["status"]
    )
    out["rebuildId"] = value["rebuild_id"]
    import capo_neptunedata.types.scope

    out["scope"] = capo_neptunedata.types.scope.serialize_json(value["scope"])
    out["concurrency"] = value["concurrency"]
    import capo_neptunedata.types.write_buffer_size

    out["writeBufferSize"] = capo_neptunedata.types.write_buffer_size.serialize_json(
        value["write_buffer_size"]
    )
    return out


def deserialize_json(data: dict) -> StartIndexRebuildOutput:
    out: StartIndexRebuildOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_neptunedata.types.rebuild_status

        out["status"] = capo_neptunedata.types.rebuild_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_neptunedata.types.rebuild_status.RebuildStatus", ""
        )
    if data.get("rebuildId") is not None:
        out["rebuild_id"] = data["rebuildId"]
    else:
        out["rebuild_id"] = ""
    if data.get("scope") is not None:
        import capo_neptunedata.types.scope

        out["scope"] = capo_neptunedata.types.scope.deserialize_json(data["scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_neptunedata.types.scope.Scope", "")
    if data.get("concurrency") is not None:
        out["concurrency"] = data["concurrency"]
    else:
        out["concurrency"] = 0
    if data.get("writeBufferSize") is not None:
        import capo_neptunedata.types.write_buffer_size

        out["write_buffer_size"] = (
            capo_neptunedata.types.write_buffer_size.deserialize_json(
                data["writeBufferSize"]
            )
        )
    else:
        import typing

        out["write_buffer_size"] = typing.cast(
            "capo_neptunedata.types.write_buffer_size.WriteBufferSize", ""
        )
    return out
