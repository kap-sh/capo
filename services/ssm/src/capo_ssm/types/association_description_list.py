"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationDescriptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.association_description

AssociationDescriptionList: TypeAlias = list[
    "capo_ssm.types.association_description.AssociationDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationDescriptionList) -> list:
    import capo_ssm.types.association_description

    out: list = []
    for item in value:
        out.append(capo_ssm.types.association_description.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationDescriptionList:
    import capo_ssm.types.association_description

    out: AssociationDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.association_description.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: AssociationDescriptionList) -> list[Any]:
    import capo_ssm.types.association_description

    return [
        capo_ssm.types.association_description.redact_sensitive(item) for item in value
    ]
