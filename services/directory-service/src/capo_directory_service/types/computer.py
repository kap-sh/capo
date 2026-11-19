"""Generated from Smithy shape ``com.amazonaws.directoryservice#Computer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.attributes
    import capo_directory_service.types.computer_name
    import capo_directory_service.types.sid


class Computer(TypedDict, closed=True):
    computer_id: NotRequired["capo_directory_service.types.sid.SID"]
    """<p>The identifier of the computer.</p>"""
    computer_name: NotRequired[
        "capo_directory_service.types.computer_name.ComputerName"
    ]
    """<p>The computer name.</p>"""
    computer_attributes: NotRequired[
        "capo_directory_service.types.attributes.Attributes"
    ]
    """<p>An array of <a>Attribute</a> objects containing the LDAP attributes that belong to the computer account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Computer) -> dict:
    out: dict = {}
    if "computer_id" in value:
        out["ComputerId"] = value["computer_id"]
    if "computer_name" in value:
        out["ComputerName"] = value["computer_name"]
    if "computer_attributes" in value:
        import capo_directory_service.types.attributes

        out["ComputerAttributes"] = (
            capo_directory_service.types.attributes.serialize_aws_json_1_1(
                value["computer_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Computer:
    out: Computer = {}  # type: ignore[typeddict-item]
    if data.get("ComputerId") is not None:
        out["computer_id"] = data["ComputerId"]
    if data.get("ComputerName") is not None:
        out["computer_name"] = data["ComputerName"]
    if data.get("ComputerAttributes") is not None:
        import capo_directory_service.types.attributes

        out["computer_attributes"] = (
            capo_directory_service.types.attributes.deserialize_aws_json_1_1(
                data["ComputerAttributes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Computer) -> dict:
    out: dict = {}
    if "computer_id" in value:
        out["ComputerId"] = value["computer_id"]
    if "computer_name" in value:
        out["ComputerName"] = value["computer_name"]
    if "computer_attributes" in value:
        import capo_directory_service.types.attributes

        out["ComputerAttributes"] = (
            capo_directory_service.types.attributes.serialize_cbor(
                value["computer_attributes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Computer:
    out: Computer = {}  # type: ignore[typeddict-item]
    if data.get("ComputerId") is not None:
        out["computer_id"] = data["ComputerId"]
    if data.get("ComputerName") is not None:
        out["computer_name"] = data["ComputerName"]
    if data.get("ComputerAttributes") is not None:
        import capo_directory_service.types.attributes

        out["computer_attributes"] = (
            capo_directory_service.types.attributes.deserialize_cbor(
                data["ComputerAttributes"]
            )
        )
    return out
