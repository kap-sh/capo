"""Generated from Smithy shape ``com.amazonaws.inspector#AddAttributesToFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.add_remove_attributes_finding_arn_list
    import capo_inspector.types.user_attribute_list


class AddAttributesToFindingsRequest(TypedDict, closed=True):
    finding_arns: "capo_inspector.types.add_remove_attributes_finding_arn_list.AddRemoveAttributesFindingArnList"
    """<p>The ARNs that specify the findings that you want to assign attributes to.</p>"""
    attributes: "capo_inspector.types.user_attribute_list.UserAttributeList"
    """<p>The array of attributes that you want to assign to specified findings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddAttributesToFindingsRequest) -> dict:
    out: dict = {}
    import capo_inspector.types.add_remove_attributes_finding_arn_list

    out["findingArns"] = (
        capo_inspector.types.add_remove_attributes_finding_arn_list.serialize_aws_json_1_1(
            value["finding_arns"]
        )
    )
    import capo_inspector.types.user_attribute_list

    out["attributes"] = capo_inspector.types.user_attribute_list.serialize_aws_json_1_1(
        value["attributes"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddAttributesToFindingsRequest:
    out: AddAttributesToFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingArns") is not None:
        import capo_inspector.types.add_remove_attributes_finding_arn_list

        out["finding_arns"] = (
            capo_inspector.types.add_remove_attributes_finding_arn_list.deserialize_aws_json_1_1(
                data["findingArns"]
            )
        )
    else:
        out["finding_arns"] = []
    if data.get("attributes") is not None:
        import capo_inspector.types.user_attribute_list

        out["attributes"] = (
            capo_inspector.types.user_attribute_list.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    else:
        out["attributes"] = []
    return out
