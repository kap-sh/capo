"""Generated from Smithy shape ``com.amazonaws.quicksight#RedshiftParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.cluster_id
    import capo_quicksight.types.database
    import capo_quicksight.types.host
    import capo_quicksight.types.identity_center_configuration
    import capo_quicksight.types.optional_port
    import capo_quicksight.types.redshift_iam_parameters


class RedshiftParameters(TypedDict, closed=True):
    host: NotRequired["capo_quicksight.types.host.Host"]
    """<p>Host. This field can be blank if <code>ClusterId</code> is provided.</p>"""
    port: "capo_quicksight.types.optional_port.OptionalPort"
    """<p>Port. This field can be blank if the <code>ClusterId</code> is provided.</p>"""
    database: "capo_quicksight.types.database.Database"
    """<p>Database.</p>"""
    cluster_id: NotRequired["capo_quicksight.types.cluster_id.ClusterId"]
    """<p>Cluster ID. This field can be blank if the <code>Host</code> and <code>Port</code> are provided.</p>"""
    iam_parameters: NotRequired[
        "capo_quicksight.types.redshift_iam_parameters.RedshiftIAMParameters"
    ]
    """<p>An optional parameter that uses IAM authentication to grant Quick Sight access to your cluster. This parameter can be used instead of <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSourceCredentials.html">DataSourceCredentials</a>.</p>"""
    identity_center_configuration: NotRequired[
        "capo_quicksight.types.identity_center_configuration.IdentityCenterConfiguration"
    ]
    """<p>An optional parameter that configures IAM Identity Center authentication to grant Quick Sight access to your cluster.</p> <p>This parameter can only be specified if your Quick Sight account is configured with IAM Identity Center.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftParameters) -> dict:
    out: dict = {}
    if "host" in value:
        out["Host"] = value["host"]
    out["Port"] = value.get("port", 0)
    out["Database"] = value["database"]
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "iam_parameters" in value:
        import capo_quicksight.types.redshift_iam_parameters

        out["IAMParameters"] = (
            capo_quicksight.types.redshift_iam_parameters.serialize_json(
                value["iam_parameters"]
            )
        )
    if "identity_center_configuration" in value:
        import capo_quicksight.types.identity_center_configuration

        out["IdentityCenterConfiguration"] = (
            capo_quicksight.types.identity_center_configuration.serialize_json(
                value["identity_center_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftParameters:
    out: RedshiftParameters = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("RedshiftParameters.database required")
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    if data.get("IAMParameters") is not None:
        import capo_quicksight.types.redshift_iam_parameters

        out["iam_parameters"] = (
            capo_quicksight.types.redshift_iam_parameters.deserialize_json(
                data["IAMParameters"]
            )
        )
    if data.get("IdentityCenterConfiguration") is not None:
        import capo_quicksight.types.identity_center_configuration

        out["identity_center_configuration"] = (
            capo_quicksight.types.identity_center_configuration.deserialize_json(
                data["IdentityCenterConfiguration"]
            )
        )
    return out
