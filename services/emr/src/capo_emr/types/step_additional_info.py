"""Generated from Smithy shape ``com.amazonaws.emr#StepAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.string
    import capo_emr.types.string_list


class StepAdditionalInfo(TypedDict, closed=True):
    resource_manager_application_ids: NotRequired[
        "capo_emr.types.string_list.StringList"
    ]
    """<p>The YARN application IDs associated with the step.</p>"""
    resource_manager: NotRequired["capo_emr.types.string.String"]
    """<p>The address of the YARN resource manager that processed the step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepAdditionalInfo) -> dict:
    out: dict = {}
    if "resource_manager_application_ids" in value:
        import capo_emr.types.string_list

        out["ResourceManagerApplicationIds"] = (
            capo_emr.types.string_list.serialize_aws_json_1_1(
                value["resource_manager_application_ids"]
            )
        )
    if "resource_manager" in value:
        out["ResourceManager"] = value["resource_manager"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StepAdditionalInfo:
    out: StepAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("ResourceManagerApplicationIds") is not None:
        import capo_emr.types.string_list

        out["resource_manager_application_ids"] = (
            capo_emr.types.string_list.deserialize_aws_json_1_1(
                data["ResourceManagerApplicationIds"]
            )
        )
    if data.get("ResourceManager") is not None:
        out["resource_manager"] = data["ResourceManager"]
    return out
