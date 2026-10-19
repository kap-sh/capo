"""Generated from Smithy shape ``com.amazonaws.outposts#StartCapacityTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_outposts.types.asset_id_input
    import capo_outposts.types.dry_run
    import capo_outposts.types.instances_to_exclude
    import capo_outposts.types.order_id
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.requested_instance_pools
    import capo_outposts.types.task_action_on_blocking_instances


class StartCapacityTaskInput(TypedDict, closed=True):
    outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outposts associated with the specified capacity task.</p>"""
    order_id: NotRequired["capo_outposts.types.order_id.OrderId"]
    """<p>The ID of the Amazon Web Services Outposts order associated with the specified capacity task.</p>"""
    asset_id: NotRequired["capo_outposts.types.asset_id_input.AssetIdInput"]
    """<p>The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    instance_pools: (
        "capo_outposts.types.requested_instance_pools.RequestedInstancePools"
    )
    """<p>The instance pools specified in the capacity task.</p>"""
    instances_to_exclude: NotRequired[
        "capo_outposts.types.instances_to_exclude.InstancesToExclude"
    ]
    """<p>List of user-specified running instances that must not be stopped in order to free up the capacity needed to run the capacity task.</p>"""
    dry_run: NotRequired["capo_outposts.types.dry_run.DryRun"]
    """<p>You can request a dry run to determine if the instance type and instance size changes is above or below available instance capacity. Requesting a dry run does not make any changes to your plan.</p>"""
    task_action_on_blocking_instances: NotRequired[
        "capo_outposts.types.task_action_on_blocking_instances.TaskActionOnBlockingInstances"
    ]
    """<p>Specify one of the following options in case an instance is blocking the capacity task from running.</p> <ul> <li> <p> <code>WAIT_FOR_EVACUATION</code> - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.</p> </li> <li> <p> <code>FAIL_TASK</code> - The capacity task fails.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCapacityTaskInput) -> dict:
    out: dict = {}
    if "order_id" in value:
        out["OrderId"] = value["order_id"]
    if "asset_id" in value:
        out["AssetId"] = value["asset_id"]
    import capo_outposts.types.requested_instance_pools

    out["InstancePools"] = capo_outposts.types.requested_instance_pools.serialize_json(
        value["instance_pools"]
    )
    if "instances_to_exclude" in value:
        import capo_outposts.types.instances_to_exclude

        out["InstancesToExclude"] = (
            capo_outposts.types.instances_to_exclude.serialize_json(
                value["instances_to_exclude"]
            )
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "task_action_on_blocking_instances" in value:
        import capo_outposts.types.task_action_on_blocking_instances

        out["TaskActionOnBlockingInstances"] = (
            capo_outposts.types.task_action_on_blocking_instances.serialize_json(
                value["task_action_on_blocking_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartCapacityTaskInput:
    out: StartCapacityTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("OrderId") is not None:
        out["order_id"] = data["OrderId"]
    if data.get("AssetId") is not None:
        out["asset_id"] = data["AssetId"]
    if data.get("InstancePools") is not None:
        import capo_outposts.types.requested_instance_pools

        out["instance_pools"] = (
            capo_outposts.types.requested_instance_pools.deserialize_json(
                data["InstancePools"]
            )
        )
    else:
        raise DeserializationError("StartCapacityTaskInput.instance_pools required")
    if data.get("InstancesToExclude") is not None:
        import capo_outposts.types.instances_to_exclude

        out["instances_to_exclude"] = (
            capo_outposts.types.instances_to_exclude.deserialize_json(
                data["InstancesToExclude"]
            )
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("TaskActionOnBlockingInstances") is not None:
        import capo_outposts.types.task_action_on_blocking_instances

        out["task_action_on_blocking_instances"] = (
            capo_outposts.types.task_action_on_blocking_instances.deserialize_json(
                data["TaskActionOnBlockingInstances"]
            )
        )
    return out
