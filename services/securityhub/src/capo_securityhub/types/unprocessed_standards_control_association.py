"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedStandardsControlAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.standards_control_association_id
    import capo_securityhub.types.unprocessed_error_code


class UnprocessedStandardsControlAssociation(TypedDict, closed=True):
    standards_control_association_id: NotRequired[
        "capo_securityhub.types.standards_control_association_id.StandardsControlAssociationId"
    ]
    """<p> An array with one or more objects that includes a security control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. This parameter shows the specific controls for which the enablement status couldn't be retrieved in specified standards when calling <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html">BatchUpdateStandardsControlAssociations</a>. </p>"""
    error_code: NotRequired[
        "capo_securityhub.types.unprocessed_error_code.UnprocessedErrorCode"
    ]
    """<p>The error code for the unprocessed standard and control association. The <code>NOT_FOUND</code> value has been deprecated and replaced by the <code>RESOURCE_NOT_FOUND</code> value. </p>"""
    error_reason: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The reason why the standard and control association was unprocessed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStandardsControlAssociation) -> dict:
    out: dict = {}
    if "standards_control_association_id" in value:
        import capo_securityhub.types.standards_control_association_id

        out["StandardsControlAssociationId"] = (
            capo_securityhub.types.standards_control_association_id.serialize_json(
                value["standards_control_association_id"]
            )
        )
    if "error_code" in value:
        import capo_securityhub.types.unprocessed_error_code

        out["ErrorCode"] = capo_securityhub.types.unprocessed_error_code.serialize_json(
            value["error_code"]
        )
    if "error_reason" in value:
        out["ErrorReason"] = value["error_reason"]
    return out


def deserialize_json(data: dict) -> UnprocessedStandardsControlAssociation:
    out: UnprocessedStandardsControlAssociation = {}  # type: ignore[typeddict-item]
    if data.get("StandardsControlAssociationId") is not None:
        import capo_securityhub.types.standards_control_association_id

        out["standards_control_association_id"] = (
            capo_securityhub.types.standards_control_association_id.deserialize_json(
                data["StandardsControlAssociationId"]
            )
        )
    if data.get("ErrorCode") is not None:
        import capo_securityhub.types.unprocessed_error_code

        out["error_code"] = (
            capo_securityhub.types.unprocessed_error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorReason") is not None:
        out["error_reason"] = data["ErrorReason"]
    return out
