"""Generated from Smithy shape ``com.amazonaws.s3#RestoreStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.is_restore_in_progress
    import capo_s3.types.restore_expiry_date


class RestoreStatus(TypedDict, closed=True):
    is_restore_in_progress: NotRequired[
        "capo_s3.types.is_restore_in_progress.IsRestoreInProgress"
    ]
    """<p>Specifies whether the object is currently being restored. If the object restoration is in progress, the header returns the value <code>TRUE</code>. For example:</p> <p> <code>x-amz-optional-object-attributes: IsRestoreInProgress="true"</code> </p> <p>If the object restoration has completed, the header returns the value <code>FALSE</code>. For example:</p> <p> <code>x-amz-optional-object-attributes: IsRestoreInProgress="false", RestoreExpiryDate="2012-12-21T00:00:00.000Z"</code> </p> <p>If the object hasn't been restored, there is no header response.</p>"""
    restore_expiry_date: NotRequired[
        "capo_s3.types.restore_expiry_date.RestoreExpiryDate"
    ]
    """<p>Indicates when the restored copy will expire. This value is populated only if the object has already been restored. For example:</p> <p> <code>x-amz-optional-object-attributes: IsRestoreInProgress="false", RestoreExpiryDate="2012-12-21T00:00:00.000Z"</code> </p>"""


# --- restXml ser/de ---
def serialize_xml(value: RestoreStatus, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "is_restore_in_progress" in value:
        SubElement(el, "IsRestoreInProgress").text = (
            "true" if value["is_restore_in_progress"] else "false"
        )
    if "restore_expiry_date" in value:
        import capo_s3.types.restore_expiry_date

        capo_s3.types.restore_expiry_date.serialize_xml(
            value["restore_expiry_date"], el, "RestoreExpiryDate"
        )


def deserialize_xml(el: Element) -> RestoreStatus:
    out: RestoreStatus = {}  # type: ignore[typeddict-item]
    child_is_restore_in_progress = el.find("IsRestoreInProgress")
    if child_is_restore_in_progress is not None:
        out["is_restore_in_progress"] = (
            child_is_restore_in_progress.text or ""
        ).lower() == "true"
    child_restore_expiry_date = el.find("RestoreExpiryDate")
    if child_restore_expiry_date is not None:
        import capo_s3.types.restore_expiry_date

        out["restore_expiry_date"] = capo_s3.types.restore_expiry_date.deserialize_xml(
            child_restore_expiry_date
        )
    return out
