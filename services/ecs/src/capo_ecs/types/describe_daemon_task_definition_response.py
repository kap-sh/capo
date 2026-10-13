"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_task_definition


class DescribeDaemonTaskDefinitionResponse(TypedDict, closed=True):
    daemon_task_definition: NotRequired[
        "capo_ecs.types.daemon_task_definition.DaemonTaskDefinition"
    ]
    """<p>The full daemon task definition description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "daemon_task_definition" in value:
        import capo_ecs.types.daemon_task_definition

        out["daemonTaskDefinition"] = (
            capo_ecs.types.daemon_task_definition.serialize_aws_json_1_1(
                value["daemon_task_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonTaskDefinitionResponse:
    out: DescribeDaemonTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("daemonTaskDefinition") is not None:
        import capo_ecs.types.daemon_task_definition

        out["daemon_task_definition"] = (
            capo_ecs.types.daemon_task_definition.deserialize_aws_json_1_1(
                data["daemonTaskDefinition"]
            )
        )
    return out


def redact_sensitive(value: DescribeDaemonTaskDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "daemon_task_definition" in value:
        import capo_ecs.types.daemon_task_definition

        out["daemon_task_definition"] = (
            capo_ecs.types.daemon_task_definition.redact_sensitive(
                value["daemon_task_definition"]
            )
        )
    return out
