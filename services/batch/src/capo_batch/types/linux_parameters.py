"""Generated from Smithy shape ``com.amazonaws.batch#LinuxParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.devices_list
    import capo_batch.types.integer
    import capo_batch.types.tmpfs_list


class LinuxParameters(TypedDict, closed=True):
    devices: NotRequired["capo_batch.types.devices_list.DevicesList"]
    """<p>Any of the host devices to expose to the container. This parameter maps to <code>Devices</code> in the <a href="https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate">Create a container</a> section of the <a href="https://docs.docker.com/engine/api/latest/">Docker Remote API</a> and the <code>--device</code> option to <a href="https://docs.docker.com/engine/reference/run/">docker run</a>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.</p> </note>"""
    init_process_enabled: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>If true, run an <code>init</code> process inside the container that forwards signals and reaps processes. This parameter maps to the <code>--init</code> option to <a href="https://docs.docker.com/engine/reference/run/">docker run</a>. This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version | grep "Server API version"</code> </p>"""
    shared_memory_size: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The value for the size (in MiB) of the <code>/dev/shm</code> volume. This parameter maps to the <code>--shm-size</code> option to <a href="https://docs.docker.com/engine/reference/run/">docker run</a>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.</p> </note>"""
    tmpfs: NotRequired["capo_batch.types.tmpfs_list.TmpfsList"]
    """<p>The container path, mount options, and size (in MiB) of the <code>tmpfs</code> mount. This parameter maps to the <code>--tmpfs</code> option to <a href="https://docs.docker.com/engine/reference/run/">docker run</a>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide this parameter for this resource type.</p> </note>"""
    max_swap: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The total amount of swap memory (in MiB) a container can use. This parameter is translated to the <code>--memory-swap</code> option to <a href="https://docs.docker.com/engine/reference/run/">docker run</a> where the value is the sum of the container memory plus the <code>maxSwap</code> value. For more information, see <a href="https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details"> <code>--memory-swap</code> details</a> in the Docker documentation.</p> <p>If a <code>maxSwap</code> value of <code>0</code> is specified, the container doesn't use swap. Accepted values are <code>0</code> or any positive integer. If the <code>maxSwap</code> parameter is omitted, the container doesn't use the swap configuration for the container instance on which it runs. A <code>maxSwap</code> value must be set for the <code>swappiness</code> parameter to be used.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.</p> </note>"""
    swappiness: NotRequired["capo_batch.types.integer.Integer"]
    """<p>You can use this parameter to tune a container's memory swappiness behavior. A <code>swappiness</code> value of <code>0</code> causes swapping to not occur unless absolutely necessary. A <code>swappiness</code> value of <code>100</code> causes pages to be swapped aggressively. Valid values are whole numbers between <code>0</code> and <code>100</code>. If the <code>swappiness</code> parameter isn't specified, a default value of <code>60</code> is used. If a value isn't specified for <code>maxSwap</code>, then this parameter is ignored. If <code>maxSwap</code> is set to 0, the container doesn't use swap. This parameter maps to the <code>--memory-swappiness</code> option to <a href="https://docs.docker.com/engine/reference/run/">docker run</a>.</p> <p>Consider the following when you use a per-container swap configuration.</p> <ul> <li> <p>Swap space must be enabled and allocated on the container instance for the containers to use.</p> <note> <p>By default, the Amazon ECS optimized AMIs don't have swap enabled. You must enable swap on the instance to use this feature. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html">Instance store swap volumes</a> in the <i>Amazon EC2 User Guide for Linux Instances</i> or <a href="http://aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/">How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file?</a> </p> </note> </li> <li> <p>The swap space parameters are only supported for job definitions using EC2 resources.</p> </li> <li> <p>If the <code>maxSwap</code> and <code>swappiness</code> parameters are omitted from a job definition, each container has a default <code>swappiness</code> value of 60. Moreover, the total swap usage is limited to two times the memory reservation of the container.</p> </li> </ul> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinuxParameters) -> dict:
    out: dict = {}
    if "devices" in value:
        import capo_batch.types.devices_list

        out["devices"] = capo_batch.types.devices_list.serialize_json(value["devices"])
    if "init_process_enabled" in value:
        out["initProcessEnabled"] = value["init_process_enabled"]
    if "shared_memory_size" in value:
        out["sharedMemorySize"] = value["shared_memory_size"]
    if "tmpfs" in value:
        import capo_batch.types.tmpfs_list

        out["tmpfs"] = capo_batch.types.tmpfs_list.serialize_json(value["tmpfs"])
    if "max_swap" in value:
        out["maxSwap"] = value["max_swap"]
    if "swappiness" in value:
        out["swappiness"] = value["swappiness"]
    return out


def deserialize_json(data: dict) -> LinuxParameters:
    out: LinuxParameters = {}  # type: ignore[typeddict-item]
    if data.get("devices") is not None:
        import capo_batch.types.devices_list

        out["devices"] = capo_batch.types.devices_list.deserialize_json(data["devices"])
    if data.get("initProcessEnabled") is not None:
        out["init_process_enabled"] = data["initProcessEnabled"]
    if data.get("sharedMemorySize") is not None:
        out["shared_memory_size"] = data["sharedMemorySize"]
    if data.get("tmpfs") is not None:
        import capo_batch.types.tmpfs_list

        out["tmpfs"] = capo_batch.types.tmpfs_list.deserialize_json(data["tmpfs"])
    if data.get("maxSwap") is not None:
        out["max_swap"] = data["maxSwap"]
    if data.get("swappiness") is not None:
        out["swappiness"] = data["swappiness"]
    return out
