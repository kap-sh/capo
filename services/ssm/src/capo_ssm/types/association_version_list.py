"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationVersionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.association_version_info

AssociationVersionList: TypeAlias = list[
    "capo_ssm.types.association_version_info.AssociationVersionInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationVersionList) -> list:
    import capo_ssm.types.association_version_info

    out: list = []
    for item in value:
        out.append(capo_ssm.types.association_version_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationVersionList:
    import capo_ssm.types.association_version_info

    out: AssociationVersionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.association_version_info.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: AssociationVersionList) -> list[Any]:
    import capo_ssm.types.association_version_info

    return [
        capo_ssm.types.association_version_info.redact_sensitive(item) for item in value
    ]
