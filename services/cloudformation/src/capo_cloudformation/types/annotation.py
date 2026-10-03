"""Generated from Smithy shape ``com.amazonaws.cloudformation#Annotation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.annotation_name
    import capo_cloudformation.types.annotation_remediation_link
    import capo_cloudformation.types.annotation_severity_level
    import capo_cloudformation.types.annotation_status
    import capo_cloudformation.types.remediation_message_remediation_message
    import capo_cloudformation.types.remediation_message_status_message


class Annotation(TypedDict, closed=True):
    annotation_name: NotRequired[
        "capo_cloudformation.types.annotation_name.AnnotationName"
    ]
    """<p>An identifier for the evaluation logic that was used when invoking the Hook. For Control Tower, this is the control ID. For Guard, this is the rule ID. For Lambda and custom Hooks, this is a user-defined identifier.</p>"""
    status: NotRequired["capo_cloudformation.types.annotation_status.AnnotationStatus"]
    """<p>The status of the Hook invocation from the downstream service.</p>"""
    status_message: NotRequired[
        "capo_cloudformation.types.remediation_message_status_message.RemediationMessageStatusMessage"
    ]
    """<p>The explanation for the specific status assigned to this Hook invocation. For example, "Bucket does not block public access".</p>"""
    remediation_message: NotRequired[
        "capo_cloudformation.types.remediation_message_remediation_message.RemediationMessageRemediationMessage"
    ]
    """<p>Suggests what to change if your Hook returns a <code>FAILED</code> status. For example, "Block public access to the bucket".</p>"""
    remediation_link: NotRequired[
        "capo_cloudformation.types.annotation_remediation_link.AnnotationRemediationLink"
    ]
    """<p>A URL that you can access for additional remediation guidance.</p>"""
    severity_level: NotRequired[
        "capo_cloudformation.types.annotation_severity_level.AnnotationSeverityLevel"
    ]
    """<p>The relative risk associated with any violations of this type.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Annotation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "annotation_name" in value:
        pairs.append((f"{key_prefix}AnnotationName", str(value["annotation_name"])))
    if "status" in value:
        import capo_cloudformation.types.annotation_status

        capo_cloudformation.types.annotation_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "remediation_message" in value:
        pairs.append(
            (f"{key_prefix}RemediationMessage", str(value["remediation_message"]))
        )
    if "remediation_link" in value:
        pairs.append((f"{key_prefix}RemediationLink", str(value["remediation_link"])))
    if "severity_level" in value:
        import capo_cloudformation.types.annotation_severity_level

        capo_cloudformation.types.annotation_severity_level.serialize_query(
            value["severity_level"], pairs, f"{key_prefix}SeverityLevel"
        )


def deserialize_query(el: Element) -> Annotation:
    out: Annotation = {}  # type: ignore[typeddict-item]
    child_annotation_name = el.find("AnnotationName")
    if child_annotation_name is not None:
        out["annotation_name"] = str(child_annotation_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.annotation_status

        out["status"] = capo_cloudformation.types.annotation_status.deserialize_query(
            child_status
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_remediation_message = el.find("RemediationMessage")
    if child_remediation_message is not None:
        out["remediation_message"] = str(child_remediation_message.text or "")
    child_remediation_link = el.find("RemediationLink")
    if child_remediation_link is not None:
        out["remediation_link"] = str(child_remediation_link.text or "")
    child_severity_level = el.find("SeverityLevel")
    if child_severity_level is not None:
        import capo_cloudformation.types.annotation_severity_level

        out["severity_level"] = (
            capo_cloudformation.types.annotation_severity_level.deserialize_query(
                child_severity_level
            )
        )
    return out
