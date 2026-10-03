"""Generated from Smithy shape ``com.amazonaws.kendra#CreateAccessControlConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_name
    import capo_kendra.types.client_token_name
    import capo_kendra.types.description
    import capo_kendra.types.hierarchical_principal_list
    import capo_kendra.types.index_id
    import capo_kendra.types.principal_list


class CreateAccessControlConfigurationRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index to create an access control configuration for your documents.</p>"""
    name: "capo_kendra.types.access_control_configuration_name.AccessControlConfigurationName"
    """<p>A name for the access control configuration.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A description for the access control configuration.</p>"""
    access_control_list: NotRequired["capo_kendra.types.principal_list.PrincipalList"]
    """<p>Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>"""
    hierarchical_access_control_list: NotRequired[
        "capo_kendra.types.hierarchical_principal_list.HierarchicalPrincipalList"
    ]
    """<p>The list of <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html">principal</a> lists that define the hierarchy for which documents users should have access to.</p>"""
    client_token: NotRequired["capo_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create an access control configuration. Multiple calls to the <code>CreateAccessControlConfiguration</code> API with the same client token will create only one access control configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccessControlConfigurationRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccessControlConfigurationRequest:
    out: CreateAccessControlConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "CreateAccessControlConfigurationRequest.index_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "CreateAccessControlConfigurationRequest.name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
