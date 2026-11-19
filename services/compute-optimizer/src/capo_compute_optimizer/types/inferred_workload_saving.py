"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InferredWorkloadSaving``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.estimated_monthly_savings
    import capo_compute_optimizer.types.inferred_workload_types


class InferredWorkloadSaving(TypedDict, closed=True):
    inferred_workload_types: NotRequired[
        "capo_compute_optimizer.types.inferred_workload_types.InferredWorkloadTypes"
    ]
    """<p>The applications that might be running on the instance as inferred by Compute Optimizer.</p> <p>Compute Optimizer can infer if one of the following applications might be running on the instance:</p> <ul> <li> <p> <code>AmazonEmr</code> - Infers that Amazon EMR might be running on the instance.</p> </li> <li> <p> <code>ApacheCassandra</code> - Infers that Apache Cassandra might be running on the instance.</p> </li> <li> <p> <code>ApacheHadoop</code> - Infers that Apache Hadoop might be running on the instance.</p> </li> <li> <p> <code>Memcached</code> - Infers that Memcached might be running on the instance.</p> </li> <li> <p> <code>NGINX</code> - Infers that NGINX might be running on the instance.</p> </li> <li> <p> <code>PostgreSql</code> - Infers that PostgreSQL might be running on the instance.</p> </li> <li> <p> <code>Redis</code> - Infers that Redis might be running on the instance.</p> </li> <li> <p> <code>Kafka</code> - Infers that Kafka might be running on the instance.</p> </li> <li> <p> <code>SQLServer</code> - Infers that SQLServer might be running on the instance.</p> </li> </ul>"""
    estimated_monthly_savings: NotRequired[
        "capo_compute_optimizer.types.estimated_monthly_savings.EstimatedMonthlySavings"
    ]
    """<p>An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferredWorkloadSaving) -> dict:
    out: dict = {}
    if "inferred_workload_types" in value:
        import capo_compute_optimizer.types.inferred_workload_types

        out["inferredWorkloadTypes"] = (
            capo_compute_optimizer.types.inferred_workload_types.serialize_aws_json_1_0(
                value["inferred_workload_types"]
            )
        )
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer.types.estimated_monthly_savings.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InferredWorkloadSaving:
    out: InferredWorkloadSaving = {}  # type: ignore[typeddict-item]
    if data.get("inferredWorkloadTypes") is not None:
        import capo_compute_optimizer.types.inferred_workload_types

        out["inferred_workload_types"] = (
            capo_compute_optimizer.types.inferred_workload_types.deserialize_aws_json_1_0(
                data["inferredWorkloadTypes"]
            )
        )
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InferredWorkloadSaving) -> dict:
    out: dict = {}
    if "inferred_workload_types" in value:
        import capo_compute_optimizer.types.inferred_workload_types

        out["inferredWorkloadTypes"] = (
            capo_compute_optimizer.types.inferred_workload_types.serialize_cbor(
                value["inferred_workload_types"]
            )
        )
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer.types.estimated_monthly_savings.serialize_cbor(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> InferredWorkloadSaving:
    out: InferredWorkloadSaving = {}  # type: ignore[typeddict-item]
    if data.get("inferredWorkloadTypes") is not None:
        import capo_compute_optimizer.types.inferred_workload_types

        out["inferred_workload_types"] = (
            capo_compute_optimizer.types.inferred_workload_types.deserialize_cbor(
                data["inferredWorkloadTypes"]
            )
        )
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer.types.estimated_monthly_savings.deserialize_cbor(
                data["estimatedMonthlySavings"]
            )
        )
    return out
