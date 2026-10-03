"""Generated from Smithy shape ``com.amazonaws.pcs#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pcs.types.cluster_slurm_configuration
    import capo_pcs.types.cluster_status
    import capo_pcs.types.endpoints
    import capo_pcs.types.error_info_list
    import capo_pcs.types.networking
    import capo_pcs.types.scheduler
    import capo_pcs.types.size


class Cluster(TypedDict, closed=True):
    name: "str"
    """<p>The name that identifies the cluster.</p>"""
    id: "str"
    """<p>The generated unique ID of the cluster.</p>"""
    arn: "str"
    """<p>The unique Amazon Resource Name (ARN) of the cluster.</p>"""
    status: "capo_pcs.types.cluster_status.ClusterStatus"
    """<p>The provisioning status of the cluster.</p> <note> <p>The provisioning status doesn't indicate the overall health of the cluster.</p> </note> <important> <p>The resource enters the <code>SUSPENDING</code> and <code>SUSPENDED</code> states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is <code>SUSPENDED</code>. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html">Frequently asked questions about Slurm versions in PCS</a> in the <i>PCS User Guide</i>.</p> </important>"""
    created_at: "datetime.datetime"
    """<p>The date and time the resource was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the resource was modified.</p>"""
    scheduler: "capo_pcs.types.scheduler.Scheduler"
    size: "capo_pcs.types.size.Size"
    """<p>The size of the cluster.</p> <ul> <li> <p> <code>SMALL</code>: 32 compute nodes and 256 jobs</p> </li> <li> <p> <code>MEDIUM</code>: 512 compute nodes and 8192 jobs</p> </li> <li> <p> <code>LARGE</code>: 2048 compute nodes and 16,384 jobs</p> </li> </ul>"""
    slurm_configuration: NotRequired[
        "capo_pcs.types.cluster_slurm_configuration.ClusterSlurmConfiguration"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    networking: "capo_pcs.types.networking.Networking"
    endpoints: NotRequired["capo_pcs.types.endpoints.Endpoints"]
    """<p>The list of endpoints available for interaction with the scheduler.</p>"""
    error_info: NotRequired["capo_pcs.types.error_info_list.ErrorInfoList"]
    """<p>The list of errors that occurred during cluster provisioning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Cluster) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_pcs.types.cluster_status

    out["status"] = capo_pcs.types.cluster_status.serialize_aws_json_1_0(
        value["status"]
    )
    import capo_pcs._protocol.serialize

    out["createdAt"] = capo_pcs._protocol.serialize.fmt_date_time(value["created_at"])
    import capo_pcs._protocol.serialize

    out["modifiedAt"] = capo_pcs._protocol.serialize.fmt_date_time(value["modified_at"])
    import capo_pcs.types.scheduler

    out["scheduler"] = capo_pcs.types.scheduler.serialize_aws_json_1_0(
        value["scheduler"]
    )
    import capo_pcs.types.size

    out["size"] = capo_pcs.types.size.serialize_aws_json_1_0(value["size"])
    if "slurm_configuration" in value:
        import capo_pcs.types.cluster_slurm_configuration

        out["slurmConfiguration"] = (
            capo_pcs.types.cluster_slurm_configuration.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    import capo_pcs.types.networking

    out["networking"] = capo_pcs.types.networking.serialize_aws_json_1_0(
        value["networking"]
    )
    if "endpoints" in value:
        import capo_pcs.types.endpoints

        out["endpoints"] = capo_pcs.types.endpoints.serialize_aws_json_1_0(
            value["endpoints"]
        )
    if "error_info" in value:
        import capo_pcs.types.error_info_list

        out["errorInfo"] = capo_pcs.types.error_info_list.serialize_aws_json_1_0(
            value["error_info"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Cluster.name required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Cluster.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Cluster.arn required")
    if data.get("status") is not None:
        import capo_pcs.types.cluster_status

        out["status"] = capo_pcs.types.cluster_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("Cluster.status required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("Cluster.created_at required")
    if data.get("modifiedAt") is not None:
        import datetime

        out["modified_at"] = datetime.datetime.fromisoformat(
            data["modifiedAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("Cluster.modified_at required")
    if data.get("scheduler") is not None:
        import capo_pcs.types.scheduler

        out["scheduler"] = capo_pcs.types.scheduler.deserialize_aws_json_1_0(
            data["scheduler"]
        )
    else:
        raise DeserializationError("Cluster.scheduler required")
    if data.get("size") is not None:
        import capo_pcs.types.size

        out["size"] = capo_pcs.types.size.deserialize_aws_json_1_0(data["size"])
    else:
        raise DeserializationError("Cluster.size required")
    if data.get("slurmConfiguration") is not None:
        import capo_pcs.types.cluster_slurm_configuration

        out["slurm_configuration"] = (
            capo_pcs.types.cluster_slurm_configuration.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if data.get("networking") is not None:
        import capo_pcs.types.networking

        out["networking"] = capo_pcs.types.networking.deserialize_aws_json_1_0(
            data["networking"]
        )
    else:
        raise DeserializationError("Cluster.networking required")
    if data.get("endpoints") is not None:
        import capo_pcs.types.endpoints

        out["endpoints"] = capo_pcs.types.endpoints.deserialize_aws_json_1_0(
            data["endpoints"]
        )
    if data.get("errorInfo") is not None:
        import capo_pcs.types.error_info_list

        out["error_info"] = capo_pcs.types.error_info_list.deserialize_aws_json_1_0(
            data["errorInfo"]
        )
    return out
