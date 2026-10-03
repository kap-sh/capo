"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean
    import capo_guardduty.types.client_token
    import capo_guardduty.types.data_source_configurations
    import capo_guardduty.types.detector_feature_configurations
    import capo_guardduty.types.finding_publishing_frequency
    import capo_guardduty.types.tag_map


class CreateDetectorRequest(TypedDict, closed=True):
    enable: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the detector is to be enabled.</p>"""
    client_token: NotRequired["capo_guardduty.types.client_token.ClientToken"]
    """<p>The idempotency token for the create request.</p>"""
    finding_publishing_frequency: NotRequired[
        "capo_guardduty.types.finding_publishing_frequency.FindingPublishingFrequency"
    ]
    """<p>A value that specifies how frequently updated findings are exported.</p>"""
    data_sources: NotRequired[
        "capo_guardduty.types.data_source_configurations.DataSourceConfigurations"
    ]
    """<p>Describes which data sources will be enabled for the detector.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>"""
    tags: NotRequired["capo_guardduty.types.tag_map.TagMap"]
    """<p>The tags to be added to a new detector resource.</p>"""
    features: NotRequired[
        "capo_guardduty.types.detector_feature_configurations.DetectorFeatureConfigurations"
    ]
    """<p>A list of features that will be configured for the detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDetectorRequest) -> dict:
    out: dict = {}
    if "enable" in value:
        out["enable"] = value["enable"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "finding_publishing_frequency" in value:
        import capo_guardduty.types.finding_publishing_frequency

        out["findingPublishingFrequency"] = (
            capo_guardduty.types.finding_publishing_frequency.serialize_json(
                value["finding_publishing_frequency"]
            )
        )
    if "data_sources" in value:
        import capo_guardduty.types.data_source_configurations

        out["dataSources"] = (
            capo_guardduty.types.data_source_configurations.serialize_json(
                value["data_sources"]
            )
        )
    if "tags" in value:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.serialize_json(value["tags"])
    if "features" in value:
        import capo_guardduty.types.detector_feature_configurations

        out["features"] = (
            capo_guardduty.types.detector_feature_configurations.serialize_json(
                value["features"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDetectorRequest:
    out: CreateDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("enable") is not None:
        out["enable"] = data["enable"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("findingPublishingFrequency") is not None:
        import capo_guardduty.types.finding_publishing_frequency

        out["finding_publishing_frequency"] = (
            capo_guardduty.types.finding_publishing_frequency.deserialize_json(
                data["findingPublishingFrequency"]
            )
        )
    if data.get("dataSources") is not None:
        import capo_guardduty.types.data_source_configurations

        out["data_sources"] = (
            capo_guardduty.types.data_source_configurations.deserialize_json(
                data["dataSources"]
            )
        )
    if data.get("tags") is not None:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.deserialize_json(data["tags"])
    if data.get("features") is not None:
        import capo_guardduty.types.detector_feature_configurations

        out["features"] = (
            capo_guardduty.types.detector_feature_configurations.deserialize_json(
                data["features"]
            )
        )
    return out
