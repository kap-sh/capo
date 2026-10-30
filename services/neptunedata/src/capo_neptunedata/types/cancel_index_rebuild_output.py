"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelIndexRebuildOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.rebuild_concurrency
    import capo_neptunedata.types.rebuild_status
    import capo_neptunedata.types.write_buffer_size


class CancelIndexRebuildOutput(TypedDict, closed=True):
    status: "capo_neptunedata.types.rebuild_status.RebuildStatus"
    """<p>The status of the cancellation request.</p>"""
    concurrency: "capo_neptunedata.types.rebuild_concurrency.RebuildConcurrency"
    """<p>The concurrency of the rebuild being cancelled, echoed from the original <code>StartIndexRebuild</code> request.</p>"""
    write_buffer_size: "capo_neptunedata.types.write_buffer_size.WriteBufferSize"
    """<p>The <code>WriteBufferSize</code> of the rebuild being cancelled, echoed from the original <code>StartIndexRebuild</code> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelIndexRebuildOutput) -> dict:
    out: dict = {}
    import capo_neptunedata.types.rebuild_status

    out["status"] = capo_neptunedata.types.rebuild_status.serialize_json(
        value["status"]
    )
    out["concurrency"] = value["concurrency"]
    import capo_neptunedata.types.write_buffer_size

    out["writeBufferSize"] = capo_neptunedata.types.write_buffer_size.serialize_json(
        value["write_buffer_size"]
    )
    return out


def deserialize_json(data: dict) -> CancelIndexRebuildOutput:
    out: CancelIndexRebuildOutput = {}  # type: ignore[typeddict-item]
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
