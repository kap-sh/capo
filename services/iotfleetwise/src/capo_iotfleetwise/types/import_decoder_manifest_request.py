"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ImportDecoderManifestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.network_file_definitions
    import capo_iotfleetwise.types.resource_name


class ImportDecoderManifestRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the decoder manifest to import. </p>"""
    network_file_definitions: (
        "capo_iotfleetwise.types.network_file_definitions.NetworkFileDefinitions"
    )
    """<p> The file to load into an Amazon Web Services account. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportDecoderManifestRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_iotfleetwise.types.network_file_definitions

    out["networkFileDefinitions"] = (
        capo_iotfleetwise.types.network_file_definitions.serialize_aws_json_1_0(
            value["network_file_definitions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportDecoderManifestRequest:
    out: ImportDecoderManifestRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("networkFileDefinitions") is not None:
        import capo_iotfleetwise.types.network_file_definitions

        out["network_file_definitions"] = (
            capo_iotfleetwise.types.network_file_definitions.deserialize_aws_json_1_0(
                data["networkFileDefinitions"]
            )
        )
    else:
        out["network_file_definitions"] = []
    return out
