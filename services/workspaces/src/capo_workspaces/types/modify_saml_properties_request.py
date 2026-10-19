"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifySamlPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.deletable_saml_properties_list
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.saml_properties


class ModifySamlPropertiesRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier for which you want to configure SAML properties.</p>"""
    saml_properties: NotRequired["capo_workspaces.types.saml_properties.SamlProperties"]
    """<p>The properties for configuring SAML 2.0 authentication.</p>"""
    properties_to_delete: NotRequired[
        "capo_workspaces.types.deletable_saml_properties_list.DeletableSamlPropertiesList"
    ]
    """<p>The SAML properties to delete as part of your request.</p> <p>Specify one of the following options:</p> <ul> <li> <p> <code>SAML_PROPERTIES_USER_ACCESS_URL</code> to delete the user access URL.</p> </li> <li> <p> <code>SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME</code> to delete the relay state parameter name.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifySamlPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "saml_properties" in value:
        import capo_workspaces.types.saml_properties

        out["SamlProperties"] = (
            capo_workspaces.types.saml_properties.serialize_aws_json_1_1(
                value["saml_properties"]
            )
        )
    if "properties_to_delete" in value:
        import capo_workspaces.types.deletable_saml_properties_list

        out["PropertiesToDelete"] = (
            capo_workspaces.types.deletable_saml_properties_list.serialize_aws_json_1_1(
                value["properties_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifySamlPropertiesRequest:
    out: ModifySamlPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("SamlProperties") is not None:
        import capo_workspaces.types.saml_properties

        out["saml_properties"] = (
            capo_workspaces.types.saml_properties.deserialize_aws_json_1_1(
                data["SamlProperties"]
            )
        )
    if data.get("PropertiesToDelete") is not None:
        import capo_workspaces.types.deletable_saml_properties_list

        out["properties_to_delete"] = (
            capo_workspaces.types.deletable_saml_properties_list.deserialize_aws_json_1_1(
                data["PropertiesToDelete"]
            )
        )
    return out
