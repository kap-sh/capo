"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateDecoderManifestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.default_for_unmapped_signals_type
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.network_interfaces
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.signal_decoders
    import capo_iotfleetwise.types.tag_list


class CreateDecoderManifestRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The unique name of the decoder manifest to create.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the decoder manifest. </p>"""
    model_manifest_arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the vehicle model (model manifest). </p>"""
    signal_decoders: NotRequired[
        "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
    ]
    """<p> A list of information about signal decoders. </p>"""
    network_interfaces: NotRequired[
        "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
    ]
    """<p> A list of information about available network interfaces. </p>"""
    default_for_unmapped_signals: NotRequired[
        "capo_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
    ]
    """<p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>"""
    tags: NotRequired["capo_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the decoder manifest.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDecoderManifestRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["modelManifestArn"] = value["model_manifest_arn"]
    if "signal_decoders" in value:
        import capo_iotfleetwise.types.signal_decoders

        out["signalDecoders"] = (
            capo_iotfleetwise.types.signal_decoders.serialize_aws_json_1_0(
                value["signal_decoders"]
            )
        )
    if "network_interfaces" in value:
        import capo_iotfleetwise.types.network_interfaces

        out["networkInterfaces"] = (
            capo_iotfleetwise.types.network_interfaces.serialize_aws_json_1_0(
                value["network_interfaces"]
            )
        )
    if "default_for_unmapped_signals" in value:
        import capo_iotfleetwise.types.default_for_unmapped_signals_type

        out["defaultForUnmappedSignals"] = (
            capo_iotfleetwise.types.default_for_unmapped_signals_type.serialize_aws_json_1_0(
                value["default_for_unmapped_signals"]
            )
        )
    if "tags" in value:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDecoderManifestRequest:
    out: CreateDecoderManifestRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDecoderManifestRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("modelManifestArn") is not None:
        out["model_manifest_arn"] = data["modelManifestArn"]
    else:
        raise DeserializationError(
            "CreateDecoderManifestRequest.model_manifest_arn required"
        )
    if data.get("signalDecoders") is not None:
        import capo_iotfleetwise.types.signal_decoders

        out["signal_decoders"] = (
            capo_iotfleetwise.types.signal_decoders.deserialize_aws_json_1_0(
                data["signalDecoders"]
            )
        )
    if data.get("networkInterfaces") is not None:
        import capo_iotfleetwise.types.network_interfaces

        out["network_interfaces"] = (
            capo_iotfleetwise.types.network_interfaces.deserialize_aws_json_1_0(
                data["networkInterfaces"]
            )
        )
    if data.get("defaultForUnmappedSignals") is not None:
        import capo_iotfleetwise.types.default_for_unmapped_signals_type

        out["default_for_unmapped_signals"] = (
            capo_iotfleetwise.types.default_for_unmapped_signals_type.deserialize_aws_json_1_0(
                data["defaultForUnmappedSignals"]
            )
        )
    if data.get("tags") is not None:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
