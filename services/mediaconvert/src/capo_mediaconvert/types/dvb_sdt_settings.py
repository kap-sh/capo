"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSdtSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min25_max2000
    import capo_mediaconvert.types.__string_min1_max256
    import capo_mediaconvert.types.output_sdt


class DvbSdtSettings(TypedDict, closed=True):
    output_sdt: NotRequired["capo_mediaconvert.types.output_sdt.OutputSdt"]
    """Selects method of inserting SDT information into output stream. "Follow input SDT" copies SDT information from input stream to output stream. "Follow input SDT if present" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter "SDT Manually" means user will enter the SDT information. "No SDT" means output stream will not contain SDT information."""
    sdt_interval: NotRequired[
        "capo_mediaconvert.types.__integer_min25_max2000.__integerMin25Max2000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream."""
    service_name: NotRequired[
        "capo_mediaconvert.types.__string_min1_max256.__stringMin1Max256"
    ]
    """The service name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters."""
    service_provider_name: NotRequired[
        "capo_mediaconvert.types.__string_min1_max256.__stringMin1Max256"
    ]
    """The service provider name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters."""


# --- restJson1 ser/de ---
def serialize_json(value: DvbSdtSettings) -> dict:
    out: dict = {}
    if "output_sdt" in value:
        import capo_mediaconvert.types.output_sdt

        out["outputSdt"] = capo_mediaconvert.types.output_sdt.serialize_json(
            value["output_sdt"]
        )
    if "sdt_interval" in value:
        out["sdtInterval"] = value["sdt_interval"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_provider_name" in value:
        out["serviceProviderName"] = value["service_provider_name"]
    return out


def deserialize_json(data: dict) -> DvbSdtSettings:
    out: DvbSdtSettings = {}  # type: ignore[typeddict-item]
    if data.get("outputSdt") is not None:
        import capo_mediaconvert.types.output_sdt

        out["output_sdt"] = capo_mediaconvert.types.output_sdt.deserialize_json(
            data["outputSdt"]
        )
    if data.get("sdtInterval") is not None:
        out["sdt_interval"] = data["sdtInterval"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceProviderName") is not None:
        out["service_provider_name"] = data["serviceProviderName"]
    return out
