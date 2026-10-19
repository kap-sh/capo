"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.iot_site_wise_source_configuration
    import capo_iottwinmaker.types.iot_twin_maker_source_configuration
    import capo_iottwinmaker.types.s3_source_configuration
    import capo_iottwinmaker.types.source_type


class SourceConfiguration(TypedDict, closed=True):
    type: "capo_iottwinmaker.types.source_type.SourceType"
    """<p>The source configuration type.</p>"""
    s3_configuration: NotRequired[
        "capo_iottwinmaker.types.s3_source_configuration.S3SourceConfiguration"
    ]
    """<p>The source configuration S3 configuration.</p>"""
    iot_site_wise_configuration: NotRequired[
        "capo_iottwinmaker.types.iot_site_wise_source_configuration.IotSiteWiseSourceConfiguration"
    ]
    """<p>The source configuration IoT SiteWise configuration.</p>"""
    iot_twin_maker_configuration: NotRequired[
        "capo_iottwinmaker.types.iot_twin_maker_source_configuration.IotTwinMakerSourceConfiguration"
    ]
    """<p>The source configuration IoT TwinMaker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "s3_configuration" in value:
        import capo_iottwinmaker.types.s3_source_configuration

        out["s3Configuration"] = (
            capo_iottwinmaker.types.s3_source_configuration.serialize_json(
                value["s3_configuration"]
            )
        )
    if "iot_site_wise_configuration" in value:
        import capo_iottwinmaker.types.iot_site_wise_source_configuration

        out["iotSiteWiseConfiguration"] = (
            capo_iottwinmaker.types.iot_site_wise_source_configuration.serialize_json(
                value["iot_site_wise_configuration"]
            )
        )
    if "iot_twin_maker_configuration" in value:
        import capo_iottwinmaker.types.iot_twin_maker_source_configuration

        out["iotTwinMakerConfiguration"] = (
            capo_iottwinmaker.types.iot_twin_maker_source_configuration.serialize_json(
                value["iot_twin_maker_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceConfiguration:
    out: SourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("s3Configuration") is not None:
        import capo_iottwinmaker.types.s3_source_configuration

        out["s3_configuration"] = (
            capo_iottwinmaker.types.s3_source_configuration.deserialize_json(
                data["s3Configuration"]
            )
        )
    if data.get("iotSiteWiseConfiguration") is not None:
        import capo_iottwinmaker.types.iot_site_wise_source_configuration

        out["iot_site_wise_configuration"] = (
            capo_iottwinmaker.types.iot_site_wise_source_configuration.deserialize_json(
                data["iotSiteWiseConfiguration"]
            )
        )
    if data.get("iotTwinMakerConfiguration") is not None:
        import capo_iottwinmaker.types.iot_twin_maker_source_configuration

        out["iot_twin_maker_configuration"] = (
            capo_iottwinmaker.types.iot_twin_maker_source_configuration.deserialize_json(
                data["iotTwinMakerConfiguration"]
            )
        )
    return out
