"""Generated from Smithy shape ``com.amazonaws.cloud9#DescribeEnvironmentStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_status
    import capo_cloud9.types.string


class DescribeEnvironmentStatusResult(TypedDict, closed=True):
    status: "capo_cloud9.types.environment_status.EnvironmentStatus"
    """<p>The status of the environment. Available values include:</p> <ul> <li> <p> <code>connecting</code>: The environment is connecting.</p> </li> <li> <p> <code>creating</code>: The environment is being created.</p> </li> <li> <p> <code>deleting</code>: The environment is being deleted.</p> </li> <li> <p> <code>error</code>: The environment is in an error state.</p> </li> <li> <p> <code>ready</code>: The environment is ready.</p> </li> <li> <p> <code>stopped</code>: The environment is stopped.</p> </li> <li> <p> <code>stopping</code>: The environment is stopping.</p> </li> </ul>"""
    message: "capo_cloud9.types.string.String"
    """<p>Any informational message about the status of the environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEnvironmentStatusResult) -> dict:
    out: dict = {}
    import capo_cloud9.types.environment_status

    out["status"] = capo_cloud9.types.environment_status.serialize_aws_json_1_1(
        value["status"]
    )
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEnvironmentStatusResult:
    out: DescribeEnvironmentStatusResult = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_cloud9.types.environment_status

        out["status"] = capo_cloud9.types.environment_status.deserialize_aws_json_1_1(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cloud9.types.environment_status.EnvironmentStatus", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
