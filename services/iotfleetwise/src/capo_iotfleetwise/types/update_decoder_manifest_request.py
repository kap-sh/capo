"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateDecoderManifestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.default_for_unmapped_signals_type
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.fqns
    import capo_iotfleetwise.types.interface_ids
    import capo_iotfleetwise.types.manifest_status
    import capo_iotfleetwise.types.network_interfaces
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.signal_decoders


class UpdateDecoderManifestRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the decoder manifest to update.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the decoder manifest to update. </p>"""
    signal_decoders_to_add: NotRequired[
        "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
    ]
    """<p> A list of information about decoding additional signals to add to the decoder manifest. </p>"""
    signal_decoders_to_update: NotRequired[
        "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
    ]
    """<p> A list of updated information about decoding signals to update in the decoder manifest. </p>"""
    signal_decoders_to_remove: NotRequired["capo_iotfleetwise.types.fqns.Fqns"]
    """<p> A list of signal decoders to remove from the decoder manifest. </p>"""
    network_interfaces_to_add: NotRequired[
        "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
    ]
    """<p> A list of information about the network interfaces to add to the decoder manifest. </p>"""
    network_interfaces_to_update: NotRequired[
        "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
    ]
    """<p> A list of information about the network interfaces to update in the decoder manifest. </p>"""
    network_interfaces_to_remove: NotRequired[
        "capo_iotfleetwise.types.interface_ids.InterfaceIds"
    ]
    """<p> A list of network interfaces to remove from the decoder manifest.</p>"""
    status: NotRequired["capo_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p> The state of the decoder manifest. If the status is <code>ACTIVE</code>, the decoder manifest can't be edited. If the status is <code>DRAFT</code>, you can edit the decoder manifest. </p>"""
    default_for_unmapped_signals: NotRequired[
        "capo_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
    ]
    """<p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDecoderManifestRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "signal_decoders_to_add" in value:
        import capo_iotfleetwise.types.signal_decoders

        out["signalDecodersToAdd"] = (
            capo_iotfleetwise.types.signal_decoders.serialize_aws_json_1_0(
                value["signal_decoders_to_add"]
            )
        )
    if "signal_decoders_to_update" in value:
        import capo_iotfleetwise.types.signal_decoders

        out["signalDecodersToUpdate"] = (
            capo_iotfleetwise.types.signal_decoders.serialize_aws_json_1_0(
                value["signal_decoders_to_update"]
            )
        )
    if "signal_decoders_to_remove" in value:
        import capo_iotfleetwise.types.fqns

        out["signalDecodersToRemove"] = (
            capo_iotfleetwise.types.fqns.serialize_aws_json_1_0(
                value["signal_decoders_to_remove"]
            )
        )
    if "network_interfaces_to_add" in value:
        import capo_iotfleetwise.types.network_interfaces

        out["networkInterfacesToAdd"] = (
            capo_iotfleetwise.types.network_interfaces.serialize_aws_json_1_0(
                value["network_interfaces_to_add"]
            )
        )
    if "network_interfaces_to_update" in value:
        import capo_iotfleetwise.types.network_interfaces

        out["networkInterfacesToUpdate"] = (
            capo_iotfleetwise.types.network_interfaces.serialize_aws_json_1_0(
                value["network_interfaces_to_update"]
            )
        )
    if "network_interfaces_to_remove" in value:
        import capo_iotfleetwise.types.interface_ids

        out["networkInterfacesToRemove"] = (
            capo_iotfleetwise.types.interface_ids.serialize_aws_json_1_0(
                value["network_interfaces_to_remove"]
            )
        )
    if "status" in value:
        import capo_iotfleetwise.types.manifest_status

        out["status"] = capo_iotfleetwise.types.manifest_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "default_for_unmapped_signals" in value:
        import capo_iotfleetwise.types.default_for_unmapped_signals_type

        out["defaultForUnmappedSignals"] = (
            capo_iotfleetwise.types.default_for_unmapped_signals_type.serialize_aws_json_1_0(
                value["default_for_unmapped_signals"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDecoderManifestRequest:
    out: UpdateDecoderManifestRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateDecoderManifestRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("signalDecodersToAdd") is not None:
        import capo_iotfleetwise.types.signal_decoders

        out["signal_decoders_to_add"] = (
            capo_iotfleetwise.types.signal_decoders.deserialize_aws_json_1_0(
                data["signalDecodersToAdd"]
            )
        )
    if data.get("signalDecodersToUpdate") is not None:
        import capo_iotfleetwise.types.signal_decoders

        out["signal_decoders_to_update"] = (
            capo_iotfleetwise.types.signal_decoders.deserialize_aws_json_1_0(
                data["signalDecodersToUpdate"]
            )
        )
    if data.get("signalDecodersToRemove") is not None:
        import capo_iotfleetwise.types.fqns

        out["signal_decoders_to_remove"] = (
            capo_iotfleetwise.types.fqns.deserialize_aws_json_1_0(
                data["signalDecodersToRemove"]
            )
        )
    if data.get("networkInterfacesToAdd") is not None:
        import capo_iotfleetwise.types.network_interfaces

        out["network_interfaces_to_add"] = (
            capo_iotfleetwise.types.network_interfaces.deserialize_aws_json_1_0(
                data["networkInterfacesToAdd"]
            )
        )
    if data.get("networkInterfacesToUpdate") is not None:
        import capo_iotfleetwise.types.network_interfaces

        out["network_interfaces_to_update"] = (
            capo_iotfleetwise.types.network_interfaces.deserialize_aws_json_1_0(
                data["networkInterfacesToUpdate"]
            )
        )
    if data.get("networkInterfacesToRemove") is not None:
        import capo_iotfleetwise.types.interface_ids

        out["network_interfaces_to_remove"] = (
            capo_iotfleetwise.types.interface_ids.deserialize_aws_json_1_0(
                data["networkInterfacesToRemove"]
            )
        )
    if data.get("status") is not None:
        import capo_iotfleetwise.types.manifest_status

        out["status"] = (
            capo_iotfleetwise.types.manifest_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("defaultForUnmappedSignals") is not None:
        import capo_iotfleetwise.types.default_for_unmapped_signals_type

        out["default_for_unmapped_signals"] = (
            capo_iotfleetwise.types.default_for_unmapped_signals_type.deserialize_aws_json_1_0(
                data["defaultForUnmappedSignals"]
            )
        )
    return out
