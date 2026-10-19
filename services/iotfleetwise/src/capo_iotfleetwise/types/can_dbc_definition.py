"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CanDbcDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.interface_id
    import capo_iotfleetwise.types.model_signals_map
    import capo_iotfleetwise.types.network_files_list


class CanDbcDefinition(TypedDict, closed=True):
    network_interface: "capo_iotfleetwise.types.interface_id.InterfaceId"
    """<p>Contains information about a network interface.</p>"""
    can_dbc_files: "capo_iotfleetwise.types.network_files_list.NetworkFilesList"
    """<p>A list of DBC files. You can upload only one DBC file for each network interface and specify up to five (inclusive) files in the list. The DBC file can be a maximum size of 200 MB.</p>"""
    signals_map: NotRequired[
        "capo_iotfleetwise.types.model_signals_map.ModelSignalsMap"
    ]
    """<p>Pairs every signal specified in your vehicle model with a signal decoder.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CanDbcDefinition) -> dict:
    out: dict = {}
    out["networkInterface"] = value["network_interface"]
    import capo_iotfleetwise.types.network_files_list

    out["canDbcFiles"] = (
        capo_iotfleetwise.types.network_files_list.serialize_aws_json_1_0(
            value["can_dbc_files"]
        )
    )
    if "signals_map" in value:
        import capo_iotfleetwise.types.model_signals_map

        out["signalsMap"] = (
            capo_iotfleetwise.types.model_signals_map.serialize_aws_json_1_0(
                value["signals_map"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CanDbcDefinition:
    out: CanDbcDefinition = {}  # type: ignore[typeddict-item]
    if data.get("networkInterface") is not None:
        out["network_interface"] = data["networkInterface"]
    else:
        out["network_interface"] = ""
    if data.get("canDbcFiles") is not None:
        import capo_iotfleetwise.types.network_files_list

        out["can_dbc_files"] = (
            capo_iotfleetwise.types.network_files_list.deserialize_aws_json_1_0(
                data["canDbcFiles"]
            )
        )
    else:
        out["can_dbc_files"] = []
    if data.get("signalsMap") is not None:
        import capo_iotfleetwise.types.model_signals_map

        out["signals_map"] = (
            capo_iotfleetwise.types.model_signals_map.deserialize_aws_json_1_0(
                data["signalsMap"]
            )
        )
    return out
