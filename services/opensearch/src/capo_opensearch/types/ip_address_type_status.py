"""Generated from Smithy shape ``com.amazonaws.opensearch#IPAddressTypeStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.ip_address_type
    import capo_opensearch.types.option_status


class IPAddressTypeStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.ip_address_type.IPAddressType"
    """<p>The IP address options for the domain.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"


# --- restJson1 ser/de ---
def serialize_json(value: IPAddressTypeStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.ip_address_type

    out["Options"] = capo_opensearch.types.ip_address_type.serialize_json(
        value["options"]
    )
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> IPAddressTypeStatus:
    out: IPAddressTypeStatus = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        import capo_opensearch.types.ip_address_type

        out["options"] = capo_opensearch.types.ip_address_type.deserialize_json(
            data["Options"]
        )
    else:
        import typing

        out["options"] = typing.cast(
            "capo_opensearch.types.ip_address_type.IPAddressType", ""
        )
    if data.get("Status") is not None:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("IPAddressTypeStatus.status required")
    return out
