"""Generated from Smithy shape ``com.amazonaws.ssm#GcpConfigurationTargets``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError
from capo_ssm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm.types.gcp_project_list


class GcpConfigurationTargetsProjectsMember(TypedDict, closed=True):
    Projects: "capo_ssm.types.gcp_project_list.GcpProjectList"


GcpConfigurationTargets: TypeAlias = (
    GcpConfigurationTargetsProjectsMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GcpConfigurationTargets) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GcpConfigurationTargets: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Projects" in value:
        import capo_ssm.types.gcp_project_list

        return {
            "Projects": capo_ssm.types.gcp_project_list.serialize_aws_json_1_1(
                value["Projects"]
            )
        }
    else:
        raise SerializationError("GcpConfigurationTargets: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GcpConfigurationTargets:
    if data.get("Projects") is not None:
        import capo_ssm.types.gcp_project_list

        return {
            "Projects": capo_ssm.types.gcp_project_list.deserialize_aws_json_1_1(
                data["Projects"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GcpConfigurationTargets: no recognized variant key")
