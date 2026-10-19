"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateLakehouseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.catalog_name_string
    import capo_redshift_serverless.types.lakehouse_idc_registration
    import capo_redshift_serverless.types.lakehouse_registration
    import capo_redshift_serverless.types.namespace_name


class UpdateLakehouseConfigurationRequest(TypedDict, closed=True):
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace whose lakehouse configuration you want to modify.</p>"""
    lakehouse_registration: NotRequired[
        "capo_redshift_serverless.types.lakehouse_registration.LakehouseRegistration"
    ]
    """<p>Specifies whether to register or deregister the namespace with Amazon Redshift federated permissions. Valid values are <code>Register</code> or <code>Deregister</code>.</p>"""
    catalog_name: NotRequired[
        "capo_redshift_serverless.types.catalog_name_string.CatalogNameString"
    ]
    """<p>The name of the Glue Data Catalog that will be associated with the namespace enabled with Amazon Redshift federated permissions.</p> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p>"""
    lakehouse_idc_registration: NotRequired[
        "capo_redshift_serverless.types.lakehouse_idc_registration.LakehouseIdcRegistration"
    ]
    """<p>Modifies the Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions. Valid values are <code>Associate</code> or <code>Disassociate</code>.</p>"""
    lakehouse_idc_application_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions.</p>"""
    dry_run: NotRequired["bool"]
    """<p>A boolean value that, if <code>true</code>, validates the request without actually updating the lakehouse configuration. Use this to check for errors before making changes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLakehouseConfigurationRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    if "lakehouse_registration" in value:
        out["lakehouseRegistration"] = value["lakehouse_registration"]
    if "catalog_name" in value:
        out["catalogName"] = value["catalog_name"]
    if "lakehouse_idc_registration" in value:
        out["lakehouseIdcRegistration"] = value["lakehouse_idc_registration"]
    if "lakehouse_idc_application_arn" in value:
        out["lakehouseIdcApplicationArn"] = value["lakehouse_idc_application_arn"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLakehouseConfigurationRequest:
    out: UpdateLakehouseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("lakehouseRegistration") is not None:
        out["lakehouse_registration"] = data["lakehouseRegistration"]
    if data.get("catalogName") is not None:
        out["catalog_name"] = data["catalogName"]
    if data.get("lakehouseIdcRegistration") is not None:
        out["lakehouse_idc_registration"] = data["lakehouseIdcRegistration"]
    if data.get("lakehouseIdcApplicationArn") is not None:
        out["lakehouse_idc_application_arn"] = data["lakehouseIdcApplicationArn"]
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
