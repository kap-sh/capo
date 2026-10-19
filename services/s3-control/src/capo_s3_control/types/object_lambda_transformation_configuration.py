"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaTransformationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.object_lambda_content_transformation
    import capo_s3_control.types.object_lambda_transformation_configuration_actions_list


class ObjectLambdaTransformationConfiguration(TypedDict, closed=True):
    actions: "capo_s3_control.types.object_lambda_transformation_configuration_actions_list.ObjectLambdaTransformationConfigurationActionsList"
    """<p>A container for the action of an Object Lambda Access Point configuration. Valid inputs are <code>GetObject</code>, <code>ListObjects</code>, <code>HeadObject</code>, and <code>ListObjectsV2</code>.</p>"""
    content_transformation: "capo_s3_control.types.object_lambda_content_transformation.ObjectLambdaContentTransformation"
    """<p>A container for the content transformation of an Object Lambda Access Point configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaTransformationConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.object_lambda_transformation_configuration_actions_list

    capo_s3_control.types.object_lambda_transformation_configuration_actions_list.serialize_xml(
        value["actions"], el, "Actions"
    )
    import capo_s3_control.types.object_lambda_content_transformation

    capo_s3_control.types.object_lambda_content_transformation.serialize_xml(
        value["content_transformation"], el, "ContentTransformation"
    )


def deserialize_xml(el: Element) -> ObjectLambdaTransformationConfiguration:
    out: ObjectLambdaTransformationConfiguration = {}  # type: ignore[typeddict-item]
    child_actions = el.find("Actions")
    if child_actions is not None:
        import capo_s3_control.types.object_lambda_transformation_configuration_actions_list

        out["actions"] = (
            capo_s3_control.types.object_lambda_transformation_configuration_actions_list.deserialize_xml(
                child_actions
            )
        )
    else:
        out["actions"] = []
    child_content_transformation = el.find("ContentTransformation")
    if child_content_transformation is not None:
        import capo_s3_control.types.object_lambda_content_transformation

        out["content_transformation"] = (
            capo_s3_control.types.object_lambda_content_transformation.deserialize_xml(
                child_content_transformation
            )
        )
    else:
        import capo_s3_control.types._unknown

        out["content_transformation"] = (
            capo_s3_control.types._unknown.UnknownUnionMember("")
        )
    return out
