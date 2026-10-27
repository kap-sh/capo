"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateFleetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_configuration
    import capo_deadline.types.fleet_id
    import capo_deadline.types.host_configuration
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.min_zero_max_integer
    import capo_deadline.types.resource_name


class UpdateFleetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID to update."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID to update."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""
    display_name: NotRequired["capo_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the fleet to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the fleet to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    role_arn: NotRequired["capo_deadline.types.iam_role_arn.IamRoleArn"]
    """The IAM role ARN that the fleet's workers assume while running jobs."""
    min_worker_count: NotRequired[
        "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    ]
    """The minimum number of workers in the fleet."""
    max_worker_count: NotRequired[
        "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    ]
    """The maximum number of workers in the fleet. Deadline Cloud limits the number of workers to less than or equal to the fleet's maximum worker count. The service maintains eventual consistency for the worker count. If you make multiple rapid calls to <code>CreateWorker</code> before the field updates, you might exceed your fleet's maximum worker count. For example, if your <code>maxWorkerCount</code> is 10 and you currently have 9 workers, making two quick <code>CreateWorker</code> calls might successfully create 2 workers instead of 1, resulting in 11 total workers."""
    configuration: NotRequired[
        "capo_deadline.types.fleet_configuration.FleetConfiguration"
    ]
    """The fleet configuration to update."""
    host_configuration: NotRequired[
        "capo_deadline.types.host_configuration.HostConfiguration"
    ]
    """Provides a script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFleetRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "min_worker_count" in value:
        out["minWorkerCount"] = value["min_worker_count"]
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "configuration" in value:
        import capo_deadline.types.fleet_configuration

        out["configuration"] = capo_deadline.types.fleet_configuration.serialize_json(
            value["configuration"]
        )
    if "host_configuration" in value:
        import capo_deadline.types.host_configuration

        out["hostConfiguration"] = (
            capo_deadline.types.host_configuration.serialize_json(
                value["host_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFleetRequest:
    out: UpdateFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("minWorkerCount") is not None:
        out["min_worker_count"] = data["minWorkerCount"]
    if data.get("maxWorkerCount") is not None:
        out["max_worker_count"] = data["maxWorkerCount"]
    if data.get("configuration") is not None:
        import capo_deadline.types.fleet_configuration

        out["configuration"] = capo_deadline.types.fleet_configuration.deserialize_json(
            data["configuration"]
        )
    if data.get("hostConfiguration") is not None:
        import capo_deadline.types.host_configuration

        out["host_configuration"] = (
            capo_deadline.types.host_configuration.deserialize_json(
                data["hostConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateFleetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "host_configuration" in value:
        import capo_deadline.types.host_configuration

        out["host_configuration"] = (
            capo_deadline.types.host_configuration.redact_sensitive(
                value["host_configuration"]
            )
        )
    return out
