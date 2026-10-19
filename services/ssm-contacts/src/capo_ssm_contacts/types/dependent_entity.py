"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DependentEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn_list
    import capo_ssm_contacts.types.string


class DependentEntity(TypedDict, closed=True):
    relation_type: "capo_ssm_contacts.types.string.String"
    """<p>The type of relationship between one resource and the other resource that it is related to or depends on.</p>"""
    dependent_resource_ids: (
        "capo_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    )
    """<p>The Amazon Resource Names (ARNs) of the dependent resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentEntity) -> dict:
    out: dict = {}
    out["RelationType"] = value["relation_type"]
    import capo_ssm_contacts.types.ssm_contacts_arn_list

    out["DependentResourceIds"] = (
        capo_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
            value["dependent_resource_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DependentEntity:
    out: DependentEntity = {}  # type: ignore[typeddict-item]
    if data.get("RelationType") is not None:
        out["relation_type"] = data["RelationType"]
    else:
        out["relation_type"] = ""
    if data.get("DependentResourceIds") is not None:
        import capo_ssm_contacts.types.ssm_contacts_arn_list

        out["dependent_resource_ids"] = (
            capo_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
                data["DependentResourceIds"]
            )
        )
    else:
        out["dependent_resource_ids"] = []
    return out
