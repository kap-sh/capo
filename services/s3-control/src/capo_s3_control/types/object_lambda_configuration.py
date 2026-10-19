"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.boolean
    import capo_s3_control.types.object_lambda_allowed_features_list
    import capo_s3_control.types.object_lambda_supporting_access_point_arn
    import capo_s3_control.types.object_lambda_transformation_configurations_list


class ObjectLambdaConfiguration(TypedDict, closed=True):
    supporting_access_point: "capo_s3_control.types.object_lambda_supporting_access_point_arn.ObjectLambdaSupportingAccessPointArn"
    """<p>Standard access point associated with the Object Lambda Access Point.</p>"""
    cloud_watch_metrics_enabled: "capo_s3_control.types.boolean.Boolean"
    """<p>A container for whether the CloudWatch metrics configuration is enabled.</p>"""
    allowed_features: NotRequired[
        "capo_s3_control.types.object_lambda_allowed_features_list.ObjectLambdaAllowedFeaturesList"
    ]
    """<p>A container for allowed features. Valid inputs are <code>GetObject-Range</code>, <code>GetObject-PartNumber</code>, <code>HeadObject-Range</code>, and <code>HeadObject-PartNumber</code>.</p>"""
    transformation_configurations: "capo_s3_control.types.object_lambda_transformation_configurations_list.ObjectLambdaTransformationConfigurationsList"
    """<p>A container for transformation configurations for an Object Lambda Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectLambdaConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "SupportingAccessPoint").text = str(value["supporting_access_point"])
    SubElement(el, "CloudWatchMetricsEnabled").text = (
        "true" if value.get("cloud_watch_metrics_enabled", False) else "false"
    )
    if "allowed_features" in value:
        import capo_s3_control.types.object_lambda_allowed_features_list

        capo_s3_control.types.object_lambda_allowed_features_list.serialize_xml(
            value["allowed_features"], el, "AllowedFeatures"
        )
    import capo_s3_control.types.object_lambda_transformation_configurations_list

    capo_s3_control.types.object_lambda_transformation_configurations_list.serialize_xml(
        value["transformation_configurations"], el, "TransformationConfigurations"
    )


def deserialize_xml(el: Element) -> ObjectLambdaConfiguration:
    out: ObjectLambdaConfiguration = {}  # type: ignore[typeddict-item]
    child_supporting_access_point = el.find("SupportingAccessPoint")
    if child_supporting_access_point is not None:
        out["supporting_access_point"] = str(child_supporting_access_point.text or "")
    else:
        out["supporting_access_point"] = ""
    child_cloud_watch_metrics_enabled = el.find("CloudWatchMetricsEnabled")
    if child_cloud_watch_metrics_enabled is not None:
        out["cloud_watch_metrics_enabled"] = (
            child_cloud_watch_metrics_enabled.text or ""
        ).lower() == "true"
    else:
        out["cloud_watch_metrics_enabled"] = False
    child_allowed_features = el.find("AllowedFeatures")
    if child_allowed_features is not None:
        import capo_s3_control.types.object_lambda_allowed_features_list

        out["allowed_features"] = (
            capo_s3_control.types.object_lambda_allowed_features_list.deserialize_xml(
                child_allowed_features
            )
        )
    child_transformation_configurations = el.find("TransformationConfigurations")
    if child_transformation_configurations is not None:
        import capo_s3_control.types.object_lambda_transformation_configurations_list

        out["transformation_configurations"] = (
            capo_s3_control.types.object_lambda_transformation_configurations_list.deserialize_xml(
                child_transformation_configurations
            )
        )
    else:
        out["transformation_configurations"] = []
    return out
