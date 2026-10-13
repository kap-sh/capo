"""Generated from Smithy shape ``com.amazonaws.networkmanager#Device``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.aws_location
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.device_arn
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.device_state
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.location
    import capo_networkmanager.types.site_id
    import capo_networkmanager.types.tag_list


class Device(TypedDict, closed=True):
    device_id: NotRequired["capo_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the device.</p>"""
    device_arn: NotRequired["capo_networkmanager.types.device_arn.DeviceArn"]
    """<p>The Amazon Resource Name (ARN) of the device.</p>"""
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    aws_location: NotRequired["capo_networkmanager.types.aws_location.AWSLocation"]
    """<p>The Amazon Web Services location of the device.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the device.</p>"""
    type: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The device type.</p>"""
    vendor: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The device vendor.</p>"""
    model: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The device model.</p>"""
    serial_number: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The device serial number.</p>"""
    location: NotRequired["capo_networkmanager.types.location.Location"]
    """<p>The site location.</p>"""
    site_id: NotRequired["capo_networkmanager.types.site_id.SiteId"]
    """<p>The site ID.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the site was created.</p>"""
    state: NotRequired["capo_networkmanager.types.device_state.DeviceState"]
    """<p>The device state.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags for the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Device) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "device_arn" in value:
        out["DeviceArn"] = value["device_arn"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "aws_location" in value:
        import capo_networkmanager.types.aws_location

        out["AWSLocation"] = capo_networkmanager.types.aws_location.serialize_json(
            value["aws_location"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    if "vendor" in value:
        out["Vendor"] = value["vendor"]
    if "model" in value:
        out["Model"] = value["model"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "location" in value:
        import capo_networkmanager.types.location

        out["Location"] = capo_networkmanager.types.location.serialize_json(
            value["location"]
        )
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.device_state

        out["State"] = capo_networkmanager.types.device_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    if data.get("DeviceArn") is not None:
        out["device_arn"] = data["DeviceArn"]
    if data.get("GlobalNetworkId") is not None:
        out["global_network_id"] = data["GlobalNetworkId"]
    if data.get("AWSLocation") is not None:
        import capo_networkmanager.types.aws_location

        out["aws_location"] = capo_networkmanager.types.aws_location.deserialize_json(
            data["AWSLocation"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Vendor") is not None:
        out["vendor"] = data["Vendor"]
    if data.get("Model") is not None:
        out["model"] = data["Model"]
    if data.get("SerialNumber") is not None:
        out["serial_number"] = data["SerialNumber"]
    if data.get("Location") is not None:
        import capo_networkmanager.types.location

        out["location"] = capo_networkmanager.types.location.deserialize_json(
            data["Location"]
        )
    if data.get("SiteId") is not None:
        out["site_id"] = data["SiteId"]
    if data.get("CreatedAt") is not None:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("State") is not None:
        import capo_networkmanager.types.device_state

        out["state"] = capo_networkmanager.types.device_state.deserialize_json(
            data["State"]
        )
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: Device) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "location" in value:
        out["location"] = "*** Sensitive Data Redacted ***"
    return out
