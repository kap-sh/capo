"""Generated from Smithy shape ``com.amazonaws.directconnect#AvailableBillingMode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.available_port_speeds
    import capo_direct_connect.types.billing_mode
    import capo_direct_connect.types.included_region_list


class AvailableBillingMode(TypedDict, closed=True):
    billing_mode: NotRequired["capo_direct_connect.types.billing_mode.BillingMode"]
    """<p>The billing mode.</p>"""
    available_port_speeds: NotRequired[
        "capo_direct_connect.types.available_port_speeds.AvailablePortSpeeds"
    ]
    """<p>The port speeds available for the billing mode.</p>"""
    included_regions: NotRequired[
        "capo_direct_connect.types.included_region_list.IncludedRegionList"
    ]
    """<p>The Amazon Web Services Regions included with the billing mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailableBillingMode) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        import capo_direct_connect.types.billing_mode

        out["billingMode"] = (
            capo_direct_connect.types.billing_mode.serialize_aws_json_1_1(
                value["billing_mode"]
            )
        )
    if "available_port_speeds" in value:
        import capo_direct_connect.types.available_port_speeds

        out["availablePortSpeeds"] = (
            capo_direct_connect.types.available_port_speeds.serialize_aws_json_1_1(
                value["available_port_speeds"]
            )
        )
    if "included_regions" in value:
        import capo_direct_connect.types.included_region_list

        out["includedRegions"] = (
            capo_direct_connect.types.included_region_list.serialize_aws_json_1_1(
                value["included_regions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AvailableBillingMode:
    out: AvailableBillingMode = {}  # type: ignore[typeddict-item]
    if data.get("billingMode") is not None:
        import capo_direct_connect.types.billing_mode

        out["billing_mode"] = (
            capo_direct_connect.types.billing_mode.deserialize_aws_json_1_1(
                data["billingMode"]
            )
        )
    if data.get("availablePortSpeeds") is not None:
        import capo_direct_connect.types.available_port_speeds

        out["available_port_speeds"] = (
            capo_direct_connect.types.available_port_speeds.deserialize_aws_json_1_1(
                data["availablePortSpeeds"]
            )
        )
    if data.get("includedRegions") is not None:
        import capo_direct_connect.types.included_region_list

        out["included_regions"] = (
            capo_direct_connect.types.included_region_list.deserialize_aws_json_1_1(
                data["includedRegions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AvailableBillingMode) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        import capo_direct_connect.types.billing_mode

        out["billingMode"] = capo_direct_connect.types.billing_mode.serialize_cbor(
            value["billing_mode"]
        )
    if "available_port_speeds" in value:
        import capo_direct_connect.types.available_port_speeds

        out["availablePortSpeeds"] = (
            capo_direct_connect.types.available_port_speeds.serialize_cbor(
                value["available_port_speeds"]
            )
        )
    if "included_regions" in value:
        import capo_direct_connect.types.included_region_list

        out["includedRegions"] = (
            capo_direct_connect.types.included_region_list.serialize_cbor(
                value["included_regions"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AvailableBillingMode:
    out: AvailableBillingMode = {}  # type: ignore[typeddict-item]
    if data.get("billingMode") is not None:
        import capo_direct_connect.types.billing_mode

        out["billing_mode"] = capo_direct_connect.types.billing_mode.deserialize_cbor(
            data["billingMode"]
        )
    if data.get("availablePortSpeeds") is not None:
        import capo_direct_connect.types.available_port_speeds

        out["available_port_speeds"] = (
            capo_direct_connect.types.available_port_speeds.deserialize_cbor(
                data["availablePortSpeeds"]
            )
        )
    if data.get("includedRegions") is not None:
        import capo_direct_connect.types.included_region_list

        out["included_regions"] = (
            capo_direct_connect.types.included_region_list.deserialize_cbor(
                data["includedRegions"]
            )
        )
    return out
