"""Generated from Smithy shape ``com.amazonaws.s3#AnnotationTableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.annotation_configuration_state
    import capo_s3.types.metadata_table_encryption_configuration
    import capo_s3.types.role


class AnnotationTableConfiguration(TypedDict, closed=True):
    configuration_state: (
        "capo_s3.types.annotation_configuration_state.AnnotationConfigurationState"
    )
    """<p>The state of the annotation table. Valid values are <code>ENABLED</code> and <code>DISABLED</code>.</p>"""
    encryption_configuration: NotRequired[
        "capo_s3.types.metadata_table_encryption_configuration.MetadataTableEncryptionConfiguration"
    ]
    role: NotRequired["capo_s3.types.role.Role"]
    """<p>The ARN of the IAM role used to manage the annotation table.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AnnotationTableConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.annotation_configuration_state

    capo_s3.types.annotation_configuration_state.serialize_xml(
        value["configuration_state"], el, "ConfigurationState"
    )
    if "encryption_configuration" in value:
        import capo_s3.types.metadata_table_encryption_configuration

        capo_s3.types.metadata_table_encryption_configuration.serialize_xml(
            value["encryption_configuration"], el, "EncryptionConfiguration"
        )
    if "role" in value:
        SubElement(el, "Role").text = str(value["role"])


def deserialize_xml(el: Element) -> AnnotationTableConfiguration:
    out: AnnotationTableConfiguration = {}  # type: ignore[typeddict-item]
    child_configuration_state = el.find("ConfigurationState")
    if child_configuration_state is not None:
        import capo_s3.types.annotation_configuration_state

        out["configuration_state"] = (
            capo_s3.types.annotation_configuration_state.deserialize_xml(
                child_configuration_state
            )
        )
    else:
        import typing

        out["configuration_state"] = typing.cast(
            "capo_s3.types.annotation_configuration_state.AnnotationConfigurationState",
            "",
        )
    child_encryption_configuration = el.find("EncryptionConfiguration")
    if child_encryption_configuration is not None:
        import capo_s3.types.metadata_table_encryption_configuration

        out["encryption_configuration"] = (
            capo_s3.types.metadata_table_encryption_configuration.deserialize_xml(
                child_encryption_configuration
            )
        )
    child_role = el.find("Role")
    if child_role is not None:
        out["role"] = str(child_role.text or "")
    return out
