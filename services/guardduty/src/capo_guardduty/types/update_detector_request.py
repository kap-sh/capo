"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean
    import capo_guardduty.types.data_source_configurations
    import capo_guardduty.types.detector_feature_configurations
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.finding_publishing_frequency


class UpdateDetectorRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    enable: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Specifies whether the detector is enabled or not enabled.</p>"""
    finding_publishing_frequency: NotRequired[
        "capo_guardduty.types.finding_publishing_frequency.FindingPublishingFrequency"
    ]
    """<p>An enum value that specifies how frequently findings are exported, such as to CloudWatch Events.</p>"""
    data_sources: NotRequired[
        "capo_guardduty.types.data_source_configurations.DataSourceConfigurations"
    ]
    """<p>Describes which data sources will be updated.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>"""
    features: NotRequired[
        "capo_guardduty.types.detector_feature_configurations.DetectorFeatureConfigurations"
    ]
    """<p>Provides the features that will be updated for the detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDetectorRequest) -> dict:
    out: dict = {}
    if "enable" in value:
        out["enable"] = value["enable"]
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
    if "features" in value:
        import capo_guardduty.types.detector_feature_configurations

        out["features"] = (
            capo_guardduty.types.detector_feature_configurations.serialize_json(
                value["features"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDetectorRequest:
    out: UpdateDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("enable") is not None:
        out["enable"] = data["enable"]
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
    if data.get("features") is not None:
        import capo_guardduty.types.detector_feature_configurations

        out["features"] = (
            capo_guardduty.types.detector_feature_configurations.deserialize_json(
                data["features"]
            )
        )
    return out
