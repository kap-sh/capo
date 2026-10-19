"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ImageGenerationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.configuration_status
    import capo_kinesis_video.types.format
    import capo_kinesis_video.types.format_config
    import capo_kinesis_video.types.height_pixels
    import capo_kinesis_video.types.image_generation_destination_config
    import capo_kinesis_video.types.image_selector_type
    import capo_kinesis_video.types.sampling_interval
    import capo_kinesis_video.types.width_pixels


class ImageGenerationConfiguration(TypedDict, closed=True):
    status: "capo_kinesis_video.types.configuration_status.ConfigurationStatus"
    """<p>Indicates whether the <code>ContinuousImageGenerationConfigurations</code> API is enabled or disabled.</p>"""
    image_selector_type: (
        "capo_kinesis_video.types.image_selector_type.ImageSelectorType"
    )
    """<p>The origin of the Server or Producer timestamps to use to generate the images.</p>"""
    destination_config: "capo_kinesis_video.types.image_generation_destination_config.ImageGenerationDestinationConfig"
    """<p>The structure that contains the information required to deliver images to a customer.</p>"""
    sampling_interval: "capo_kinesis_video.types.sampling_interval.SamplingInterval"
    """<p>The time interval in milliseconds (ms) at which the images need to be generated from the stream. The minimum value that can be provided is 200 ms. If the timestamp range is less than the sampling interval, the Image from the <code>StartTimestamp</code> will be returned if available. </p>"""
    format: "capo_kinesis_video.types.format.Format"
    """<p>The accepted image format.</p>"""
    format_config: NotRequired["capo_kinesis_video.types.format_config.FormatConfig"]
    """<p>The list of a key-value pair structure that contains extra parameters that can be applied when the image is generated. The <code>FormatConfig</code> key is the <code>JPEGQuality</code>, which indicates the JPEG quality key to be used to generate the image. The <code>FormatConfig</code> value accepts ints from 1 to 100. If the value is 1, the image will be generated with less quality and the best compression. If the value is 100, the image will be generated with the best quality and less compression. If no value is provided, the default value of the <code>JPEGQuality</code> key will be set to 80.</p>"""
    width_pixels: NotRequired["capo_kinesis_video.types.width_pixels.WidthPixels"]
    """<p>The width of the output image that is used in conjunction with the <code>HeightPixels</code> parameter. When both <code>WidthPixels</code> and <code>HeightPixels</code> parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the <code>WidthPixels</code> parameter is provided, its original aspect ratio will be used to calculate the <code>HeightPixels</code> ratio. If neither parameter is provided, the original image size will be returned.</p>"""
    height_pixels: NotRequired["capo_kinesis_video.types.height_pixels.HeightPixels"]
    """<p>The height of the output image that is used in conjunction with the <code>WidthPixels</code> parameter. When both <code>HeightPixels</code> and <code>WidthPixels</code> parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the <code>HeightPixels</code> parameter is provided, its original aspect ratio will be used to calculate the <code>WidthPixels</code> ratio. If neither parameter is provided, the original image size will be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageGenerationConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_video.types.configuration_status

    out["Status"] = capo_kinesis_video.types.configuration_status.serialize_json(
        value["status"]
    )
    import capo_kinesis_video.types.image_selector_type

    out["ImageSelectorType"] = (
        capo_kinesis_video.types.image_selector_type.serialize_json(
            value["image_selector_type"]
        )
    )
    import capo_kinesis_video.types.image_generation_destination_config

    out["DestinationConfig"] = (
        capo_kinesis_video.types.image_generation_destination_config.serialize_json(
            value["destination_config"]
        )
    )
    out["SamplingInterval"] = value["sampling_interval"]
    import capo_kinesis_video.types.format

    out["Format"] = capo_kinesis_video.types.format.serialize_json(value["format"])
    if "format_config" in value:
        import capo_kinesis_video.types.format_config

        out["FormatConfig"] = capo_kinesis_video.types.format_config.serialize_json(
            value["format_config"]
        )
    if "width_pixels" in value:
        out["WidthPixels"] = value["width_pixels"]
    if "height_pixels" in value:
        out["HeightPixels"] = value["height_pixels"]
    return out


def deserialize_json(data: dict) -> ImageGenerationConfiguration:
    out: ImageGenerationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_kinesis_video.types.configuration_status

        out["status"] = capo_kinesis_video.types.configuration_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_kinesis_video.types.configuration_status.ConfigurationStatus", ""
        )
    if data.get("ImageSelectorType") is not None:
        import capo_kinesis_video.types.image_selector_type

        out["image_selector_type"] = (
            capo_kinesis_video.types.image_selector_type.deserialize_json(
                data["ImageSelectorType"]
            )
        )
    else:
        import typing

        out["image_selector_type"] = typing.cast(
            "capo_kinesis_video.types.image_selector_type.ImageSelectorType", ""
        )
    if data.get("DestinationConfig") is not None:
        import capo_kinesis_video.types.image_generation_destination_config

        out["destination_config"] = (
            capo_kinesis_video.types.image_generation_destination_config.deserialize_json(
                data["DestinationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ImageGenerationConfiguration.destination_config required"
        )
    if data.get("SamplingInterval") is not None:
        out["sampling_interval"] = data["SamplingInterval"]
    else:
        out["sampling_interval"] = 0
    if data.get("Format") is not None:
        import capo_kinesis_video.types.format

        out["format"] = capo_kinesis_video.types.format.deserialize_json(data["Format"])
    else:
        import typing

        out["format"] = typing.cast("capo_kinesis_video.types.format.Format", "")
    if data.get("FormatConfig") is not None:
        import capo_kinesis_video.types.format_config

        out["format_config"] = capo_kinesis_video.types.format_config.deserialize_json(
            data["FormatConfig"]
        )
    if data.get("WidthPixels") is not None:
        out["width_pixels"] = data["WidthPixels"]
    if data.get("HeightPixels") is not None:
        out["height_pixels"] = data["HeightPixels"]
    return out
