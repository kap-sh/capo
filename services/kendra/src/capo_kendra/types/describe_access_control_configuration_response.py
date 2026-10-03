"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeAccessControlConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_name
    import capo_kendra.types.description
    import capo_kendra.types.error_message
    import capo_kendra.types.hierarchical_principal_list
    import capo_kendra.types.principal_list


class DescribeAccessControlConfigurationResponse(TypedDict, closed=True):
    name: "capo_kendra.types.access_control_configuration_name.AccessControlConfigurationName"
    """<p>The name for the access control configuration.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>The description for the access control configuration.</p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>The error message containing details if there are issues processing the access control configuration.</p>"""
    access_control_list: NotRequired["capo_kendra.types.principal_list.PrincipalList"]
    """<p>Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>"""
    hierarchical_access_control_list: NotRequired[
        "capo_kendra.types.hierarchical_principal_list.HierarchicalPrincipalList"
    ]
    """<p>The list of <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html">principal</a> lists that define the hierarchy for which documents users should have access to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccessControlConfigurationResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "access_control_list" in value:
        import capo_kendra.types.principal_list

        out["AccessControlList"] = (
            capo_kendra.types.principal_list.serialize_aws_json_1_1(
                value["access_control_list"]
            )
        )
    if "hierarchical_access_control_list" in value:
        import capo_kendra.types.hierarchical_principal_list

        out["HierarchicalAccessControlList"] = (
            capo_kendra.types.hierarchical_principal_list.serialize_aws_json_1_1(
                value["hierarchical_access_control_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccessControlConfigurationResponse:
    out: DescribeAccessControlConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "DescribeAccessControlConfigurationResponse.name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("AccessControlList") is not None:
        import capo_kendra.types.principal_list

        out["access_control_list"] = (
            capo_kendra.types.principal_list.deserialize_aws_json_1_1(
                data["AccessControlList"]
            )
        )
    if data.get("HierarchicalAccessControlList") is not None:
        import capo_kendra.types.hierarchical_principal_list

        out["hierarchical_access_control_list"] = (
            capo_kendra.types.hierarchical_principal_list.deserialize_aws_json_1_1(
                data["HierarchicalAccessControlList"]
            )
        )
    return out
