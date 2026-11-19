"""Generated from Smithy shape ``com.amazonaws.directconnect#Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.available_billing_mode_list
    import capo_direct_connect.types.available_mac_sec_port_speeds
    import capo_direct_connect.types.available_port_speeds
    import capo_direct_connect.types.location_code
    import capo_direct_connect.types.location_name
    import capo_direct_connect.types.provider_list
    import capo_direct_connect.types.region


class Location(TypedDict, closed=True):
    location_code: NotRequired["capo_direct_connect.types.location_code.LocationCode"]
    """<p>The code for the location.</p>"""
    location_name: NotRequired["capo_direct_connect.types.location_name.LocationName"]
    """<p>The name of the location. This includes the name of the colocation partner and the physical site of the building.</p>"""
    region: NotRequired["capo_direct_connect.types.region.Region"]
    """<p>The Amazon Web Services Region for the location.</p>"""
    available_port_speeds: NotRequired[
        "capo_direct_connect.types.available_port_speeds.AvailablePortSpeeds"
    ]
    """<p>The available port speeds for the location.</p>"""
    available_providers: NotRequired[
        "capo_direct_connect.types.provider_list.ProviderList"
    ]
    """<p>The name of the service provider for the location.</p>"""
    available_mac_sec_port_speeds: NotRequired[
        "capo_direct_connect.types.available_mac_sec_port_speeds.AvailableMacSecPortSpeeds"
    ]
    """<p>The available MAC Security (MACsec) port speeds for the location.</p>"""
    available_billing_modes: NotRequired[
        "capo_direct_connect.types.available_billing_mode_list.AvailableBillingModeList"
    ]
    """<p>The billing modes available at the location, including the port speeds and Amazon Web Services Regions supported by each mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Location) -> dict:
    out: dict = {}
    if "location_code" in value:
        out["locationCode"] = value["location_code"]
    if "location_name" in value:
        out["locationName"] = value["location_name"]
    if "region" in value:
        out["region"] = value["region"]
    if "available_port_speeds" in value:
        import capo_direct_connect.types.available_port_speeds

        out["availablePortSpeeds"] = (
            capo_direct_connect.types.available_port_speeds.serialize_aws_json_1_1(
                value["available_port_speeds"]
            )
        )
    if "available_providers" in value:
        import capo_direct_connect.types.provider_list

        out["availableProviders"] = (
            capo_direct_connect.types.provider_list.serialize_aws_json_1_1(
                value["available_providers"]
            )
        )
    if "available_mac_sec_port_speeds" in value:
        import capo_direct_connect.types.available_mac_sec_port_speeds

        out["availableMacSecPortSpeeds"] = (
            capo_direct_connect.types.available_mac_sec_port_speeds.serialize_aws_json_1_1(
                value["available_mac_sec_port_speeds"]
            )
        )
    if "available_billing_modes" in value:
        import capo_direct_connect.types.available_billing_mode_list

        out["availableBillingModes"] = (
            capo_direct_connect.types.available_billing_mode_list.serialize_aws_json_1_1(
                value["available_billing_modes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if data.get("locationCode") is not None:
        out["location_code"] = data["locationCode"]
    if data.get("locationName") is not None:
        out["location_name"] = data["locationName"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("availablePortSpeeds") is not None:
        import capo_direct_connect.types.available_port_speeds

        out["available_port_speeds"] = (
            capo_direct_connect.types.available_port_speeds.deserialize_aws_json_1_1(
                data["availablePortSpeeds"]
            )
        )
    if data.get("availableProviders") is not None:
        import capo_direct_connect.types.provider_list

        out["available_providers"] = (
            capo_direct_connect.types.provider_list.deserialize_aws_json_1_1(
                data["availableProviders"]
            )
        )
    if data.get("availableMacSecPortSpeeds") is not None:
        import capo_direct_connect.types.available_mac_sec_port_speeds

        out["available_mac_sec_port_speeds"] = (
            capo_direct_connect.types.available_mac_sec_port_speeds.deserialize_aws_json_1_1(
                data["availableMacSecPortSpeeds"]
            )
        )
    if data.get("availableBillingModes") is not None:
        import capo_direct_connect.types.available_billing_mode_list

        out["available_billing_modes"] = (
            capo_direct_connect.types.available_billing_mode_list.deserialize_aws_json_1_1(
                data["availableBillingModes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Location) -> dict:
    out: dict = {}
    if "location_code" in value:
        out["locationCode"] = value["location_code"]
    if "location_name" in value:
        out["locationName"] = value["location_name"]
    if "region" in value:
        out["region"] = value["region"]
    if "available_port_speeds" in value:
        import capo_direct_connect.types.available_port_speeds

        out["availablePortSpeeds"] = (
            capo_direct_connect.types.available_port_speeds.serialize_cbor(
                value["available_port_speeds"]
            )
        )
    if "available_providers" in value:
        import capo_direct_connect.types.provider_list

        out["availableProviders"] = (
            capo_direct_connect.types.provider_list.serialize_cbor(
                value["available_providers"]
            )
        )
    if "available_mac_sec_port_speeds" in value:
        import capo_direct_connect.types.available_mac_sec_port_speeds

        out["availableMacSecPortSpeeds"] = (
            capo_direct_connect.types.available_mac_sec_port_speeds.serialize_cbor(
                value["available_mac_sec_port_speeds"]
            )
        )
    if "available_billing_modes" in value:
        import capo_direct_connect.types.available_billing_mode_list

        out["availableBillingModes"] = (
            capo_direct_connect.types.available_billing_mode_list.serialize_cbor(
                value["available_billing_modes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if data.get("locationCode") is not None:
        out["location_code"] = data["locationCode"]
    if data.get("locationName") is not None:
        out["location_name"] = data["locationName"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("availablePortSpeeds") is not None:
        import capo_direct_connect.types.available_port_speeds

        out["available_port_speeds"] = (
            capo_direct_connect.types.available_port_speeds.deserialize_cbor(
                data["availablePortSpeeds"]
            )
        )
    if data.get("availableProviders") is not None:
        import capo_direct_connect.types.provider_list

        out["available_providers"] = (
            capo_direct_connect.types.provider_list.deserialize_cbor(
                data["availableProviders"]
            )
        )
    if data.get("availableMacSecPortSpeeds") is not None:
        import capo_direct_connect.types.available_mac_sec_port_speeds

        out["available_mac_sec_port_speeds"] = (
            capo_direct_connect.types.available_mac_sec_port_speeds.deserialize_cbor(
                data["availableMacSecPortSpeeds"]
            )
        )
    if data.get("availableBillingModes") is not None:
        import capo_direct_connect.types.available_billing_mode_list

        out["available_billing_modes"] = (
            capo_direct_connect.types.available_billing_mode_list.deserialize_cbor(
                data["availableBillingModes"]
            )
        )
    return out
