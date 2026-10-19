"""Generated from Smithy shape ``com.amazonaws.evs#DeleteEntitlementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.client_token
    import capo_evs.types.connector_id
    import capo_evs.types.entitlement_type
    import capo_evs.types.environment_id
    import capo_evs.types.vm_id_list


class DeleteEntitlementRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "capo_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment that the entitlement belongs to.</p>"""
    connector_id: "capo_evs.types.connector_id.ConnectorId"
    """<p>A unique ID for the connector associated with the entitlement.</p>"""
    entitlement_type: "capo_evs.types.entitlement_type.EntitlementType"
    """<p>The type of entitlement to delete.</p>"""
    vm_ids: "capo_evs.types.vm_id_list.VmIdList"
    """<p>The list of VMware vSphere virtual machine managed object IDs to delete entitlements for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEntitlementRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["environmentId"] = value["environment_id"]
    out["connectorId"] = value["connector_id"]
    import capo_evs.types.entitlement_type

    out["entitlementType"] = capo_evs.types.entitlement_type.serialize_aws_json_1_0(
        value["entitlement_type"]
    )
    import capo_evs.types.vm_id_list

    out["vmIds"] = capo_evs.types.vm_id_list.serialize_aws_json_1_0(value["vm_ids"])
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEntitlementRequest:
    out: DeleteEntitlementRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("connectorId") is not None:
        out["connector_id"] = data["connectorId"]
    else:
        out["connector_id"] = ""
    if data.get("entitlementType") is not None:
        import capo_evs.types.entitlement_type

        out["entitlement_type"] = (
            capo_evs.types.entitlement_type.deserialize_aws_json_1_0(
                data["entitlementType"]
            )
        )
    else:
        import typing

        out["entitlement_type"] = typing.cast(
            "capo_evs.types.entitlement_type.EntitlementType", ""
        )
    if data.get("vmIds") is not None:
        import capo_evs.types.vm_id_list

        out["vm_ids"] = capo_evs.types.vm_id_list.deserialize_aws_json_1_0(
            data["vmIds"]
        )
    else:
        out["vm_ids"] = []
    return out
