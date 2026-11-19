"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationResourceData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_ec2_instance
    import capo_guardduty.types.investigation_ecs_cluster
    import capo_guardduty.types.investigation_eks_cluster
    import capo_guardduty.types.lambda_function
    import capo_guardduty.types.rds_db_instance
    import capo_guardduty.types.rds_db_user


class InvestigationResourceData(TypedDict, closed=True):
    ec2_instance: NotRequired[
        "capo_guardduty.types.investigation_ec2_instance.InvestigationEc2Instance"
    ]
    """<p>Details about an Amazon EC2 instance.</p>"""
    lambda_function: NotRequired["capo_guardduty.types.lambda_function.LambdaFunction"]
    """<p>Details about an Lambda function.</p>"""
    rds_db_instance: NotRequired["capo_guardduty.types.rds_db_instance.RdsDbInstance"]
    """<p>Details about an Amazon RDS database instance.</p>"""
    rds_db_user: NotRequired["capo_guardduty.types.rds_db_user.RdsDbUser"]
    """<p>Details about the user that logged in to an Amazon RDS database instance.</p>"""
    eks_cluster: NotRequired[
        "capo_guardduty.types.investigation_eks_cluster.InvestigationEksCluster"
    ]
    """<p>Details about an Amazon EKS cluster.</p>"""
    ecs_cluster: NotRequired[
        "capo_guardduty.types.investigation_ecs_cluster.InvestigationEcsCluster"
    ]
    """<p>Details about an Amazon ECS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationResourceData) -> dict:
    out: dict = {}
    if "ec2_instance" in value:
        import capo_guardduty.types.investigation_ec2_instance

        out["ec2Instance"] = (
            capo_guardduty.types.investigation_ec2_instance.serialize_json(
                value["ec2_instance"]
            )
        )
    if "lambda_function" in value:
        import capo_guardduty.types.lambda_function

        out["lambdaFunction"] = capo_guardduty.types.lambda_function.serialize_json(
            value["lambda_function"]
        )
    if "rds_db_instance" in value:
        import capo_guardduty.types.rds_db_instance

        out["rdsDbInstance"] = capo_guardduty.types.rds_db_instance.serialize_json(
            value["rds_db_instance"]
        )
    if "rds_db_user" in value:
        import capo_guardduty.types.rds_db_user

        out["rdsDbUser"] = capo_guardduty.types.rds_db_user.serialize_json(
            value["rds_db_user"]
        )
    if "eks_cluster" in value:
        import capo_guardduty.types.investigation_eks_cluster

        out["eksCluster"] = (
            capo_guardduty.types.investigation_eks_cluster.serialize_json(
                value["eks_cluster"]
            )
        )
    if "ecs_cluster" in value:
        import capo_guardduty.types.investigation_ecs_cluster

        out["ecsCluster"] = (
            capo_guardduty.types.investigation_ecs_cluster.serialize_json(
                value["ecs_cluster"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvestigationResourceData:
    out: InvestigationResourceData = {}  # type: ignore[typeddict-item]
    if data.get("ec2Instance") is not None:
        import capo_guardduty.types.investigation_ec2_instance

        out["ec2_instance"] = (
            capo_guardduty.types.investigation_ec2_instance.deserialize_json(
                data["ec2Instance"]
            )
        )
    if data.get("lambdaFunction") is not None:
        import capo_guardduty.types.lambda_function

        out["lambda_function"] = capo_guardduty.types.lambda_function.deserialize_json(
            data["lambdaFunction"]
        )
    if data.get("rdsDbInstance") is not None:
        import capo_guardduty.types.rds_db_instance

        out["rds_db_instance"] = capo_guardduty.types.rds_db_instance.deserialize_json(
            data["rdsDbInstance"]
        )
    if data.get("rdsDbUser") is not None:
        import capo_guardduty.types.rds_db_user

        out["rds_db_user"] = capo_guardduty.types.rds_db_user.deserialize_json(
            data["rdsDbUser"]
        )
    if data.get("eksCluster") is not None:
        import capo_guardduty.types.investigation_eks_cluster

        out["eks_cluster"] = (
            capo_guardduty.types.investigation_eks_cluster.deserialize_json(
                data["eksCluster"]
            )
        )
    if data.get("ecsCluster") is not None:
        import capo_guardduty.types.investigation_ecs_cluster

        out["ecs_cluster"] = (
            capo_guardduty.types.investigation_ecs_cluster.deserialize_json(
                data["ecsCluster"]
            )
        )
    return out


def redact_sensitive(value: InvestigationResourceData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ec2_instance" in value:
        import capo_guardduty.types.investigation_ec2_instance

        out["ec2_instance"] = (
            capo_guardduty.types.investigation_ec2_instance.redact_sensitive(
                value["ec2_instance"]
            )
        )
    return out
