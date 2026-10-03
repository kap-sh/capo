"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListManagedThingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.connector_device_id
    import capo_iot_managed_integrations.types.connector_policy_id
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.owner
    import capo_iot_managed_integrations.types.parent_controller_id
    import capo_iot_managed_integrations.types.provisioning_status
    import capo_iot_managed_integrations.types.role
    import capo_iot_managed_integrations.types.serial_number


class ListManagedThingsRequest(TypedDict, closed=True):
    owner_filter: NotRequired["capo_iot_managed_integrations.types.owner.Owner"]
    """<p>Filter on device owners when listing managed things.</p>"""
    credential_locker_filter: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>Filter on a credential locker for a managed thing.</p>"""
    role_filter: NotRequired["capo_iot_managed_integrations.types.role.Role"]
    """<p>Filter on the type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.</p>"""
    parent_controller_identifier_filter: NotRequired[
        "capo_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
    ]
    """<p>Filter on a parent controller id for a managed thing.</p>"""
    connector_policy_id_filter: NotRequired[
        "capo_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
    ]
    """<p>Filter on a connector policy id for a managed thing.</p>"""
    connector_destination_id_filter: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>Filter managed things by the connector destination ID they are associated with.</p>"""
    connector_device_id_filter: NotRequired[
        "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
    ]
    """<p>Filter managed things by the connector device ID they are associated with. When specified, only managed things with this connector device ID will be returned.</p>"""
    serial_number_filter: NotRequired[
        "capo_iot_managed_integrations.types.serial_number.SerialNumber"
    ]
    """<p>Filter on the serial number of the device.</p>"""
    provisioning_status_filter: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
    ]
    """<p>Filter on the status of the device. For more information, see <a href="https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html">Device Provisioning</a>.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "capo_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedThingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedThingsRequest:
    out: ListManagedThingsRequest = {}  # type: ignore[typeddict-item]
    return out
