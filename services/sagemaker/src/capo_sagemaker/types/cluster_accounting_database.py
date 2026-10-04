"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAccountingDatabase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_accounting_database_endpoint
    import capo_sagemaker.types.cluster_accounting_database_name
    import capo_sagemaker.types.cluster_accounting_database_port
    import capo_sagemaker.types.cluster_accounting_database_secret_arn


class ClusterAccountingDatabase(TypedDict, closed=True):
    endpoint: "capo_sagemaker.types.cluster_accounting_database_endpoint.ClusterAccountingDatabaseEndpoint"
    """<p>The hostname or endpoint of the accounting database, such as the endpoint of an Amazon RDS for MySQL or Aurora MySQL database. The database must be reachable from the subnets and security groups that you configure for the cluster.</p>"""
    port: NotRequired[
        "capo_sagemaker.types.cluster_accounting_database_port.ClusterAccountingDatabasePort"
    ]
    """<p>The port that the accounting database listens on. The default is <code>3306</code>.</p>"""
    name: NotRequired[
        "capo_sagemaker.types.cluster_accounting_database_name.ClusterAccountingDatabaseName"
    ]
    """<p>The name of the database schema that stores the Slurm accounting data. The default is <code>slurm_acct_db_</code> followed by the cluster ID from the cluster ARN, for example <code>slurm_acct_db_a1b2c3d4e5f6</code>.</p>"""
    secret_arn: "capo_sagemaker.types.cluster_accounting_database_secret_arn.ClusterAccountingDatabaseSecretArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the user name and password for the accounting database. The database user must be able to create the schema and to read from and write to it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAccountingDatabase) -> dict:
    out: dict = {}
    out["Endpoint"] = value["endpoint"]
    if "port" in value:
        out["Port"] = value["port"]
    if "name" in value:
        out["Name"] = value["name"]
    out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterAccountingDatabase:
    out: ClusterAccountingDatabase = {}  # type: ignore[typeddict-item]
    if data.get("Endpoint") is not None:
        out["endpoint"] = data["Endpoint"]
    else:
        raise DeserializationError("ClusterAccountingDatabase.endpoint required")
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("ClusterAccountingDatabase.secret_arn required")
    return out
