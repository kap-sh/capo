"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOrchestratorSlurmConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_accounting_database
    import capo_sagemaker.types.cluster_slurm_config_strategy


class ClusterOrchestratorSlurmConfig(TypedDict, closed=True):
    slurm_config_strategy: NotRequired[
        "capo_sagemaker.types.cluster_slurm_config_strategy.ClusterSlurmConfigStrategy"
    ]
    """<p>The strategy for managing partitions for the Slurm configuration. Valid values are <code>Managed</code>, <code>Overwrite</code>, and <code>Merge</code>.</p>"""
    accounting_database: NotRequired[
        "capo_sagemaker.types.cluster_accounting_database.ClusterAccountingDatabase"
    ]
    """<p>The external database that stores the Slurm accounting data for the cluster, such as job history, associations, and usage. When you omit this field, Slurm accounting uses a database on the cluster's controller node.</p> <note> <p>This field is only supported for clusters using <code>Continuous</code> as the <code>NodeProvisioningMode</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOrchestratorSlurmConfig) -> dict:
    out: dict = {}
    if "slurm_config_strategy" in value:
        import capo_sagemaker.types.cluster_slurm_config_strategy

        out["SlurmConfigStrategy"] = (
            capo_sagemaker.types.cluster_slurm_config_strategy.serialize_aws_json_1_1(
                value["slurm_config_strategy"]
            )
        )
    if "accounting_database" in value:
        import capo_sagemaker.types.cluster_accounting_database

        out["AccountingDatabase"] = (
            capo_sagemaker.types.cluster_accounting_database.serialize_aws_json_1_1(
                value["accounting_database"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterOrchestratorSlurmConfig:
    out: ClusterOrchestratorSlurmConfig = {}  # type: ignore[typeddict-item]
    if data.get("SlurmConfigStrategy") is not None:
        import capo_sagemaker.types.cluster_slurm_config_strategy

        out["slurm_config_strategy"] = (
            capo_sagemaker.types.cluster_slurm_config_strategy.deserialize_aws_json_1_1(
                data["SlurmConfigStrategy"]
            )
        )
    if data.get("AccountingDatabase") is not None:
        import capo_sagemaker.types.cluster_accounting_database

        out["accounting_database"] = (
            capo_sagemaker.types.cluster_accounting_database.deserialize_aws_json_1_1(
                data["AccountingDatabase"]
            )
        )
    return out
