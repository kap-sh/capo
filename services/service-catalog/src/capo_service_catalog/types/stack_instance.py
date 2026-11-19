"""Generated from Smithy shape ``com.amazonaws.servicecatalog#StackInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.account_id
    import capo_service_catalog.types.region
    import capo_service_catalog.types.stack_instance_status


class StackInstance(TypedDict, closed=True):
    account: NotRequired["capo_service_catalog.types.account_id.AccountId"]
    """<p>The name of the Amazon Web Services account that the stack instance is associated with.</p>"""
    region: NotRequired["capo_service_catalog.types.region.Region"]
    """<p>The name of the Amazon Web Services Region that the stack instance is associated with.</p>"""
    stack_instance_status: NotRequired[
        "capo_service_catalog.types.stack_instance_status.StackInstanceStatus"
    ]
    """<p>The status of the stack instance, in terms of its synchronization with its associated stack set. </p> <ul> <li> <p> <code>INOPERABLE</code>: A <code>DeleteStackInstances</code> operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further <code>UpdateStackSet</code> operations. You might need to perform a <code>DeleteStackInstances</code> operation, with <code>RetainStacks</code> set to true, to delete the stack instance, and then delete the stack manually. </p> </li> <li> <p> <code>OUTDATED</code>: The stack isn't currently up to date with the stack set because either the associated stack failed during a <code>CreateStackSet</code> or <code>UpdateStackSet</code> operation, or the stack was part of a <code>CreateStackSet</code> or <code>UpdateStackSet</code> operation that failed or was stopped before the stack was created or updated.</p> </li> <li> <p> <code>CURRENT</code>: The stack is currently up to date with the stack set.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackInstance) -> dict:
    out: dict = {}
    if "account" in value:
        out["Account"] = value["account"]
    if "region" in value:
        out["Region"] = value["region"]
    if "stack_instance_status" in value:
        import capo_service_catalog.types.stack_instance_status

        out["StackInstanceStatus"] = (
            capo_service_catalog.types.stack_instance_status.serialize_aws_json_1_1(
                value["stack_instance_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StackInstance:
    out: StackInstance = {}  # type: ignore[typeddict-item]
    if data.get("Account") is not None:
        out["account"] = data["Account"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("StackInstanceStatus") is not None:
        import capo_service_catalog.types.stack_instance_status

        out["stack_instance_status"] = (
            capo_service_catalog.types.stack_instance_status.deserialize_aws_json_1_1(
                data["StackInstanceStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StackInstance) -> dict:
    out: dict = {}
    if "account" in value:
        out["Account"] = value["account"]
    if "region" in value:
        out["Region"] = value["region"]
    if "stack_instance_status" in value:
        import capo_service_catalog.types.stack_instance_status

        out["StackInstanceStatus"] = (
            capo_service_catalog.types.stack_instance_status.serialize_cbor(
                value["stack_instance_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StackInstance:
    out: StackInstance = {}  # type: ignore[typeddict-item]
    if data.get("Account") is not None:
        out["account"] = data["Account"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("StackInstanceStatus") is not None:
        import capo_service_catalog.types.stack_instance_status

        out["stack_instance_status"] = (
            capo_service_catalog.types.stack_instance_status.deserialize_cbor(
                data["StackInstanceStatus"]
            )
        )
    return out
