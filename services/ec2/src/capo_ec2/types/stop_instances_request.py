"""Generated from Smithy shape ``com.amazonaws.ec2#StopInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_id_string_list


class StopInstancesRequest(TypedDict, closed=True):
    instance_ids: NotRequired[
        "capo_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The IDs of the instances.</p>"""
    hibernate: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Hibernates the instance if the instance was enabled for hibernation at launch. If the instance cannot hibernate successfully, a normal shutdown occurs. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html">Hibernate your Amazon EC2 instance</a> in the <i>Amazon EC2 User Guide</i>.</p> <p> Default: <code>false</code> </p>"""
    skip_os_shutdown: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to bypass the graceful OS shutdown process when the instance is stopped.</p> <important> <p>Bypassing the graceful OS shutdown might result in data loss or corruption (for example, memory contents not flushed to disk or loss of in-flight IOs) or skipped shutdown scripts.</p> </important> <p>Default: <code>false</code> </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    force: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Forces the instance to stop. The instance will first attempt a graceful shutdown, which includes flushing file system caches and metadata. If the graceful shutdown fails to complete within the timeout period, the instance shuts down forcibly without flushing the file system caches and metadata.</p> <p>After using this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html">Troubleshoot Amazon EC2 instance stop issues</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StopInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_string_list

        capo_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceId"
        )
    if "hibernate" in value:
        pairs.append(
            (f"{key_prefix}Hibernate", "true" if value["hibernate"] else "false")
        )
    if "skip_os_shutdown" in value:
        pairs.append(
            (
                f"{key_prefix}SkipOsShutdown",
                "true" if value["skip_os_shutdown"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "force" in value:
        pairs.append((f"{key_prefix}Force", "true" if value["force"] else "false"))


def deserialize_ec2_query(el: Element) -> StopInstancesRequest:
    out: StopInstancesRequest = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceId")
    if child_instance_ids is not None:
        import capo_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            capo_ec2.types.instance_id_string_list.deserialize_ec2_query(
                child_instance_ids
            )
        )
    child_hibernate = el.find("Hibernate")
    if child_hibernate is not None:
        out["hibernate"] = (child_hibernate.text or "").lower() == "true"
    child_skip_os_shutdown = el.find("SkipOsShutdown")
    if child_skip_os_shutdown is not None:
        out["skip_os_shutdown"] = (child_skip_os_shutdown.text or "").lower() == "true"
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_force = el.find("force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    return out
