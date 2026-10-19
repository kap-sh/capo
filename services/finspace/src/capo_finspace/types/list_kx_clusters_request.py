"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_cluster_type
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.max_results
    import capo_finspace.types.pagination_token


class ListKxClustersRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    cluster_type: NotRequired["capo_finspace.types.kx_cluster_type.KxClusterType"]
    """<p>Specifies the type of KDB database that is being created. The following types are available: </p> <ul> <li> <p>HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.</p> </li> <li> <p>RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the <code>savedownStorageConfiguration</code> parameter.</p> </li> <li> <p>GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.</p> </li> <li> <p>GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only <code>SINGLE</code> AZ mode.</p> </li> <li> <p>Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.</p> </li> </ul>"""
    max_results: NotRequired["capo_finspace.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in this request.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxClustersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxClustersRequest:
    out: ListKxClustersRequest = {}  # type: ignore[typeddict-item]
    return out
