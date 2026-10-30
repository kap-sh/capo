"""Generated from Smithy shape ``com.amazonaws.neptunedata#StartIndexRebuildInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.rebuild_concurrency
    import capo_neptunedata.types.scope
    import capo_neptunedata.types.write_buffer_size


class StartIndexRebuildInput(TypedDict, closed=True):
    scope: NotRequired["capo_neptunedata.types.scope.Scope"]
    """<p>Specifies the scope of the rebuild operation. Possible values are:</p> <ul> <li> <p> <code>ALL</code> - Rebuild all (quads and dictionaries). This is the default if not specified.</p> </li> <li> <p> <code>QUADS</code> - Rebuild only the quad indexes. </p> </li> <li> <p> <code>DICTIONARIES</code> - Rebuild only the dictionaries.</p> </li> </ul>"""
    concurrency: NotRequired[
        "capo_neptunedata.types.rebuild_concurrency.RebuildConcurrency"
    ]
    """<p>The number of concurrent indexes to rebuild in parallel. If not specified, defaults to <code>1</code>.</p> <p>Valid values are between <code>1</code> and the number of vCPUs available on the writer instance. If the value exceeds the available vCPUs, it is capped at the maximum instead of returning an <code>InvalidParameterException</code>. The effective (capped) value is returned in the response.</p> <p>Higher concurrency can shorten the overall rebuild, but also increases CPU and I/O load during the operation.</p>"""
    write_buffer_size: NotRequired[
        "capo_neptunedata.types.write_buffer_size.WriteBufferSize"
    ]
    """<p>Controls the buffer size used for tracking concurrent write operations during the index rebuild. If your database has high write traffic during the rebuild, a larger buffer prevents the operation from failing due to buffer overflow. Possible values are:</p> <ul> <li> <p> <code>LOW</code> - Suitable for databases with light to moderate write activity. This is the default.</p> </li> <li> <p> <code>MEDIUM</code> - Recommended for databases with sustained write traffic or bulk loading.</p> </li> <li> <p> <code>HIGH</code> - Use when rebuilding indexes during heavy write workloads or continuous bulk data ingestion.</p> </li> </ul> <p>If your rebuild fails and you are actively writing data to the database, retry with a higher <code>writeBufferSize</code> value. For bulk load operations, consider using <code>HIGH</code>.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the SDK automatically generates one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartIndexRebuildInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartIndexRebuildInput:
    out: StartIndexRebuildInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
