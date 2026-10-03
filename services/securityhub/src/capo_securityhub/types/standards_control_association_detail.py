"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.association_status
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.related_requirements_list
    import capo_securityhub.types.standards_control_arn_list
    import capo_securityhub.types.timestamp


class StandardsControlAssociationDetail(TypedDict, closed=True):
    standards_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of a security standard. </p>"""
    security_control_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The unique identifier of a security control across standards. Values for this field typically consist of an Amazon Web Services service name and a number, such as APIGateway.3. </p>"""
    security_control_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN of a security control across standards, such as <code>arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1</code>. This parameter doesn't mention a specific standard. </p>"""
    association_status: NotRequired[
        "capo_securityhub.types.association_status.AssociationStatus"
    ]
    """<p> Specifies whether a control is enabled or disabled in a specified standard. </p>"""
    related_requirements: NotRequired[
        "capo_securityhub.types.related_requirements_list.RelatedRequirementsList"
    ]
    """<p> The requirement that underlies a control in the compliance framework related to the standard. </p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> The time at which the enablement status of the control in the specified standard was last updated. </p>"""
    updated_reason: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The reason for updating the enablement status of a control in a specified standard. </p>"""
    standards_control_title: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The title of a control. This field may reference a specific standard. </p>"""
    standards_control_description: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of a control. This typically summarizes how Security Hub CSPM evaluates the control and the conditions under which it produces a failed finding. This parameter may reference a specific standard. </p>"""
    standards_control_arns: NotRequired[
        "capo_securityhub.types.standards_control_arn_list.StandardsControlArnList"
    ]
    """<p> Provides the input parameter that Security Hub CSPM uses to call the <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html">UpdateStandardsControl</a> API. This API can be used to enable or disable a control in a specified standard. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationDetail) -> dict:
    out: dict = {}
    if "standards_arn" in value:
        out["StandardsArn"] = value["standards_arn"]
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "security_control_arn" in value:
        out["SecurityControlArn"] = value["security_control_arn"]
    if "association_status" in value:
        import capo_securityhub.types.association_status

        out["AssociationStatus"] = (
            capo_securityhub.types.association_status.serialize_json(
                value["association_status"]
            )
        )
    if "related_requirements" in value:
        import capo_securityhub.types.related_requirements_list

        out["RelatedRequirements"] = (
            capo_securityhub.types.related_requirements_list.serialize_json(
                value["related_requirements"]
            )
        )
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "updated_reason" in value:
        out["UpdatedReason"] = value["updated_reason"]
    if "standards_control_title" in value:
        out["StandardsControlTitle"] = value["standards_control_title"]
    if "standards_control_description" in value:
        out["StandardsControlDescription"] = value["standards_control_description"]
    if "standards_control_arns" in value:
        import capo_securityhub.types.standards_control_arn_list

        out["StandardsControlArns"] = (
            capo_securityhub.types.standards_control_arn_list.serialize_json(
                value["standards_control_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardsControlAssociationDetail:
    out: StandardsControlAssociationDetail = {}  # type: ignore[typeddict-item]
    if data.get("StandardsArn") is not None:
        out["standards_arn"] = data["StandardsArn"]
    if data.get("SecurityControlId") is not None:
        out["security_control_id"] = data["SecurityControlId"]
    if data.get("SecurityControlArn") is not None:
        out["security_control_arn"] = data["SecurityControlArn"]
    if data.get("AssociationStatus") is not None:
        import capo_securityhub.types.association_status

        out["association_status"] = (
            capo_securityhub.types.association_status.deserialize_json(
                data["AssociationStatus"]
            )
        )
    if data.get("RelatedRequirements") is not None:
        import capo_securityhub.types.related_requirements_list

        out["related_requirements"] = (
            capo_securityhub.types.related_requirements_list.deserialize_json(
                data["RelatedRequirements"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if data.get("UpdatedReason") is not None:
        out["updated_reason"] = data["UpdatedReason"]
    if data.get("StandardsControlTitle") is not None:
        out["standards_control_title"] = data["StandardsControlTitle"]
    if data.get("StandardsControlDescription") is not None:
        out["standards_control_description"] = data["StandardsControlDescription"]
    if data.get("StandardsControlArns") is not None:
        import capo_securityhub.types.standards_control_arn_list

        out["standards_control_arns"] = (
            capo_securityhub.types.standards_control_arn_list.deserialize_json(
                data["StandardsControlArns"]
            )
        )
    return out
