"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyReservedInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_configuration_list
    import capo_ec2.types.reserved_instances_id_string_list
    import capo_ec2.types.string


class ModifyReservedInstancesRequest(TypedDict, closed=True):
    reserved_instances_ids: NotRequired[
        "capo_ec2.types.reserved_instances_id_string_list.ReservedInstancesIdStringList"
    ]
    """<p>The IDs of the Reserved Instances to modify.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive token you provide to ensure idempotency of your modification request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    target_configurations: NotRequired[
        "capo_ec2.types.reserved_instances_configuration_list.ReservedInstancesConfigurationList"
    ]
    """<p>The configuration settings for the Reserved Instances to modify.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyReservedInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_instances_ids" in value:
        import capo_ec2.types.reserved_instances_id_string_list

        capo_ec2.types.reserved_instances_id_string_list.serialize_ec2_query(
            value["reserved_instances_ids"], pairs, f"{key_prefix}ReservedInstancesId"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "target_configurations" in value:
        import capo_ec2.types.reserved_instances_configuration_list

        capo_ec2.types.reserved_instances_configuration_list.serialize_ec2_query(
            value["target_configurations"],
            pairs,
            f"{key_prefix}ReservedInstancesConfigurationSetItemType",
        )


def deserialize_ec2_query(el: Element) -> ModifyReservedInstancesRequest:
    out: ModifyReservedInstancesRequest = {}  # type: ignore[typeddict-item]
    child_reserved_instances_ids = el.find("ReservedInstancesId")
    if child_reserved_instances_ids is not None:
        import capo_ec2.types.reserved_instances_id_string_list

        out["reserved_instances_ids"] = (
            capo_ec2.types.reserved_instances_id_string_list.deserialize_ec2_query(
                child_reserved_instances_ids
            )
        )
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_target_configurations = el.find("ReservedInstancesConfigurationSetItemType")
    if child_target_configurations is not None:
        import capo_ec2.types.reserved_instances_configuration_list

        out["target_configurations"] = (
            capo_ec2.types.reserved_instances_configuration_list.deserialize_ec2_query(
                child_target_configurations
            )
        )
    return out
