"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerRestartPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.integer_list


class ContainerRestartPolicy(TypedDict, closed=True):
    enabled: "capo_ecs.types.boxed_boolean.BoxedBoolean"
    """<p>Specifies whether a restart policy is enabled for the container.</p>"""
    ignored_exit_codes: NotRequired["capo_ecs.types.integer_list.IntegerList"]
    """<p>A list of exit codes that Amazon ECS will ignore and not attempt a restart on. You can specify a maximum of 50 container exit codes. By default, Amazon ECS does not ignore any exit codes.</p>"""
    restart_attempt_period: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>A period of time (in seconds) that the container must run for before a restart can be attempted. A container can be restarted only once every <code>restartAttemptPeriod</code> seconds. If a container isn't able to run for this time period and exits early, it will not be restarted. You can set a minimum <code>restartAttemptPeriod</code> of 60 seconds and a maximum <code>restartAttemptPeriod</code> of 1800 seconds. By default, a container must run for 300 seconds before it can be restarted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerRestartPolicy) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "ignored_exit_codes" in value:
        import capo_ecs.types.integer_list

        out["ignoredExitCodes"] = capo_ecs.types.integer_list.serialize_aws_json_1_1(
            value["ignored_exit_codes"]
        )
    if "restart_attempt_period" in value:
        out["restartAttemptPeriod"] = value["restart_attempt_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerRestartPolicy:
    out: ContainerRestartPolicy = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("ignoredExitCodes") is not None:
        import capo_ecs.types.integer_list

        out["ignored_exit_codes"] = (
            capo_ecs.types.integer_list.deserialize_aws_json_1_1(
                data["ignoredExitCodes"]
            )
        )
    if data.get("restartAttemptPeriod") is not None:
        out["restart_attempt_period"] = data["restartAttemptPeriod"]
    return out
