"""Generated from Smithy shape ``com.amazonaws.continuum#AssociateCollectorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.association_client_token
    import capo_continuum.types.collector_arn
    import capo_continuum.types.environment_id
    import capo_continuum.types.environment_source_role_arn


class AssociateCollectorInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier of the Environment making the association."""
    client_token: NotRequired[
        "capo_continuum.types.association_client_token.AssociationClientToken"
    ]
    """Caller-provided token that makes retried association requests idempotent. The first successful request binds the token to the complete Collector ARN, supplied role, and result for at least 24 hours. During that retry window, reusing it with a different request fails with ConflictException. A matching replay still requires the supplied role to have current Collector access. Once authorized, a matching replay returns the stored result without changing association state. Revocation can deny a replay; it does not remove the stored association or its original result."""
    collector_arn: "capo_continuum.types.collector_arn.CollectorArn"
    """The ARN of the Collector to associate with this Environment."""
    collector_data_access_role_arn: (
        "capo_continuum.types.environment_source_role_arn.EnvironmentSourceRoleArn"
    )
    """IAM role in the Environment account that Continuum assumes before authorizing access to associated Collector inventory. Every association, including a same-account association, requires this role. The supplied ARN replaces the Environment's previously stored role. The customer is responsible for granting the role access to every Collector that should contribute data."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateCollectorInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["collectorArn"] = value["collector_arn"]
    out["collectorDataAccessRoleArn"] = value["collector_data_access_role_arn"]
    return out


def deserialize_json(data: dict) -> AssociateCollectorInput:
    out: AssociateCollectorInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("collectorArn") is not None:
        out["collector_arn"] = data["collectorArn"]
    else:
        out["collector_arn"] = ""
    if data.get("collectorDataAccessRoleArn") is not None:
        out["collector_data_access_role_arn"] = data["collectorDataAccessRoleArn"]
    else:
        out["collector_data_access_role_arn"] = ""
    return out
